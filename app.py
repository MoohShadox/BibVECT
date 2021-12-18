import bibtexparser
from owlready2 import *
from flask import Flask, render_template, redirect, request, send_from_directory, send_file, url_for, make_response
import os

from werkzeug.utils import secure_filename

from kb import get_world_ontology, init_world_ontology, save
import requests
from datetime import datetime
from query_articles import download_article, get_doi_id

import subprocess
import tempfile

app = Flask(__name__)
RESET = False
articles_directory = "articles"
markdowns_directory = "markdowns"

if not os.path.exists(articles_directory):
    os.makedirs(articles_directory)

if not os.path.exists(markdowns_directory):
    os.makedirs(markdowns_directory)

if not (os.path.exists("bib.owl") and os.path.exists("bib.sqlite3")) or RESET :
    world, ontology = init_world_ontology()
    print("Found files: ", os.listdir("."))
    print("Initialisation ! ")
else:
    world, ontology = get_world_ontology()
    print("Onotology Loading ! ")

@app.route('/')
def home():
    ##We Create an "all" bibliography
    all_bib = ontology.search_one(type = ontology.Bibliography, label="All")
    if not all_bib:
        all_bib = ontology.Bibliography(label="All")
        all_bib.bibliographyDate = datetime.now()

    articles = ontology.search(type=ontology.Article)
    if(len(articles) > 0):
        all_bib.bibliographyContains = articles
        all_bib.bibliographyDate = datetime.now()

    bibliographies = ontology.search(type=ontology.Bibliography)
    L = []
    for bibliography in bibliographies:
        D = {
            "name":bibliography.label[0],
            "date":bibliography.bibliographyDate.strftime("%d %b %Y %H:%M"),
            "n": len(bibliography.bibliographyContains)
        }
        L.append(D)
    return render_template("index.html", bibliographies=L)


@app.route('/dl_bib/<name>')
def dl_bib(name):
    f = open("f.tmp", "w")
    bib = ontology.search_one(type = ontology.Bibliography, label = name)
    ref = ""
    if(len(bib.bibliographyContains) > 0):
        for article in bib.bibliographyContains:
            ref += article.bibtexReference + "\n"
    f.write(ref)
    f.close()
    return send_file("f.tmp", as_attachment=True, attachment_filename=name+".bibtex")

@app.route("/new_bib", methods=["POST", "GET"])
def new_bib():
    if(request.method == "POST"):
        name = request.form["name"]
        bibliography = ontology.Bibliography(label = name, bibliographyDate = datetime.now() )
    return redirect("/")


@app.route("/browse/<name>", methods=["POST", "GET"])
def browse(name):
    bibliography = ontology.search_one(type = ontology.Bibliography, label = name)
    L = []
    for article in bibliography.bibliographyContains:
        D = {
            "title":article.title,
            "author":article.author,
            "journal":article.journal,
            "ID":article.articleID,
        }
        L.append(D)

    return render_template("browse.html", articles=L, bibliograhy_name=name)

@app.route("/view_pdf/<ID>")
def view_pdf(ID):
    article = ontology.search_one(articleID = ID)
    binary_pdf = open(article.inFile, "rb").read()
    response = make_response(binary_pdf)
    response.headers['Content-Type'] = 'application/pdf'
    response.headers['Content-Disposition'] = \
        'inline; filename=%s.pdf' % 'yourfilename'
    return response

@app.route("/dl_citation/<id>")
def dl_citation(id):
    article = ontology.search_one(articleID = id)
    if(article):
        return article.bibtexReference


@app.route("/rm_article/<name>/<id>")
def rm_article(name, id):
    article = ontology.search_one(type = ontology.Article, articleID = id)
    bib = ontology.search_one(type = ontology.Bibliography, label = name)
    bib.bibliographyContains.remove(article)
    if(name == "All"):
        destroy_entity(article)
    world.save()
    ontology.save()
    return redirect("/browse/"+name)


def get_default_id():
    articles = ontology.search(type = ontology.Article)
    return "A" + str(len(articles) + 1)



