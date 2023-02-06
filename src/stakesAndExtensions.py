import random
from rounds import *
from cardsInit import * 
from fullParty import *
from playerScoresInit import * 

def init_Mises (liste_joueurs,v=0):      #creer un dictionnaire comptant le nombre de victoire ou les mises
    dictionnaire={}

    for nom in liste_joueurs:
        dictionnaire[nom]=v
    return dictionnaire

# B4 les Mises
def verif_Mises(Mises, liste_des_joueurs,liste_IA_IQ,liste_IA_Int,liste_IA_P,liste_IA_al,liste_Tot):          #Fonction retirant du jeu tous les participants n'ayant plus de kopeck (des dictionnaires,des listes IA/joueurs,et de la liste tot)
    L_retire=[]
    for key in Mises:
        if Mises[key]<= 0 :
            L_retire.append(key)
    for nom in L_retire:
            del Mises[nom]
            if nom in liste_des_joueurs:
                liste_des_joueurs.remove(nom)
            elif nom in liste_IA_IQ:
                liste_IA_IQ.remove(nom)
            elif nom in liste_IA_Int:
                liste_IA_Int.remove(nom)
            elif nom in liste_IA_P:
                indice=0
                while liste_IA_P[indice]!=nom:
                    indice+=1
                liste_IA_P.remove(nom)
                liste_para_IA.pop(indice)
            elif nom in liste_IA_al:
                liste_IA_al.remove(nom)
            
            liste_Tot.remove(nom)
    print(Mises)
#*************************************************
def pose_Mises(DICTIONNAIRE, Mises, liste_des_joueurs, Mises_en_jeu):       #Fonction demandant aux joueurs humains combien ils veulent miser et adapte les dictionnaires en fonction de leurs réponses
    for i in liste_des_joueurs:
        mise = -1
        print(i, "Votre score est : ", DICTIONNAIRE[i])
        while mise < 1 or mise > Mises[i]:
            mise = int(input("Combien misez-vous?"))
        Mises[i] = Mises[i] - mise
        Mises_en_jeu[i]= mise
        print(i, "pari : ",mise)
#*****************************************************************************************************************        
def pose_Mises_IA_al(DICTIONNAIRE, Mises, liste_IA_al, Mises_en_jeu):       #Fonction qui fait miser un pourcentage de 0 à 100% de leurs kopeck aux Ia dans la liste
    z=random.randint(0,10)/10
    for i in liste_IA_al:
        print(i, "Votre score est : ", DICTIONNAIRE[i])
        mise =Mises[i]*z
        mise= int(mise)
        if mise< 1:
            mise=1
        Mises[i] = Mises[i] - mise
        Mises_en_jeu[i]= mise
        print(i, "pari : ",mise)
#*****************************************************************************************************************      
def pose_Mises_IA_P(DICTIONNAIRE, Mises,liste_IA_P,Mises_en_jeu,liste_para_IA): #Fonction qui fait miser un pourcentage des kopecks de l'Ia en fonction de son paramètre associés,(L'ia d'indice 1 possède le paramètre d'indice 1)  
    for i in range(len(liste_IA_P)):
        print(liste_IA_P[i], "Votre score est : ", DICTIONNAIRE[liste_IA_P[i]])
        z=liste_para_IA[i]
        mise =Mises[liste_IA_P[i]]*z
        mise= int(mise)
        if mise< 1:
            mise=1
        Mises[liste_IA_P[i]] = Mises[liste_IA_P[i]] - mise
        Mises_en_jeu[liste_IA_P[i]]= mise
        print(liste_IA_P, "pari : ",mise)
#*****************************************************************************************************************
def pose_Mises_IA_Int(DICTIONNAIRE, Mises, liste_IA_Int, Mises_en_jeu):   #Fonction qui fait miser un pourcentage des kopecks de l'Ia en fonction de la proximité de son score avec 21

    for i in liste_IA_Int:
        print(i, "Votre score est : ", DICTIONNAIRE[i])
        z = (DICTIONNAIRE[i] / 21)
        mise =Mises[i]*z
        mise= int(mise)
        if mise< 1:
            mise=1
        Mises[i] = Mises[i] - mise
        Mises_en_jeu[i]= mise
        print(i, "pari : ",mise)
#*****************************************************************************************************************       
def pose_Mises_IA_200IQ(DICTIONNAIRE, Mises, liste_IA_IQ,Mises_en_jeu):  #Fonction qui fait miser un pourcentage des kopecks de l'Ia en fonction de la proximité des scores adverses avec 21 
    for i in range(len(liste_IA_IQ)):                                    #(la somme de leur scores sur 21 fois le nombre d'adversaires)
        print(liste_IA_IQ[i], "Votre score est : ", DICTIONNAIRE[liste_IA_IQ[i]])
        q=0
        f=0
        cpt=0
        for e in DICTIONNAIRE:
            if e!= liste_IA_IQ[i]:
                cpt+= DICTIONNAIRE[e]
                if DICTIONNAIRE[e]==21:
                    f+=1
                q+=1
        if f<1:
            z=1-cpt/(q*21)
        else:
            z=0
        mise = Mises[liste_IA_IQ[i]] * z
        mise= int(mise)
        if mise < 1:
            mise = 1
        Mises[liste_IA_IQ[i]] = Mises[liste_IA_IQ[i]] - mise
        Mises_en_jeu[liste_IA_IQ[i]]= mise
        print(liste_IA_IQ[i], "pari : ",mise)
#***************************************************************************************************************** 
def recupMise(Mises_en_jeu,Casino):                             #Fonction qui ajoute la mise de chaque joueur au capital du casino
    for key in Mises_en_jeu:
        Casino+=Mises_en_jeu[key]
    return Casino