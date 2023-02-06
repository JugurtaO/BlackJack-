import random
from cardsInit import * 
from fullParty import *
from stakesAndExtensions import * 
from playerScoresInit import * 

def premiertour (liste_Tot,liste_joueurs):                           # Fais piocher deux cartes pour chaque joueurs dans la liste donné et renvoie un dictionnaire avec les scores de chaque joueurs après le premier tour
    DICTIONNAIRE=initscores (liste_Tot)
    p=initpioche(liste_Tot)

    for nom in liste_Tot:
        val=0
        liste_de_cartes= piochecarte(p,2)

        for j in range (0,2):
            val+=valeurcarte(liste_de_cartes[j],nom,liste_joueurs,DICTIONNAIRE)
        DICTIONNAIRE[nom]=val
    return DICTIONNAIRE
#************************************************************************
def prem_Tour_Cr(Croupier,liste_joueurs,p):                # le croupier étant considéré comme un joueur à part(il est contenu dans un dictionnaire), on lui fait piocher deux cartes et on modifie la valeur de la clé "Scores" 
        val=0
        liste_de_cartes= piochecarte(p,2)

        for j in range (0,2):
            val+=valeurcarte(liste_de_cartes[j],"Scores",liste_joueurs,Croupier)
        Croupier["Scores"]=val

def continuee():                                                                      #fonction qui demande à l'utilisateur si il souhaite continuer la partie,avant de renvoyer un Boléen
    reponse = input("Voulez-vous continuer la partie?  oui,go/non,stop :")                                         
    while reponse != "oui" and reponse != "go" and reponse != "non" and reponse != "stop":
        reponse = input("TAPEZ  oui,go OU  non,stop :")
    if reponse == "oui" or reponse == "go":
        return True
    return False
#************************************************************************************************************************

def tourjoueur(nom_joueur, tour, liste_joueurs, p, DICTIONNAIRE, liste_retire,liste_gagnant):           #Affiche le numéro du tour,le nom du joueur, et son score, avant de jouer la fonction continue et faire piocher une carte ou non selon la réponse
    print("Tour n°:", tour)                                                                             # Si l'utilisateur dépasse 21 ou répond non, il est enlevé de la liste des joueurs(en cours de jeu)
    print("Joueur:", nom_joueur) 
    print("Score:", DICTIONNAIRE[nom_joueur])
    CONTINUE = continuee()
    if CONTINUE == True:
        carte = piochecarte(p)
        DICTIONNAIRE[nom_joueur] += valeurcarte(carte[0],nom_joueur,liste_joueurs,DICTIONNAIRE)
        if DICTIONNAIRE[nom_joueur] > 21:
            liste_retire.append(nom_joueur)
        if DICTIONNAIRE[nom_joueur] == 21:
            liste_gagnant.append(nom_joueur)
    if CONTINUE == False:
        liste_retire.append(nom_joueur)
#************************************************************************************************************************
def tourIA_alea(nom_IA, tour,liste_joueurs, p, DICTIONNAIRE, liste_retire_IA_al,liste_gagnant):                # Même fonction que tourjoueur mais remplace la fonction continuee() par une réponse aléatoire (0 ou 1)
    
    print("Tour n°:", tour)
    print("Joueur:", nom_IA)
    print("Score:", DICTIONNAIRE[nom_IA])
    CONTINUE = random.randint(0,1)
    if CONTINUE == 1:
        print(nom_IA,"continue de jouer")
        carte = piochecarte(p)
        DICTIONNAIRE[nom_IA] += valeurcarte(carte[0],nom_IA,liste_joueurs, DICTIONNAIRE)
        if DICTIONNAIRE[nom_IA] > 21:
            liste_retire_IA_al.append(nom_IA)
        if DICTIONNAIRE[nom_IA] == 21:
            liste_gagnant.append(nom_IA)
    elif CONTINUE ==0 :
        print(nom_IA,"arrete de jouer")
        liste_retire_IA_al.append(nom_IA)
#************************************************************************************************************************


