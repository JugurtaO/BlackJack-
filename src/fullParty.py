import random
from rounds import *
from cardsInit import *
from stakesAndExtensions import * 
from playerScoresInit import *
############################################################################################################## 
def gagnant_instantane(DICT):                   # fonction pour vérifier si un joueur atteint le score de 21 et renvoyer la liste des joueurs ayant ce score
    GAGNANT = []
    for key in DICT:
        if DICT[key] == 21:
            GAGNANT.append(key)
    return GAGNANT

#************************************************************************************************************************
#***********************************************************************
def liste_Tot(liste_des_joueurs,liste_IA_IQ,liste_IA_Int,liste_IA_P,liste_IA_al):                                       # Cette fonction prends la liste de tout les participants Ia et humains afin de faire une liste globale, 
    L=[]
    L.extend(liste_des_joueurs)                                                                                         # utile notamment pour créer les dictionnaires de mises et de scores
    L.extend(liste_IA_IQ)
    L.extend(liste_IA_Int)
    L.extend(liste_IA_P)
    L.extend(liste_IA_al)
    return L
#************************************************************************************************************************
def quitter(liste_des_joueurs, Mises,list_Tot):                 #Fonction demandant au joueurs humain si ils veulent continuer à faire des parties et adapte les listes en fonction de leur réponse
    L=[]
    for i in liste_des_joueurs:
        print(i, ":", end="")
        rep = input("Voulez-vous rejouer une nouvelle partie?  oui /non  :")
        while rep != "oui" and rep != "non":
            rep = input("Pour rejouer une nouvelle partie, tapez 'oui' sinon tapez 'non' :")
        if rep == 'non':
            L.append(i)
            del Mises[i]
    for e in L:
        liste_des_joueurs.remove(e)
        list_Tot.remove(e)

#************************************************************************************************************************


#************************************************************************************************************************
# B2
def tourcomplet(tour, liste_des_joueurs, p, DICTIONNAIRE,liste_IA_IQ,liste_IA_Int,liste_IA_P,liste_IA_al,liste_para_IA,liste_Tot,Croupier,Lose):  # pour éviter de modifier les listes des participants encore en jeu pendant les boucles while 
    i = 0                                                                                               #on crée des listes contenant les joueurs à retirer du jeu, et à la fin de la fonction, on les enlève des listes des participants encore en jeu
    j=0 
    GG=False
    liste_retire = []
    liste_retire_IA_IQ = []
    liste_retire_IA_Int = []
    liste_retire_IA_P = []
    liste_retire_IA_al = []
    while j<len(liste_des_joueurs)and GG==False:
        tourjoueur(liste_des_joueurs[j], tour, liste_des_joueurs, p, DICTIONNAIRE, liste_retire,liste_gagnant)
        if len(liste_gagnant)!=0 :
            GG=True
        j+=1
    j=0
    while j<len(liste_IA_IQ)and GG==False:
        tourIA_200IQ(liste_IA_IQ[j], tour, liste_des_joueurs, p, DICTIONNAIRE, liste_retire_IA_IQ,liste_gagnant)
        if len(liste_gagnant)!=0 :
            GG=True
        j+=1
    j=0
    while j<len(liste_IA_Int)and GG==False:
        tourIA_int(liste_IA_Int[j], tour, liste_des_joueurs, p, DICTIONNAIRE, liste_retire_IA_Int,liste_gagnant)
        if len(liste_gagnant)!=0 :
            GG=True
        j+=1
    j=0
    while j<len(liste_IA_P)and GG==False:
        z= liste_para_IA[j]
        tourIA_p(liste_IA_P[j], tour, liste_des_joueurs, p, DICTIONNAIRE, liste_retire_IA_P,liste_gagnant,z)
        if len(liste_gagnant)!=0 :
            GG=True
        j+=1
    j=0
    while j<len(liste_IA_al)and GG==False:
        tourIA_alea(liste_IA_al[j], tour, liste_des_joueurs, p, DICTIONNAIRE, liste_retire_IA_al,liste_gagnant)
        if len(liste_gagnant)!=0 :
            GG=True
        j+=1
    if Croupier["Croupier"]<=1 and Lose!="stop":
        z=Croupier["Croupier"]
        Lose=tourCR_p(tour, p,Croupier,liste_gagnant,z,liste_des_joueurs)
    elif Croupier["Croupier"]==2 and Lose!="stop":
        Lose=tourCR_alea(tour, p,Croupier,liste_gagnant,liste_des_joueurs)
    elif Croupier["Croupier"]==3 and Lose!="stop":
        Lose=tourCR_int(tour, p,Croupier,liste_gagnant,liste_des_joueurs)
    elif Croupier["Croupier"]==4 and Lose!="stop":
        Lose=tourCR_200IQ(tour, p,Croupier,liste_gagnant,liste_des_joueurs)

    while i < len(liste_retire):
        b = liste_retire[i]
        liste_des_joueurs.remove(b)
        i += 1
    i=0
    while i < len(liste_retire_IA_IQ):
        b = liste_retire_IA_IQ[i]
        liste_IA_IQ.remove(b)
        i += 1
    i=0
    while i < len(liste_retire_IA_Int):
        b = liste_retire_IA_Int[i]
        liste_IA_Int.remove(b)
        i += 1
    i=0
    for nom in liste_retire_IA_P:
        i=0
        while liste_IA_P[i]!=nom:
            i+=1
        c= liste_para_IA[i]
        liste_IA_P.remove(nom)
        liste_para_IA.remove(c)
        i += 1
    i=0
    for nom in liste_retire_IA_al:
        liste_IA_al.remove(nom)
    return Lose
