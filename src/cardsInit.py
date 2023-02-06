import random

from rounds import *
 
from fullParty import *
from stakesAndExtensions import * 
from playerScoresInit import * 

def paquet ():        #creer un paquet de cartes
    paquet_carte = ["as de pique", "as de coeur", "as de trefle", "as de carreau", "deux de pique", "deux de coeur",
                    "deux de trefle", "deux de carreau", "trois de pique", "trois de coeur", "trois de trefle",
                    "trois de carreau", "quatre de pique", "quatre de coeur", "quatre de trefle", "quatre de carreau",
                    "cinq de pique", "cinq de coeur", "cinq de trefle", "cinq de carreau", "six de pique",
                    "six de coeur", "six de trefle", "six de carreau", "sept de pique", "sept de coeur",
                    "sept de trefle", "sept de carreau", "huit de pique", "huit de coeur", "huit de trefle",
                    "huit de carreau", "neuf de pique", "neuf de coeur", "neuf de trefle", "neuf de carreau",
                    "dix de pique", "dix de coeur", "dix de trefle", "dix de carreau", "valet de pique",
                    "valet de coeur", "valet de trefle", "valet de carreau", "dame de pique", "dame de coeur",
                    "dame de trefle", "dame de carreau", "roi de pique", "roi de coeur", "roi de trefle",
                    "roi de carreau"]
    return paquet_carte

#************************************************************************************************************************

def valeurcarte (carte,nom,liste_joueurs,D):
    i=0
    premier_mot=""                                                         #récupérer le premier mot du nom de la carte
                                                                            #et ensuite renvoyer sa valeur numérique
    while i<len(carte) and carte[i] !=" ":
        premier_mot+=carte[i]
        i+=1


    if premier_mot=="as" and nom in liste_joueurs:
        valeur= int(input("Veuillez taper la valeur que vous souhaitez retenir pour l'as:"))
        while valeur!=1 and  valeur!=11:
            valeur = int(input("Mauvaise valeur, saisissez  ** 1 ou 11 **:"))
        return valeur
    elif premier_mot=="as":
        a=21-D[nom]
        if a>=11:
            return 11
        return 1
    elif premier_mot=="deux":
        return 2
    elif premier_mot =="trois":
        return 3
    elif premier_mot =="quatre":
        return 4
    elif premier_mot=="cinq":
        return 5
    elif premier_mot =="six":
        return 6
    elif premier_mot =="sept":
        return 7
    elif premier_mot =="huit":
        return 8
    elif premier_mot =="neuf":
        return 9
    else:
        return 10
#************************************************************************************************************************

def initpioche (L):#n représente le nombre de joueurs de la partie
    n=len(L)
    pioche=[]                 #la variable 'pioche' est une liste qui contient les n paquets de cartes (contient n listes)
    nouvelle_pioche = []
    for i in range(1, n + 1):
        pioche.append(random.sample(paquet(), 52))
    i = 0
    while i < n:
        nouvelle_pioche.extend(pioche[i])           # l'idée c'est d'extraire les cartes de chaque paquet de la pioche

        i += 1                              # Les stocker ensuite dans une nouvelle liste appellée nouvelle_pioche

                                           #on compte mélanger d'abord les cartes de chaque paquet et ensuite le stocker dans la liste
    return nouvelle_pioche
#************************************************************************************************************************
def piochecarte (p,x=1):            #'p' représente la pioche constituée de n paquets
    liste_de_cartes_piochees=[]

    for i in range(1,x+1):
        liste_de_cartes_piochees.append(p[0])
        p.pop(0)

    return liste_de_cartes_piochees