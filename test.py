# Vérifier si le terminal supporte les séquences d'échappement ANSI
def verifierSupportAnsi():
    try:
        # Essaie d'imprimer une séquence ANSI
        print("\x1b[31mCe texte est rouge !\x1b[0m")
        print("\x1b[1A\x1b[2K", end="")
        return True
    except Exception:
        return False

if verifierSupportAnsi():
    print("Le terminal supporte les séquences ANSI.")
else:
    print("Le terminal ne supporte pas les séquences ANSI.")
