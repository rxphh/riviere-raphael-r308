"""TP1 - Partie B : « Devine le nombre » (bornes personnalisables, rejouable)."""
import random


def lire_entier(invite, defaut=None):
    """Lit un entier ; redemande tant que la saisie est invalide. Entrée vide -> défaut."""
    while True:
        texte = input(invite).strip()
        if not texte and defaut is not None:
            return defaut
        try:
            return int(texte)
        except ValueError:
            print("Veuillez entrer un nombre entier.")


def jouer(mini=1, maxi=100, essais_max=10):
    """Une partie. Renvoie True si gagnée."""
    # nombre secret tiré au hasard (bornes incluses)
    secret = random.randint(mini, maxi)
    # 10 essais maximum
    for essai in range(1, essais_max + 1):
        proposition = lire_entier(f"Essai {essai}/{essais_max} - votre nombre ({mini}-{maxi}) : ")
        # compare la proposition au nombre secret
        if proposition < secret:
            print("Trop petit")
        elif proposition > secret:
            print("Trop grand")
        else:
            print(f"Gagné en {essai} essai(s) !")
            return True
    # les essais sont épuisés
    print(f"Perdu ! Le nombre était {secret}.")
    return False


# Bonus : le joueur choisit les bornes (Entrée = valeurs par défaut)
def configurer_bornes():
    while True:
        mini = lire_entier("Borne min [1] : ", 1)
        maxi = lire_entier("Borne max [100] : ", 100)
        if mini < maxi:
            return mini, maxi
        print("Le minimum doit être inférieur au maximum.")


# Programme principal : on peut rejouer
if __name__ == "__main__":
    mini, maxi = configurer_bornes()
    while True:
        jouer(mini, maxi)
        # toute réponse autre que 'o' arrête le jeu
        if input("Rejouer ? (o/n) ").strip().lower() != "o":
            break