def tourIA_p(nom_IA, tour,liste_joueurs, p, DICTIONNAIRE, liste_retire_IA_P,liste_gagnant,z):    # Même fonction que tourIA_alea mais la fonction aleatoire pioche entre 1 et m, m déterminé par le paramètre z qui est le pourcentage de chance de continuer

    print("Tour n°:", tour)
    print("Joueur:", nom_IA)
    print("Score:", DICTIONNAIRE[nom_IA])
    if z==0:
        CONTINUE = 1
        m=1
    else:
        m=(1/z)+1
        m=int(m)
        CONTINUE=random.randint(0,m)
    c=(m+1)*z
    if CONTINUE <=c:
        print(nom_IA,"continue de jouer")
        carte = piochecarte(p)
        DICTIONNAIRE[nom_IA] += valeurcarte(carte[0],nom_IA,liste_joueurs,DICTIONNAIRE)
        if DICTIONNAIRE[nom_IA] > 21:
            liste_retire_IA_P.append(nom_IA)
        if DICTIONNAIRE[nom_IA] == 21:
            liste_gagnant.append(nom_IA)
    if CONTINUE >c:
        print(nom_IA,"arrete de jouer")
        liste_retire_IA_P.append(nom_IA)
#************************************************************************************************************************

def tourIA_int(nom_IA, tour, liste_joueurs, p, DICTIONNAIRE, liste_retire_IA_Int,liste_gagnant): # Même fonction que tourIA_p, mais z est automatiquement déterminé par le scores de l'IA ( plus le score est proche de 21 moins il a de chance de piocher)
    print("Tour n°:", tour)
    print("Joueur:", nom_IA)
    print("Score:", DICTIONNAIRE[nom_IA])
    z=1-(DICTIONNAIRE[nom_IA]/21)
    if z<=0:
        CONTINUE = 1
        m=1
    else:
        m=(1/z)+1
        m=int(m)
        CONTINUE=random.randint(0,m)
    c=(m+1)*z
    c=int(c)
    if CONTINUE <=c:
        print(nom_IA,"continue de jouer")
        carte=piochecarte(p)
        DICTIONNAIRE[nom_IA] += valeurcarte(carte[0],nom_IA,liste_joueurs,DICTIONNAIRE)
        if DICTIONNAIRE[nom_IA] > 21:
            liste_retire_IA_Int.append(nom_IA)
        if DICTIONNAIRE[nom_IA] == 21:
            liste_gagnant.append(nom_IA)
    else:
        print(nom_IA,"arrete de jouer")
        liste_retire_IA_Int.append(nom_IA)
#************************************************************************************************************************

def tourIA_200IQ(nom_IA, tour,liste_joueurs, p, DICTIONNAIRE, liste_retire_IA_IQ,liste_gagnant):   # Même fonction que tourIA_p, mais cette fois l'Ia compte (cpt) le nombre de carte dans le paquet inférieur à la différence entre son score et 21
    print("Tour n°:", tour)                                                                        # puis l'Ia fait le ratio entre le nombre cpt et le nombre de carte dans le paquet
    print("Joueur:", nom_IA)
    print("Score:", DICTIONNAIRE[nom_IA])
    cpt=0
    a=21-DICTIONNAIRE[nom_IA]
    for e in p:
        if valeurcarte(e,nom_IA,liste_joueurs,DICTIONNAIRE)<=a:
            cpt+=1
    z = cpt/len(p)
    if z == 0:
        CONTINUE = 1
        m = 1
    else:
        m = (1 / z) + 1
        m=int(m)
        CONTINUE = random.randint(0, m)
    c = (m + 1) * z
    if CONTINUE <= c:
        print(nom_IA,"continue de jouer")
        carte = piochecarte(p)
        DICTIONNAIRE[nom_IA] += valeurcarte(carte[0],nom_IA,liste_joueurs,DICTIONNAIRE)
        if DICTIONNAIRE[nom_IA] > 21:
            liste_retire_IA_IQ.append(nom_IA)
        if DICTIONNAIRE[nom_IA] == 21:
            liste_gagnant.append(nom_IA)
    if CONTINUE > c:
        print(nom_IA,"arrete de jouer")
        liste_retire_IA_IQ.append(nom_IA)
        
