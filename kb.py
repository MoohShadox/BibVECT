from datetime import date

from owlready2 import *
import os


def get_world_ontology():
    world= World(filename = "bib.sqlite3")
    onto = get_ontology("file:///home/moohshadox/PycharmProjects/BibVEC/bib.owl").load()
    return world, onto

def save(world, onto):
    world.save()
    onto.save()

def rm_if_exists(filename):
    if os.path.exists(filename):
        os.remove(filename)

def init_world_ontology():
    rm_if_exists("bib.sqlite3")
    rm_if_exists("bib.owl")
    world= World(filename = "bib.sqlite3")
    onto = get_ontology("file:///home/moohshadox/PycharmProjects/BibVEC/bib.owl")
    with onto:
        ### Concepts :
        class Bibliography(Thing):
            pass
        class Article(Thing):
            pass
        class Researcher(Thing):
            pass
        class Journal(Thing):
            pass

        ### Roles:
        class bibliographyContains(Bibliography >> Article):
            pass
        class authored(Researcher >> Article):
            pass
        class about(Thing >> Article):
            pass
        class inFile(Article >> str,FunctionalProperty):
            pass
        class publicatedIn(Article >> Journal, FunctionalProperty):
            pass

        class articleID(Article >> str, FunctionalProperty):
            pass
        ### Attributes



        class fullText(Article >> str, FunctionalProperty):
            pass
        class content(Thing >> str,  FunctionalProperty):
            pass
        class doi(Article >> str, FunctionalProperty):
            pass
        class found(Article >> bool,  FunctionalProperty):
            pass

        class bibtexReference(Article >> str, FunctionalProperty):
            pass

        class title(Article >> str, FunctionalProperty):
            pass

        class author(Article >> str, FunctionalProperty):
            pass

        class journal(Article >> str, FunctionalProperty):
            pass

        class publicationYear(Article >> int, FunctionalProperty):
            pass

        class bibliographyDate(Bibliography >> date, FunctionalProperty):
            pass

        class articleReview(Article >> str, FunctionalProperty):
            pass

        class hasDir(Article >> str, FunctionalProperty):
            pass

    world.save()
    onto.save()
    return world, onto

