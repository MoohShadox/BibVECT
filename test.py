import requests
import bibtexparser
import random

def lancer_de6() -> float:
    """ Précondition : Rien
        Renvoie à chaque appel une valeur entière comprise entre 1 et 6 """
    if 0 <= random.random() <= 1 / 6:
        return 1
    elif 1 / 6 < random.random() <= 2 / 6:
        return 2
    elif 2 / 6 < random.random() <= 3 / 6:
        return 3
    elif 3 / 6 < random.random() <= 4 / 6:
        return 4
    elif 4 / 6 < random.random() <= 5 / 6:
        return 5
    else:
        return 6



import numpy as np

def lancer():
    print(random.random()*10)
    a = int(10*random.random()) % 6 + 1
    return a

def fibonacci(n:int)->int:
    """n est strictement positif"""
    if n==0:
        return 0
    elif n==1:
        return 1
    i:int=2
    r:int=0
    temp:int=1 #variable temporaire
    temp2:int=0 #variable temporaire 2
    while i<=n:
        r=temp2+temp
        temp2=temp
        temp=r
        i=i+1
    return r


def chiffre(s: str) -> int:
    """Pré : Rien
           Retourne l'entier qui correspond au caractère donné. """
    return ord(s) - ord('0')


assert chiffre('5') == 5
assert chiffre('8') == 8


def entier(s:str)->int:
    """ retourne l’entier représenté par la chaîne s. """
    i:str
    res:int=0
    for i in s:
        res=res*10+((ord(i))-ord("0"))
    return res

print(entier("12"))
print(entier("012"))
print(entier("05612"))
