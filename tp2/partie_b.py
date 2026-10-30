"""TP2 - Partie B : classes JoueurHumain et JoueurIA.

Les deux classes ont la même méthode prochain_coup(tab, symbole) qui renvoie (x, y),
avec x = ligne et y = colonne. tab est la Grille, symbole est 'X' ou 'O'.
"""
import random


class JoueurHumain:
    """Joueur qui saisit son coup au clavier."""

    def __init__(self, nom="Joueur"):
        self.nom = nom

    def prochain_coup(self, tab, symbole):
        """Demande 'ligne colonne' (exemple : 1 2) et renvoie (x, y)."""
        while True:
            texte = input(f"{self.nom} ({symbole}) - ligne et colonne (0 à 2, ex : 1 2) : ")
            morceaux = texte.replace(",", " ").split()
            if len(morceaux) == 2:
                try:
                    return int(morceaux[0]), int(morceaux[1])
                except ValueError:
                    pass  # pas des nombres : on redemande
            print("Saisie invalide : tapez deux nombres entiers, par exemple 1 2.")
            # Remarque : on ne vérifie pas ici si la case est libre, la Grille s'en charge.


class JoueurIA:
    """Joueur qui joue une case libre au hasard."""

    def __init__(self, nom="IA"):
        self.nom = nom

    def prochain_coup(self, tab, symbole):
        """Renvoie une case libre choisie au hasard."""
        libres = tab.cases_libres()
        if not libres:
            raise ValueError("la grille est pleine")
        return random.choice(libres)


if __name__ == "__main__":
    from partie_a import Grille

    g = Grille()
    ia = JoueurIA()
    print("Coup de l'IA sur une grille vide :", ia.prochain_coup(g, "X"))
