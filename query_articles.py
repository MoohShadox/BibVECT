import os.path

import requests
import bibtexparser
from bs4 import BeautifulSoup
import requests

def get_doi_id(doi):
   return doi.replace("https://doi.org/","")

def query_bib(doi_clean):
    print("doi clean: ", doi_clean)
    headers = {"User-Agent":"Mozilla/4.0"}
    ans = requests.get(f"https://www.doi2bib.org/2/doi2bib?id={doi_clean}",headers=headers)
    bibtex_str = ans.content.decode("utf8")
    bib_database = bibtexparser.loads(bibtex_str)
    return (bib_database.entries[0], bibtex_str)

def scihub_dl(doi_id, file_name = "out"):
    response= requests.get(f'https://sci-hub.ru/{doi_id}')
    print("Request to: ", f'https://sci-hub.ru/{doi_id}')
    soup = BeautifulSoup(response.text, 'html.parser')
    print(soup)
    href = soup.findAll("button")[0]["onclick"].replace("location.href=", "").replace("'","").replace("?download=true","")
    pdf_req = requests.get(href)
    file_name = file_name + ".pdf" if ".pdf" not in file_name else file_name
    f = open(file_name, "wb")
    f.write(pdf_req.content)

def download_article(doi_id, dir = ""):
    doi_id = get_doi_id(doi_id)
    bib, bib_str = query_bib(doi_id)
    title = bib["title"]
    name = title.title().replace(" ","") + ".pdf"
    scihub_dl(doi_id,os.path.join(dir,name))
    return bib,bib_str, os.path.join(dir,name)

doi = "https://doi.org/10.1016/j.jflm.2013.11.003"
