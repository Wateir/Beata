TAILLE_GRILLE = 9

def error(texte,type):
    if type == 0:
        print("\033[31m==>\033[0m "+ texte)
        print("")


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


def mettre_char_coord(grille,x,y,char):
    grille[x][y]=char

def initialise_debut(grille):
    i = 0
    for i in range(int(TAILLE_GRILLE/3)):
        for y in range(TAILLE_GRILLE):
            mettre_char_coord(grille, i, y, "●")
    for i in range(int(TAILLE_GRILLE/3+3),TAILLE_GRILLE):
        for y in range(TAILLE_GRILLE):
            mettre_char_coord(grille, i , y, "○")

def initialise_milieu(grille):
    liste = [2, 3, 1, 3, 2, 1, 1, 2, 3, 3, 1, 1, 2, 3, 2, 1, 3, 2, 1, 1, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 3, 1, 1, 3, 2, 1, 3, 1, 2, 3, 1, 2, 3, 2, 1, 3, 2, 1, 1, 3, 2, 3, 2, 1, 1, 3, 2, 1, 3, 2, 3, 1, 2, 1, 3, 2, 1, 1, 3, 2, 3, 3, 1, 2, 1, 3, 1, 2, 1, 3, 2]
    for i in range(TAILLE_GRILLE):
        for j in range (TAILLE_GRILLE):
            if liste[i*TAILLE_GRILLE+j] == 1:
                mettre_char_coord(grille, i, j, "●")
            if liste[i*TAILLE_GRILLE+j] == 2:
                mettre_char_coord(grille, i, j, "○")

def initialise_fin(grille):
    pass

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




def menu_choix(type):
    print("Select a mode :")
    possibilité = "()"
    test_pos = ["1"]


    if type == "ouverture":
        print(" -> 1 : Atelier 1")
        print(" -> 2 : Jouer au jeu (Pas implementer)")
        print(" -> 3 : Relancer les tests")
        possibilité = "(1-3)"
        test_pos = ["1","2","3"]

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


def test():
    test_est_au_bon_format()
    test_est_dans_grille()

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
    while not choix in [1]:
        choix = menu_choix("ouverture")
        if choix == 0:
            error("Choix hors de porté",0)
        if choix == 1:
            print("Run test")
            test()
    choix = 0

    choix = menu_choix("Atelier1")
    while True:
        if choix in [1,2,3,4]:
            if choix == 1:
                initialise_debut(plateau_jeu)
                afficher_grille(plateau_jeu)

            elif choix == 2:
                initialise_milieu(plateau_jeu)
                afficher_grille(plateau_jeu)
            elif choix == 3:
                initialise_fin(plateau_jeu)
                afficher_grille(plateau_jeu)
            elif choix == 4:
                coord = input("Rentrer une coordonnée (exp : A3) : ")
                if est_au_bon_format(coord):
                    if not est_dans_grille(coord):
                        print("Coordonnée invalide")
                    else:
                        x, y = convertir_en_tuple(coord)
                        mettre_char_coord(plateau_jeu, x, y, "X")
                        print("Yo")
                        afficher_grille(plateau_jeu)
                else:
                    print("Coordonnée invalide")
        elif choix == 5:
            break
        choix = menu_choix("Atelier12")

lancement()
