import random

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
#************************************************************************************************************************
def init_Mises (liste_joueurs,v=0):      #creer un dictionnaire comptant le nombre de victoire ou les mises
    dictionnaire={}

    for nom in liste_joueurs:
        dictionnaire[nom]=v
    return dictionnaire
#************************************************************************************************************************
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
#************************************************************************************************************************
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
#************************************************************************************************************************
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

#******************************************************************************
def gagnant_instantane(DICT):                   # fonction pour vérifier si un joueur atteint le score de 21 et renvoyer la liste des joueurs ayant ce score
    GAGNANT = []
    for key in DICT:
        if DICT[key] == 21:
            GAGNANT.append(key)
    return GAGNANT

#************************************************************************************************************************
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
