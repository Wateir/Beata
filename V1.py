TAILLE_GRILLE = 9

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
    pass

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
    if len(coord) == 2:
        if coord[0].isalpha and coord[0].isupper:
            if coord[1].isdigit:
                return 1
            else:
                return 0
        else:
            return 0
    else:
        return 0

def est_dans_grille(coord):
    if not est_au_bon_format(coord):
        return 0

    lettre = transfrom_lettre_chiffre(coord[0])
    chiffre = int(coord[1]) - 1
    if lettre > 8 or chiffre < 0 or chiffre > 8:
        return 0

    return 1

def transfrom_lettre_chiffre(chiffre):
    lettres = {
        "A": 0,
        "B": 1,
        "C": 2,
        "D": 3,
        "E": 4,
        "F": 5,
        "G": 6,
        "H": 7,
        "I": 8,
        "J": 9,
        "K": 10,
        "L": 11,
        "M": 12,
        "N": 13,
        "O": 14,
        "P": 15,
        "Q": 16,
        "R": 17,
        "S": 18,
        "T": 19,
        "U": 20,
        "V": 21,
        "W": 22,
        "X": 23,
        "Y": 24,
        "Z": 25
    }
    return lettres[chiffre]


def test_est_au_bon_format():
    assert est_au_bon_format("A1") == 1  , "First Case"
    assert est_au_bon_format("I9") == 1  ,"Last Case"
    assert est_au_bon_format("Bad") == 0 , "Bad"



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

    initialise_debut(plateau_jeu)
    afficher_grille(plateau_jeu)

lancement()
