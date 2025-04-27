TAILLE_GRILLE = 9
PION_BLANC = "●"
PION_NOIR = "○"

def error(texte,type):
    if type == 0:
        print("\033[31m==>\033[0m "+ texte)
        print("")

def donner_pion(couleur):
    if couleur == 1:
        return PION_BLANC
    else:
        return PION_NOIR

def obtenir_numero_pion(pion):
    if pion == PION_BLANC:
        return 1
    else:
        return 0

def donner_grille():
    grille = [
        [" "," "," "," "," "," "," "," "," "],
        [" "," "," "," "," "," "," "," "," "],
        [" "," "," "," "," "," "," "," "," "],
        [" "," "," "," "," "," "," "," "," "],
        [" "," "," "," "," "," "," "," "," "],
        [" "," "," "," "," "," "," "," "," "],
        [" "," "," "," "," "," "," "," "," "],
        [" "," "," "," "," "," "," "," "," "],
        [" "," "," "," "," "," "," "," "," "],
    ]
    return grille

def convertir_en_tuple(coord):
    lettre = coord[0].upper()
    chiffre = int(coord[1])
    lettre_num = ord(lettre) - ord('A')
    return (lettre_num, chiffre - 1)

def obtenir_pion(coord,grille):
    x, y = coord
    return grille[x][y]



# Retirer permet a l'user de la fonction si l'ancienne postions doit etre retirer
def bouger_pion(coord_avant,coord_apres,grille,retirer):
    contenu = obtenir_pion(coord_avant,grille)
    mettre_char_coord(grille, coord_apres, contenu)
    if retirer == "oui":
        mettre_char_coord(grille, coord_avant, " ")
    return 0

def faire_mouvement(coord_avant, coord_apres, grille,type):
    def verifier_coordonnee(direction,vecteur,distance):
        if (not vecteur[0] and not vecteur[1]): # Meme coordonnées
            return 1
        if (vecteur[0] != 0 and vecteur[1] != 0): # Deplacement non orthogonaux
            if (vecteur[0] != vecteur[1]): # Deplacement non diagonale
                return 1
        if(vecteur[0] == vecteur[1] and abs(vecteur[1])>=2): # Deplacement diagonal
            direction[0] = vecteur[0] // abs(vecteur[0])
            direction[1] = vecteur[1] // abs(vecteur[1])
        elif (abs(vecteur[1])>=distance): # Deplacement vertical
           direction[0] = 0
           direction[1] = vecteur[1] // abs(vecteur[1])
        elif (abs(vecteur[0])>=distance): # Deplacement horizontal
            direction[0] = vecteur[0] // abs(vecteur[0])
            direction[1] = 0
        else:
            return 1
        return 0

    def check_case_vide(pos,direction,condition):
        while pos[0] != coord_apres[0]+condition[0] or pos[1] != coord_apres[1]+condition[1]:
            if (obtenir_pion(pos,grille) != " "):
                return 1
            pos[0] -= direction[0]
            pos[1] -= direction[1]
        return 0

    def elimination(coord_avant, coord_apres, grille):
        """ La case d’arrivé doit être occupé par un pion adverse.
        - Que les cases entre votre pion(départ) et le pion ennemi(arrivé) soit vide.
        - Que entre votre pion et le pion de votre adversaires il y est au moins une case vide qui les
        séparent."""
        direction = [0, 0]
        vecteur = (coord_avant[0] - coord_apres[0], coord_avant[1] - coord_apres[1])

        result = verifier_coordonnee(direction,vecteur,2)
        if result != 0:
            return 1

        pos = [coord_avant[0] - direction[0], coord_avant[1] - direction[1]]
        result = check_case_vide(pos,direction,(0,0))
        if result != 0:
            return 1

        mettre_char_coord(grille,coord_apres,obtenir_pion(coord_avant,grille))
        mettre_char_coord(grille,coord_avant," ")
        return 0

    def retournement(coord_avant, coord_apres,grille):
        direction = [0, 0]
        vecteur = (coord_avant[0] - coord_apres[0], coord_avant[1] - coord_apres[1])

        result = verifier_coordonnee(direction,vecteur,3)
        if result != 0:
            return 1

        pos = [coord_avant[0] - direction[0], coord_avant[1] - direction[1]]
        result = check_case_vide(pos,direction,direction)
        if result != 0:
            return 1

        if (obtenir_pion((coord_apres[0]+direction[0],coord_apres[1]+direction[1]),grille) == " "):
            return 1
        if (obtenir_pion(coord_apres,grille) != " "):
            return 1


        mettre_char_coord(grille,coord_apres,obtenir_pion(coord_avant,grille))
        mettre_char_coord(grille,coord_avant," ")
        return 0

    result = 1
    if (type == "elimination"):
        result = elimination(coord_avant, coord_apres, grille)
    elif (type == "retournement"):
        result = retournement(coord_avant, coord_apres, grille)

    return result

