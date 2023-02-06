import random
from rounds import *
from cardsInit import * 
from fullParty import *
from stakesAndExtensions import * 
from playerScoresInit import * 

#************************************************************************************************************************
n = int(input("Veuillez saisir le nombre de joueurs:"))     # les listes en majuscules sont des sauvegardes des listes au début de chaque partie afin de les restaurer à la fin de la partie(pour les modifier en fonction des éliminations)
paquet_carte = paquet()
liste_des_joueurs = initjoueurs(n)
liste_IA_IQ = init_IA_200IQ()
liste_IA_Int = init_IA_int()
liste_IA_P = init_IA_P()
liste_para_IA = para_Ia(liste_IA_P)
liste_IA_al = init_IA_Al()
liste_Tot = liste_Tot(liste_des_joueurs,liste_IA_IQ,liste_IA_Int,liste_IA_P,liste_IA_al)
Croupier=init_Croupier()
Mises = init_Mises(liste_Tot, 100)
Casino= 0
rep = "oui"
while rep == "oui":
  
    verif_Mises(Mises, liste_des_joueurs,liste_IA_IQ,liste_IA_Int,liste_IA_P,liste_IA_al,liste_Tot)
    LISTE_DES_JOUEURS = list(liste_des_joueurs)
    LISTE_IA_IQ = list(liste_IA_IQ)
    LISTE_IA_INT = list(liste_IA_Int)
    LISTE_IA_P = list(liste_IA_P)
    LISTE_PARA_IA =list(liste_para_IA)
    LISTE_IA_AL = list(liste_IA_al)
    liste_gagnant = []
    pioche = initpioche(liste_Tot)
    DICTIONNAIRE = initscores(liste_Tot)
    Casino=partiecomplete(liste_des_joueurs, pioche, liste_gagnant, DICTIONNAIRE,Mises,liste_IA_IQ,liste_IA_Int,liste_IA_P,liste_IA_al,liste_para_IA,liste_Tot,Croupier,Casino)
    quitter(LISTE_DES_JOUEURS, Mises,liste_Tot)
    liste_des_joueurs = list(LISTE_DES_JOUEURS)
    liste_IA_IQ = list(LISTE_IA_IQ)
    liste_IA_Int = list(LISTE_IA_INT)
    liste_IA_P = list(LISTE_IA_P)
    liste_para_IA = list(LISTE_PARA_IA)
    liste_IA_al = list(LISTE_IA_AL)
    if len(LISTE_DES_JOUEURS) < 1:
        rep = input("Voulez-vous refaire une partie avec uniquement des IA ? oui/non : ")