@app.route("/manual_add/<bib_name>", methods=["POST"])
def manual_add(bib_name):
    bibtex = request.form["bibtex"].strip()
    file = request.files['file']
    bib = bibtexparser.loads(bibtex).entries[0]
    print("bib: ", bib, " of type  : ", type(bib))
    file_path = os.path.join(articles_directory, secure_filename(file.filename))
    file.save(os.path.join(articles_directory,secure_filename(file.filename)))
    article = ontology.Article(doi="NOT AVAILABLE",
                               found=True,
                               inFile=file_path,
                               bibtexReference=bibtex ,
                               title=bib["title"]  if "title" in bib else "UNKNOWN",
                               author=bib["author"]  if "author" in bib else "UNKNOWN" ,
                               journal=bib["journal"] if "journal" in bib else "UNKNOWN",
                               publicationYear=int(bib["year"])  if "year" in bib else 0000 ,
                               articleID=bib["ID"]  if "ID" in bib else get_default_id(),
                               )

    bib = ontology.search_one(type = ontology.Bibliography, label = bib_name)
    if(article not in bib.bibliographyContains):
        bib.bibliographyContains.append(article)
    world.save()
    ontology.save()
    return redirect("/browse/"+bib_name)



@app.route("/edit_review/<article_ID>", methods=["POST", "GET"])
def edit_review(article_ID):
    article = ontology.search_one(type=ontology.Article, articleID=article_ID)
    content = None
    print("content loaded: ", article.articleReview)
    if (article.articleReview):
        content = article.articleReview
    return render_template("edit.html", id=article_ID, content=content)

@app.route("/save_review/<article_ID>", methods=["POST"])
def save_review(article_ID):
    article = ontology.search_one(type=ontology.Article, articleID = article_ID)
    content = request.form["content"]
    article.articleReview = content
    ontology.save()
    world.save()
    print("Saved: ", content)
    return redirect(f"/see_review/{article_ID}")


@app.route("/see_review/<article_ID>", methods=["POST", "GET"])
def see_review(article_ID):
    article = ontology.search_one(type=ontology.Article, articleID = article_ID)
    review = None
    if(article.articleReview):
        review = article.articleReview
    return render_template("see_review.html", review = review, id = article_ID)

def remove_lower(s):
    return ''.join(ch for ch in s if ch.isupper())

@app.route("/browse_dir/<article_id>", methods=["POST", "GET"])
def browse_dir(article_id):
    article = ontology.search_one(type=ontology.Article, articleID = article_id)
    if not article.hasDir:
        article.hasDir = os.path.join(markdowns_directory, article_id)
        if not os.path.exists(article.hasDir):
            os.makedirs(article.hasDir)
    files = [i for i in os.listdir(article.hasDir) if i.endswith(".md")]
    return render_template("browse_md.html", files = files, id= article_id)

@app.route("/open_md/<articleID>/<file>", methods=["POST", "GET"])
def open_typora(articleID, file):
    article = ontology.search_one(type=ontology.Article, articleID = articleID)
    file = os.path.join(article.hasDir, file)
    subprocess.run(["typora", file])
    return redirect("/browse_dir/"+articleID)



@app.route("/new_md/<article_id>", methods=["POST", "GET"])
def new_md(article_id):
    if(request.method == "POST"):
        name = request.form["name"]
        article = ontology.search_one(type=ontology.Article, articleID=article_id)
        art_dir = os.path.join(article.hasDir, name)
        if not os.path.exists(art_dir):
            f = open(art_dir + ".md", "w")
    return redirect("/browse_dir/"+article_id)


@app.route("/new_article/<bib_name>", methods=["POST"])
def new_article(bib_name):
    doi = request.form["doi"].strip()
    article = ontology.search_one(doi = doi)
    if(not article):
        print("not found article , downloading it ! ")
        bib,bib_str, name_file = download_article(doi, articles_directory)
        print("Downloaded: ", bib)
        article = ontology.Article(doi = doi,
                                   found= True,
                                   inFile = name_file,
                                   bibtexReference = bib_str,
                                   title=bib["title"],
                                   author=bib["author"],
                                   journal=bib["journal"] if "journal" in  bib else (bib["publisher"] if "publisher" in bib else "NOT SPECIFIED"),
                                   publicationYear = int(bib["year"]),
                                   articleID = remove_lower(name_file.split("/")[-1].split(".")[0]),
                                   )
    bib = ontology.search_one(type = ontology.Bibliography, label = bib_name)
    if(article not in bib.bibliographyContains):
        bib.bibliographyContains.append(article)

    world.save()
    ontology.save()
    return redirect("/browse/"+bib_name)


if __name__ == '__main__':
    app.config['UPLOAD_FOLDER'] = "articles"
    app.run(debug=True)
    world.save()
    ontology.save()