def mettre_char_coord(grille,coord,char):
    grille[coord[0]][coord[1]]=char

def initialise(grille, periode):
    blanc = donner_pion(1)
    noir = donner_pion(0)
    def remplir_depuis_liste(grille, liste, symbole_1, symbole_2):
        for i in range(TAILLE_GRILLE):
            for j in range(TAILLE_GRILLE):
                val = liste[(i-1) * TAILLE_GRILLE + j]
                if val == 3:
                    mettre_char_coord(grille, (i,j), symbole_1)
                elif val == 2 or val == 3:
                    mettre_char_coord(grille,  (i,j), symbole_2)

    def initialise_debut(grille):
        limite = int(TAILLE_GRILLE / 3)
        for i in range(TAILLE_GRILLE):
            symbole = blanc if i < limite else (noir if i >= limite + 3 else " ")
            if symbole != " ":
                for j in range(TAILLE_GRILLE):
                    mettre_char_coord(grille, (i,j), symbole)

    def initialise_milieu(grille):
        liste = [2, 3, 3, 3, 2, 1, 1, 2, 3, 3, 3, 1, 2, 3, 2, 1, 3, 2, 3, 1, 3, 1, 2, 3, 3, 2, 3, 1, 2, 3, 3, 1, 1, 3, 2, 1, 3, 1, 2, 3, 1, 2, 3, 2, 1, 3, 2, 1, 1, 3, 2, 3, 2, 1, 1, 3, 2, 1, 3, 2, 3, 1, 2, 1, 3, 2, 1, 1, 3, 2, 3, 3, 1, 2, 1, 3, 1, 2, 1, 3, 2]
        remplir_depuis_liste(grille, liste, blanc, noir)

    def initialise_fin(grille):
        liste = [1, 3, 1, 1, 1, 2, 1, 2, 1, 3, 1, 1, 2, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 2, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        remplir_depuis_liste(grille, liste, blanc, noir)

    if periode == "debut":
        initialise_debut(grille)
    elif periode == "milieu":
        initialise_milieu(grille)
    else:
        initialise_fin(grille)


def afficher_grille(matrice):
    print("    A   B   C   D   E   F   G   H   I  ")
    print("  -------------------------------------")
    coordonnée_vertical = 0
    for ligne in matrice:
        ligne_final = "|"
        coordonnée_vertical += 1
        for valeur in ligne:
            ligne_final += f" {valeur} |"
        print(coordonnée_vertical, ligne_final)
        print("  -------------------------------------")


def est_au_bon_format(coord):
    if len(coord) == 2 and coord[0].isalpha() and coord[1].isdigit():
        lettre = coord[0].upper()
        chiffre = int(coord[1])
        if lettre in 'ABCDEFGHI' and 1 <= chiffre <= 9:
            return True
    return False

def est_dans_grille(coord):
    if est_au_bon_format(coord):
        coord_tuple = convertir_en_tuple(coord)
        if coord_tuple:
            x, y = coord_tuple
            if 0 <= x <= 8 and 0 <= y <= 8:
                return True
            return False
    else:
        return False

def demander_coord(grille,char):
    while True:
        coord = input("Rentrer une coordonnée (exp : A3) : ")
        if est_au_bon_format(coord):
            if not est_dans_grille(coord):
                print("Coordonnée invalide")
            else:
                x, y = convertir_en_tuple(coord)
                mettre_char_coord(grille, (y,x), char)
                break
        else:
            print("Coordonnée invalide")


def lancer_tour(grille):
    afficher_grille(grille)

    return 0

def menu_choix(type):
    print("Select a mode :")
    possibilité = "()"
    test_pos = ["1"]


    if type == "ouverture":
        print(" -> 1 : Atelier 2")
        print(" -> 2 : Atelier 3")
        print(" -> 3 : Jouer au jeu (Pas implementer)")
        print(" -> 4 : Relancer les tests")
        possibilité = "(1-3)"
        test_pos = ["1","2","3","3"]

    if type == "Atelier1":
        print(" -> 1 : Configuration de depart")
        print(" -> 2 : Configuration du milieu")
        print(" -> 3 : Configuration de fin")
        print(" -> 4 : Rentrer une coordonnée")
        possibilité = "(1-4)"
        test_pos = ["1","2","3","4"]

    if type == "Atelier12":
        print(" -> 1 : Configuration de depart")
        print(" -> 2 : Configuration du milieu")
        print(" -> 3 : Configuration de fin")
        print(" -> 4 : Rentrer une coordonnée")
        print(" -> 5 : Quitter")
        possibilité = "(1-5)"
        test_pos = ["1","2","3","4","5"]

    if type == "Atelier3":
        print(" -> 1 : Configuration de depart")
        print(" -> 2 : Configuration du milieu")
        print(" -> 3 : Configuration de fin")
        possibilité = "(1-3)"
        test_pos = ["1","2","3"]

    if type == "Atelier32":
        print(" -> 1 : Configuration de depart")
        print(" -> 2 : Configuration du milieu")
        print(" -> 3 : Configuration de fin")
        print(" -> 5 : Quitter")
        possibilité = "(1-5)"
        test_pos = ["1","2","3","4",]

    print("")
    choix = input("Entrer un numero "+ possibilité +" : ")
    if choix in test_pos:
        return int(choix)
    else:
        return 0


def test_est_au_bon_format():
    assert est_au_bon_format("A1") == 1  , "First Case"
    assert est_au_bon_format("I9") == 1  ,"Last Case"
    assert est_au_bon_format("Bad") == 0 , "Bad"
    assert est_au_bon_format("AZ") == 0  , "double lettre"



def test_est_dans_grille():
    assert est_dans_grille("A1") == 1  , "First Case"
    assert est_dans_grille("I9") == 1  , "Last Case"
    assert est_dans_grille("Bad") == 0 , "Bad"
    assert est_dans_grille("Z1") == 0  , "Pas dans la grille"
    assert est_dans_grille("A10") == 0 , "Pas dans la grille"
    assert est_dans_grille("A0") == 0  , "Pas dans la grille"
    assert est_dans_grille("J9") == 0  , "First case not on the grille"


def test_faire_elimination():
    blanc = donner_pion(1)
    noir = donner_pion(0)

    plateau_test = donner_grille()
    mettre_char_coord(plateau_test,(1,1),blanc)
    mettre_char_coord(plateau_test,(1,3),noir)
    assert faire_mouvement((1,1),(1,3), plateau_test,"elimination") == 0, "Bouger 2 case a droite"

    plateau_test = donner_grille()
    mettre_char_coord(plateau_test,(1,1),blanc)
    mettre_char_coord(plateau_test,(1,4),noir)
    assert faire_mouvement((1,1),(1,4), plateau_test,"elimination") == 0, "Bouger 3 case a droite"

    plateau_test = donner_grille()
    mettre_char_coord(plateau_test,(1,1),blanc)
    mettre_char_coord(plateau_test,(4,1),noir)
    assert faire_mouvement((1,1),(4,1), plateau_test,"elimination") == 0, "Bouger 3 case en bas"

    plateau_test = donner_grille()
    mettre_char_coord(plateau_test,(1,1),blanc)
    mettre_char_coord(plateau_test,(4,4),noir)
    assert faire_mouvement((1,1),(4,4), plateau_test,"elimination") == 0, "Bouger 3 case en diagonale"

    plateau_test = donner_grille()
    mettre_char_coord(plateau_test,(1,1),blanc)
    mettre_char_coord(plateau_test,(4,4),noir)
    assert faire_mouvement((4,4),(1,1), plateau_test,"elimination") == 0, "Bouger 3 case en diagonale"

    plateau_test = donner_grille()
    mettre_char_coord(plateau_test,(1,1),blanc)
    mettre_char_coord(plateau_test,(2,4),noir)
    assert faire_mouvement((1,1),(2,4), plateau_test,"elimination") == 1, "Deplacement invalide"

    plateau_test = donner_grille()
    mettre_char_coord(plateau_test,(1,1),blanc)
    mettre_char_coord(plateau_test,(4,1),noir)
    assert faire_mouvement((1,1),(2,1), plateau_test,"elimination") == 1, "Bouger 1 case en bas"

    plateau_test = donner_grille()
    mettre_char_coord(plateau_test,(1,1),blanc)
    mettre_char_coord(plateau_test,(4,4),noir)
    mettre_char_coord(plateau_test,(3,3),noir)
    assert faire_mouvement((1,1),(4,4), plateau_test,"elimination") == 1, "Bouger 3 case en diagonale avec pion au milieu"

def test_faire_retournement():
    blanc = donner_pion(1)
    noir = donner_pion(0)

    plateau_test = donner_grille()
    mettre_char_coord(plateau_test,(1,1),blanc)
    mettre_char_coord(plateau_test,(1,3),noir)
    assert faire_mouvement((1,1),(1,3), plateau_test,"retournement") == 1, "Bouger 2 case a droite avec pion a la fin"

    plateau_test = donner_grille()
    mettre_char_coord(plateau_test,(1,1),blanc)
    mettre_char_coord(plateau_test,(1,3),noir)
    assert faire_mouvement((1,1),(1,4), plateau_test,"retournement") == 0, "Bouger 4 case a droite"

    plateau_test = donner_grille()
    mettre_char_coord(plateau_test,(1,1),blanc)
    mettre_char_coord(plateau_test,(4,4),noir)
    mettre_char_coord(plateau_test,(3,3),noir)
    assert faire_mouvement((1,1),(4,4), plateau_test,"retournement") == 1, "Bouger 3 case en diagonale avec pion au milieu"

    plateau_test = donner_grille()
    mettre_char_coord(plateau_test,(1,1),blanc)
    mettre_char_coord(plateau_test,(3,3),noir)
    assert faire_mouvement((1,1),(4,4), plateau_test,"retournement") == 0, "Bouger 3 case en diagonale avec pion au milieu"

def test():
    test_est_au_bon_format()
    test_est_dans_grille()
    test_faire_elimination()
    test_faire_retournement()

def lancement():
    plateau_jeu = donner_grille()


    print(" ____             _        ")
    print("| __ )  ___  __ _| |_ __ _ ")
    print("|  _ \\ / _ \\/ _` | __/ _` |")
    print("| |_) |  __/ (_| |  ||(_| |")
    print("|____/ \\___|\\__,_|\\__\\__,_|")
    print("")

    test()

    choix = 0
    while not choix in [1,2]:
        choix = menu_choix("ouverture")

        if choix == 0:
            error("Choix hors de porté",0)
        if choix == 1:
            choix = menu_choix("Atelier1")
            while True:
                if choix in [1,2,3,4]:
                    plateau_jeu = donner_grille()
                    if choix == 1:
                        initialise(plateau_jeu,"debut")
                        afficher_grille(plateau_jeu)

                    elif choix == 2:
                        initialise(plateau_jeu,"milieu")
                        afficher_grille(plateau_jeu)
                    elif choix == 3:
                        initialise(plateau_jeu,"fin")
                        afficher_grille(plateau_jeu)
                    elif choix == 4:
                        demander_coord(plateau_jeu,"X")
                        afficher_grille(plateau_jeu)
                elif choix == 5:
                    quit()
                choix = menu_choix("Atelier12")

        if choix == 2:
            choix = menu_choix("Atelier3")
            while True:
                if choix in [1,2,3]:
                    plateau_jeu = donner_grille()
                    if choix == 1:
                        initialise(plateau_jeu,"debut")
                        afficher_grille(plateau_jeu)

                    elif choix == 2:
                        initialise(plateau_jeu,"milieu")
                        afficher_grille(plateau_jeu)
                    elif choix == 3:
                        initialise(plateau_jeu,"fin")
                        afficher_grille(plateau_jeu)
                elif choix == 4:
                    quit()
                choix = menu_choix("Atelier32")

        if choix == 3:
            print("Run test")
            test()
            print("")
            print("Test passé avec succés")
    choix = 0



lancement()