#************************************************************************************************************************
def partiefinie(liste_des_joueurs,liste_IA_IQ,liste_IA_Int,liste_IA_P,liste_IA_al):
    if len(liste_des_joueurs) == 0 and len(liste_IA_IQ) == 0 and len(liste_IA_Int) == 0 and len(liste_IA_P) == 0 and len(liste_IA_al) == 0:
        return True
    return False     #Fonction qui renvoie le Boléen vérifiant si il y a encore des participants en jeu

#************************************************************************************************************************
def partiecomplete(liste_des_joueurs, p, liste_gagnant, DICTIONNAIRE,Mises,liste_IA_IQ,liste_IA_Int,liste_IA_P,liste_IA_al,liste_para_IA,liste_Tot,Croupier,Casino):
    tour = 1
    Mises_en_jeu=init_Mises(liste_Tot)
    DICTIONNAIRE = premiertour(liste_Tot,liste_des_joueurs)
    prem_Tour_Cr(Croupier,liste_des_joueurs,p)
    pose_Mises(DICTIONNAIRE, Mises, liste_des_joueurs, Mises_en_jeu)
    pose_Mises_IA_al(DICTIONNAIRE, Mises, liste_IA_al, Mises_en_jeu)
    pose_Mises_IA_P(DICTIONNAIRE, Mises,liste_IA_P,Mises_en_jeu,liste_para_IA)  #Dans cette fonction, on fait jouer le premier tour au participant qui renvoie le dictionnaire des scores,puis le premier tour du croupier
    pose_Mises_IA_Int(DICTIONNAIRE, Mises, liste_IA_Int, Mises_en_jeu)          #puis chaque types d'Ia mise selon son comportement, on récupère chaque mise individuelement via le dictionnaire Mises_en_jeu, et Casino récupère le total de ces mises
    pose_Mises_IA_200IQ(DICTIONNAIRE, Mises, liste_IA_IQ,Mises_en_jeu)
    Casino=recupMise(Mises_en_jeu,Casino)
    gagnant_inst = gagnant_instantane(DICTIONNAIRE)                             #on test s'il y a un gagnant dès la distribution des cartes
    Lose=False                                                                  #Lose représente le statut du croupier (True= en jeu, False=éliminé, 'stop'=arrête de jouer)
    if len(gagnant_inst) != 0:
        print("le(s) gagnant(s)est(sont) : ",gagnant_inst,"par victoire instantané")
        for nom in gagnant_inst:
            Mises[nom] += 2*Mises_en_jeu[nom]
            Casino-= 2*Mises_en_jeu[nom]
    else:                                                                       #tant qu'il ya des joueurs pour jouer,qu'il ny a pas de gagnant,,et que le croupier n'a pas perdu alors on continue de jouer
        while partiefinie(liste_des_joueurs,liste_IA_IQ,liste_IA_Int,liste_IA_P,liste_IA_al) == False and len(liste_gagnant) == 0 and Lose!=True:
            Lose=tourcomplet(tour, liste_des_joueurs, p, DICTIONNAIRE,liste_IA_IQ,liste_IA_Int,liste_IA_P,liste_IA_al,liste_para_IA,liste_Tot,Croupier,Lose)
            tour += 1
        if Lose ==True:                                                   #si le croupier dépasse 21 tout le monde gagne 2 fois sa mise
            for key in Mises:
                Mises[key]+=2*Mises_en_jeu[key]
                Casino-= 2*Mises_en_jeu[key]
        elif len(liste_gagnant) != 0 :                                        #si il ya eu un score de 21 alors si le croupier n'a pas gagné les vainqueurs gagne 2 fois leur mise sinon ils reprennent leur mises
            print("le(s) gagnant(s)est(sont) : ",liste_gagnant)
            if "Croupier" not in liste_gagnant:
                for nom in liste_gagnant:
                    Mises[nom] += 2*Mises_en_jeu[nom]
                    Casino-= 2*Mises_en_jeu[nom]
            else:
                liste_gagnant.remove("Croupier")
                for nom in liste_gagnant:
                    Mises[nom] += Mises_en_jeu[nom]
                    Casino-= Mises_en_jeu[nom]
        
        else:                                             #si personne n'a un score de 21 tous ceux qui on  le score le plus proche de 21 gagnent sauf si le croupier possède un meilleur score,si le score est égal alors les gagnants de liste récupèrent leur mises
            LISTE = gagnant(DICTIONNAIRE)
            print("le(s) gagnant(s)est(sont) : ",LISTE)
            for nom in LISTE :
                if DICTIONNAIRE[nom]> Croupier["Scores"]:
                   Mises[nom] += 2*Mises_en_jeu[nom]
                   Casino-= 2*Mises_en_jeu[nom]
                elif DICTIONNAIRE[nom]== Croupier["Scores"]:
                    Mises[nom] += Mises_en_jeu[nom]
                    Casino-= Mises_en_jeu[nom]
                else:
                    print("Croupier est plus proche de 21 que ",nom)
    return Casino
