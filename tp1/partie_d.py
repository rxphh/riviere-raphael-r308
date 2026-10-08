"""TP1 - Partie D : Jeu du Pendu (+ bonus : hall of fame, ASCII art, mode 2 joueurs)."""
import getpass
import os
import unicodedata

from partie_a import charger, sauvegarder
from partie_c import charger_mots, choisir_mot, masque

# nombre d'erreurs autorisées
MAX_ERREURS = 7
FICHIER_SCORES = os.path.join(os.path.dirname(os.path.abspath(__file__)), "scores.txt")

# Dessins du pendu : l'indice correspond au nombre d'erreurs (0 à 7)
PENDU = [
    "\n\n\n\n\n\n=========",
    "\n      |\n      |\n      |\n      |\n      |\n=========",
    "  +---+\n      |\n      |\n      |\n      |\n      |\n=========",
    "  +---+\n  |   |\n      |\n      |\n      |\n      |\n=========",
    "  +---+\n  |   |\n  O   |\n      |\n      |\n      |\n=========",
    "  +---+\n  |   |\n  O   |\n /|\\  |\n      |\n      |\n=========",
    "  +---+\n  |   |\n  O   |\n /|\\  |\n /    |\n      |\n=========",
    "  +---+\n  |   |\n  O   |\n /|\\  |\n / \\  |\n      |\n=========",
]


def normaliser(c):
    """'é' -> 'E' : majuscule sans accent, pour comparer les lettres."""
    # sépare la lettre de son accent
    decompose = unicodedata.normalize("NFD", c)
    return "".join(x for x in decompose if not unicodedata.combining(x)).upper()


def reveler(mot, m, lettre):
    """Révèle toutes les positions de `lettre` (insensible casse/accents). True si présente."""
    trouvee = False
    for i, c in enumerate(mot):
        if normaliser(c) == lettre:
            m[i] = c
            trouvee = True
    return trouvee


# Mot accepté : lettres, tiret, apostrophe ou espace
def mot_valide(mot):
    return bool(mot) and all(c.isalpha() or c in "-' " for c in mot) and any(c.isalpha() for c in mot)


# Demande une seule lettre au joueur
def lire_lettre():
    while True:
        saisie = input("Lettre : ").strip()
        if len(saisie) != 1 or not saisie.isalpha():
            print("Entrez une seule lettre.")
            continue
        return normaliser(saisie)


def jouer_pendu(mot):
    """Une partie sur `mot`. Renvoie True si gagnée."""
    mot = mot.strip().upper()
    # masque de '_' (partie C)
    m = masque(mot)
    for i, c in enumerate(mot):          # tirets, espaces, apostrophes déjà visibles
        if not c.isalpha():
            m[i] = c
    # compteur d'erreurs et lettres déjà jouées
    erreurs, proposees = 0, []
    while True:
        # affichage du tour
        print(PENDU[erreurs])
        print("Mot      :", " ".join(m))
        print(f"Erreurs  : {erreurs}/{MAX_ERREURS}")
        print("Proposées:", " ".join(proposees) or "-")
        # plus de '_' : victoire
        if "_" not in m:
            print("Gagné !")
            return True
        # 7 erreurs : défaite
        if erreurs >= MAX_ERREURS:
            print(f"Perdu, le mot était {mot}")
            return False
        lettre = lire_lettre()
        # lettre déjà jouée : pas d'erreur
        if lettre in proposees:
            print("Lettre déjà proposée (pas d'erreur).")
            continue
        proposees.append(lettre)
        # lettre absente : une erreur de plus
        if not reveler(mot, m, lettre):
            erreurs += 1
            print("Absente !")
        else:
            print("Présente !")


def saisir_mot_secret():
    """Mode 2 joueurs : le joueur 1 tape le mot (masqué à l'écran)."""
    while True:
        try:
            mot = getpass.getpass("Mot secret (invisible) : ").strip().upper()
        except (EOFError, KeyboardInterrupt):
            raise
        except Exception:
            mot = input("Mot secret : ").strip().upper()
        if mot_valide(mot):
            # efface l'écran pour cacher le mot
            print("\n" * 30)
            return mot
        print("Mot invalide (lettres, tirets, espaces uniquement).")


# Programme principal : hall of fame et rejouer
def main():
    # scores relus depuis scores.txt (absent : départ à zéro)
    scores = charger(FICHIER_SCORES)
    nom = input("Votre nom : ").strip() or "Anonyme"
    scores.setdefault(nom, 0.0)
    mots = charger_mots()
    while True:
        choix = input("Mode : 1) mot aléatoire  2) mot choisi par un autre joueur [1] ").strip()
        mot = saisir_mot_secret() if choix == "2" else choisir_mot(mots)
        # victoire : +1 au score
        if jouer_pendu(mot):
            scores[nom] += 1
        # scores réécrits après chaque partie
        sauvegarder(scores, FICHIER_SCORES)
        print("Hall of fame :", ", ".join(f"{n} {int(v)}" for n, v in
                                          sorted(scores.items(), key=lambda x: -x[1])))
        if input("Rejouer ? (o/n) ").strip().lower() != "o":
            break


# Lancement du jeu
if __name__ == "__main__":
    try:
        main()
    except (EOFError, KeyboardInterrupt):
        print("\nÀ bientôt !")
