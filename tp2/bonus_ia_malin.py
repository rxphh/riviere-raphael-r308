"""TP2 - Bonus Jeu 1 : JoueurIAMalin (gagne si possible, sinon bloque, sinon hasard)."""
from partie_b import JoueurIA


class JoueurIAMalin(JoueurIA):
    """IA qui réfléchit un peu : 1) coup gagnant, 2) blocage, 3) hasard."""

    def __init__(self, nom="IA maligne"):
        super().__init__(nom)

    def _coup_gagnant(self, tab, symbole):
        """Renvoie une case qui fait gagner `symbole`, ou None s'il n'y en a pas."""
        for x, y in tab.cases_libres():
            essai = tab.copie()           # on teste sur une copie, la vraie grille ne bouge pas
            essai.jouer(x, y, symbole)
            if essai.est_gagnant(symbole):
                return (x, y)
        return None

    def prochain_coup(self, tab, symbole):
        adversaire = "O" if symbole == "X" else "X"
        coup = self._coup_gagnant(tab, symbole)       # 1) je peux gagner
        if coup is not None:
            return coup
        coup = self._coup_gagnant(tab, adversaire)    # 2) je bloque l'adversaire
        if coup is not None:
            return coup
        return super().prochain_coup(tab, symbole)    # 3) sinon hasard


if __name__ == "__main__":
    from partie_a import Grille

    def grille_depuis(texte):
        """Construit une grille depuis 'XX_/_O_/___' pour tester."""
        g = Grille()
        for x, ligne in enumerate(texte.split("/")):
            for y, car in enumerate(ligne):
                if car != "_":
                    g.cases[x][y] = car
        return g

    ia = JoueurIAMalin()
    print("Blocage :", ia.prochain_coup(grille_depuis("XX_/_O_/___"), "O"))   # (0, 2)
    print("Gagne   :", ia.prochain_coup(grille_depuis("OO_/XX_/___"), "O"))   # (0, 2)
