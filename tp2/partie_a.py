"""TP2 - Partie A : classe Grille (morpion 3x3)."""


class Grille:
    """Grille 3x3 : une liste de 3 listes de 3 cases. Une case vide contient ' '."""

    def __init__(self):
        # 3 lignes de 3 cases vides
        self.cases = [[" " for _ in range(3)] for _ in range(3)]

    def afficher(self):
        """Affiche la grille de façon lisible."""
        lignes = []
        for ligne in self.cases:
            lignes.append(" " + " | ".join(ligne))
        print("\n---------\n".join(lignes))

    def dans_grille(self, x, y):
        """True si (x, y) est une case de la grille (0, 1 ou 2)."""
        return isinstance(x, int) and isinstance(y, int) and 0 <= x < 3 and 0 <= y < 3

    def jouer(self, x, y, joueur):
        """Place 'X' ou 'O' en (x, y) = (ligne, colonne).
        Renvoie True si le coup est accepté, False s'il est refusé."""
        if joueur not in ("X", "O"):
            print("Joueur invalide : utilisez 'X' ou 'O'.")
            return False
        if not self.dans_grille(x, y):
            print(f"Case ({x}, {y}) hors grille : choisissez des nombres entre 0 et 2.")
            return False
        if self.cases[x][y] != " ":
            print(f"Case ({x}, {y}) déjà occupée.")
            return False
        self.cases[x][y] = joueur
        return True

    def est_gagnant(self, j):
        """True si le joueur j a aligné 3 symboles (ligne, colonne ou diagonale)."""
        if j not in ("X", "O"):
            return False
        c = self.cases
        alignements = []
        for i in range(3):
            alignements.append(c[i])                          # ligne i
            alignements.append([c[0][i], c[1][i], c[2][i]])   # colonne i
        alignements.append([c[0][0], c[1][1], c[2][2]])       # diagonale
        alignements.append([c[0][2], c[1][1], c[2][0]])       # autre diagonale
        return any(all(case == j for case in a) for a in alignements)

    def est_plein(self):
        """True si aucune case n'est libre."""
        return all(case != " " for ligne in self.cases for case in ligne)

    def cases_libres(self):
        """Liste des cases libres sous la forme (x, y)."""
        return [(x, y) for x in range(3) for y in range(3) if self.cases[x][y] == " "]

    def copie(self):
        """Renvoie une copie indépendante de la grille (utile pour tester un coup)."""
        autre = Grille()
        autre.cases = [ligne[:] for ligne in self.cases]
        return autre


if __name__ == "__main__":
    # Jeu d'essai du sujet
    g = Grille()
    g.jouer(0, 0, "X")
    g.jouer(0, 1, "O")
    g.jouer(1, 1, "X")
    g.afficher()
    print("Case occupée :", g.jouer(0, 0, "O"))      # False
    print("Hors grille  :", g.jouer(3, 0, "O"))      # False
    print("X gagne ?", g.est_gagnant("X"))           # False
    g.jouer(2, 2, "X")
    print("X gagne ?", g.est_gagnant("X"))           # True
    print("Plein ?", g.est_plein())                  # False