#************************************************************************************************************************
def tourCR_p(tour, p,Croupier,liste_gagnant,z,liste_des_joueurs):                               # Même fonction que pour les Ias mais adapté au Croupier
    Lose=False
    print("Tour n°:", tour)
    print("Joueur: ","Croupier")
    print("Score:", Croupier["Scores"])
    if z==0:
        CONTINUE = 1
        m=1
    else:
        m=(1/z)+1
        m=int(m)
        CONTINUE=random.randint(0,m)
    c=(m+1)*z
    if CONTINUE <=c:
        print("Croupier","continue de jouer")
        carte = piochecarte(p)
        Croupier["Scores"]+= valeurcarte(carte[0],"Scores",liste_des_joueurs,Croupier)
        if Croupier["Scores"] > 21:
            Lose=True
        if Croupier["Scores"] == 21:
            liste_gagnant.append("Croupier")
    if CONTINUE >c:
        print("Croupier ","arrete de jouer")
        Lose="stop"
    return Lose

def tourCR_alea(tour, p,Croupier,liste_gagnant,liste_des_joueurs):
    Lose=False
    print("Tour n°:", tour)
    print("Joueur: ","Croupier")
    print("Score:", Croupier["Scores"])
    CONTINUE = random.randint(0,1)
    if CONTINUE == 1:
        print("Croupier","continue de jouer")
        carte = piochecarte(p)
        Croupier["Scores"]+= valeurcarte(carte[0],"Scores",liste_des_joueurs,Croupier)
        if Croupier["Scores"] > 21:
            Lose=True
        if Croupier["Scores"] == 21:
            liste_gagnant.append("Croupier")
    elif CONTINUE ==0:
        print("Croupier ","arrete de jouer")
        Lose="stop"
    return Lose

def tourCR_int(tour, p,Croupier,liste_gagnant,liste_des_joueurs):
    Lose=False
    print("Tour n°:", tour)
    print("Joueur: ","Croupier")
    print("Score:", Croupier["Scores"])
    z=1-(Croupier["Scores"]/21)
    if z<=0:
        CONTINUE = 1
        m=1
    else:
        m=(1/z)+1
        m=int(m)
        CONTINUE=random.randint(0,m)
    c=(m+1)*z
    c=int(c)
    if CONTINUE <=c:
        print("Croupier","continue de jouer")
        carte = piochecarte(p)
        Croupier["Scores"]+= valeurcarte(carte[0],"Scores",liste_des_joueurs,Croupier)
        if Croupier["Scores"] > 21:
            Lose=True
        if Croupier["Scores"] == 21:
            liste_gagnant.append("Croupier")
    if CONTINUE >c:
        print("Croupier ","arrete de jouer")
        Lose="stop"
    return Lose

def tourCR_200IQ(tour, p,Croupier,liste_gagnant,liste_des_joueurs):
    Lose=False
    print("Tour n°:", tour)
    print("Joueur: ","Croupier")
    print("Score:", Croupier["Scores"])
    z=1-(Croupier["Scores"]/21)
    cpt=0
    a=21-Croupier["Scores"]
    for e in p:
        if valeurcarte(e,"Scores",liste_des_joueurs,Croupier)<=a:
            cpt+=1
    z = cpt/len(p)
    if z == 0:
        CONTINUE = 1
        m = 1
    else:
        m = (1 / z) + 1
        m=int(m)
        CONTINUE = random.randint(0, m)
    c = (m + 1) * z
    if CONTINUE <=c:
        print("Croupier","continue de jouer")
        carte = piochecarte(p)
        Croupier["Scores"]+= valeurcarte(carte[0],"Scores",liste_des_joueursCroupier)
        if Croupier["Scores"] > 21:
            Lose=True
        if Croupier["Scores"] == 21:
            liste_gagnant.append("Croupier")
    if CONTINUE >c:
        print("Croupier ","arrete de jouer")
        Lose="stop"
    return Lose

