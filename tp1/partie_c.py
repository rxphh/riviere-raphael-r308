"""TP1 - Partie C : manipulation des mots."""
import os
import random

# fichier de mots placé à côté du script
FICHIER_MOTS = os.path.join(os.path.dirname(os.path.abspath(__file__)), "mots.txt")
# liste utilisée si le fichier est absent
MOTS_SECOURS = ["python", "reseau", "routeur", "protocole", "serveur"]


def charger_mots(chemin=FICHIER_MOTS):
    """Charge les mots d'un .txt (un par ligne). Si absent/vide : liste de secours."""
    try:
        with open(chemin, "r", encoding="utf-8") as f:
            # un mot par ligne, on ignore les lignes vides
            mots = [ligne.strip() for ligne in f if ligne.strip()]
    except (OSError, UnicodeDecodeError) as e:
        print(f"Lecture de {chemin} impossible ({e}), liste par défaut utilisée.")
        mots = []
    # liste de secours si le fichier est vide ou absent
    return mots or list(MOTS_SECOURS)


def choisir_mot(liste):
    """Renvoie un mot de la liste, en MAJUSCULES."""
    if not liste:
        raise ValueError("la liste de mots est vide")
    # mot au hasard, en MAJUSCULES
    return random.choice(liste).strip().upper()


def masque(mot):
    """masque('PYTHON') -> ['_', '_', '_', '_', '_', '_']"""
    # un '_' par lettre du mot
    return ["_"] * len(mot)


# Test rapide
if __name__ == "__main__":
    mot = choisir_mot(charger_mots())
    print(mot, masque(mot))
    print(masque("PYTHON"))
