import random
from rounds import *
from cardsInit import * 
from fullParty import *
 
from playerScoresInit import * 
#************************************************************************************************************************
def initjoueurs (n):                         #creer une liste avec n joueur en demandant leurs nom à l'utilisateur
    liste_joueurs=[]
    for i in range(1,n+1):
        print("Joueur ",i,":",end="")
        nom_joueur=input("  Veuillez saisir le nom du joueur:")
        liste_joueurs.append(nom_joueur)
    return liste_joueurs
#***************************************************************************************************************
def init_IA_Al():
    Liste_nom_IA=["Ia_al1","Ia_al2","Ia_al3","Ia_al4","Ia_al5","Ia_al6","Ia_al7"]   # Chaque fonction permet de créer une liste d'Ia de différent nom (Pourquoi 7? Car de base le blackjack se joue jusqu'à 7)
    rep=-1
    while rep<0 or rep>7:
        rep=int(input("Combien voulez-vous rajouter d'IA aleatoire de 0 à 7 ? : "))
    L=[]
    for i in range(0,rep):
        L.append(Liste_nom_IA[i])
    return L
def init_IA_int():
    Liste_nom_IA=["Ia_int1","Ia_int2","Ia_int3","Ia_int4","Ia_int5","Ia_int6","Ia_int7"]
    rep=-1
    while rep<0 or rep>7:
        rep=int(input("Combien voulez-vous rajouter d'IA intelligente de 0 à 7 ? : "))
    L=[]
    for i in range(0,rep):
        L.append(Liste_nom_IA[i])
    return L
def init_IA_200IQ():
    Liste_nom_IA=["Ia_201IQ","Ia_202IQ","Ia_203IQ","Ia_204IQ","Ia_205IQ","Ia_206IQ","Ia_207IQ"]
    rep=-1
    while rep<0 or rep>7:
        rep=int(input("Combien voulez-vous rajouter d'IA 200IQ de 0 à 7 ? : "))
    L=[]
    for i in range(0,rep):
        L.append(Liste_nom_IA[i])
    return L

def init_IA_P():
    Liste_nom_IA=["Ia_P1","Ia_P2","Ia_P3","Ia_P4","Ia_P5","Ia_P6","Ia_P7"]
    rep=-1
    while rep<0 or rep>7:
        rep=int(input("Combien voulez-vous rajouter d'IA parametre de 0 à 7 ? : "))
    L=[]
    for i in range(0,rep):
        L.append(Liste_nom_IA[i])
    return L

def para_Ia(L_P):
    L_para=[]
    for nom in L_P:
        z=-1
        while z<0 or z>1 :
            z= float(input("Entrer le paramètre d'aversion au risque de 0 à 1 (0=prudent,1=téméraire) : "))
            L_para.append(z)
    return L_para

def init_Croupier():
    c=-1
    print("choisissez le caractère du croupier","Parametre: entre 0 et 1","aleatoire: 2","Intelligent: 3","200IQ: 4",sep="\n")
    while c<0 or c>4 :
        c=float(input("carac : "))
        if c>1:
            c=int(c)
    
    D={"Croupier":c,"Scores":0}
    return D
#************************************************************************************************************************
def liste_Tot(liste_des_joueurs,liste_IA_IQ,liste_IA_Int,liste_IA_P,liste_IA_al):                                       # Cette fonction prends la liste de tout les participants Ia et humains afin de faire une liste globale, 
    L=[]
    L.extend(liste_des_joueurs)                                                                                         # utile notamment pour créer les dictionnaires de mises et de scores
    L.extend(liste_IA_IQ)
    L.extend(liste_IA_Int)
    L.extend(liste_IA_P)
    L.extend(liste_IA_al)
    return L
#************************************************************************************************************************
def initscores (liste_joueurs,v=0):         #creer un dictionnaire comptant les scores 
    dictionnaire={}

    for nom in liste_joueurs:
        dictionnaire[nom]=v
    return dictionnaire
#************************************************************************
def gagnant(scores):                        # La fonction reçoit le dictionnaire des scores et cherche le score le plus proche de 21, avant de rajouter tous les joueurs avec ce score dans une liste pour la renvoyer
    max = 2
    P_max = ""
    for key in scores:

        if scores[key] > max and scores[key] <= 21:
            max = scores[key]
            p_max = key
    L =[]
    for key in scores:
        if scores[key] == max:
            L.append(key)
    return L