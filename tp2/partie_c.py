"""TP2 - Partie C : jeu complet du Morpion (+ score multi-parties, 2 humains, IA vs IA)."""
from partie_a import Grille
from partie_b import JoueurHumain, JoueurIA

try:
    from bonus_ia_malin import JoueurIAMalin
except ImportError:
    JoueurIAMalin = None  # le bonus n'est pas présent : l'option 3 sera indisponible


def jouer_partie(joueur_x, joueur_o, afficher=True):
    """Joue une partie. joueur_x joue 'X' et commence, joueur_o joue 'O'.
    Renvoie le joueur gagnant, ou None en cas de match nul."""
    grille = Grille()
    joueurs = [(joueur_x, "X"), (joueur_o, "O")]
    tour = 0
    while True:
        joueur, symbole = joueurs[tour % 2]          # on alterne X, O, X, O...
        if afficher:
            print()
            grille.afficher()
            print(f"Au tour de {joueur.nom} ({symbole})")
        x, y = joueur.prochain_coup(grille, symbole)
        if not grille.jouer(x, y, symbole):
            continue                                 # coup invalide : le même joueur rejoue
        if grille.est_gagnant(symbole):              # victoire
            if afficher:
                print()
                grille.afficher()
                print(f"Victoire de {joueur.nom} !")
            return joueur
        if grille.est_plein():                       # grille pleine sans gagnant : nul
            if afficher:
                print()
                grille.afficher()
                print("Match nul.")
            return None
        tour += 1


def afficher_scores(scores):
    print("Scores :", ", ".join(f"{nom} {points}" for nom, points in scores.items()))


def tournoi_ia(nb_parties=20):
    """IA contre IA : joue nb_parties parties sans affichage et renvoie les scores."""
    ia1, ia2 = JoueurIA("IA 1"), JoueurIA("IA 2")
    scores = {ia1.nom: 0, ia2.nom: 0, "Nuls": 0}
    for _ in range(nb_parties):
        gagnant = jouer_partie(ia1, ia2, afficher=False)
        scores["Nuls" if gagnant is None else gagnant.nom] += 1
    return scores


def creer_joueurs():
    """Demande le mode de jeu et renvoie (joueur1, joueur2)."""
    while True:
        print("\n1) Humain contre IA   2) Deux humains   3) Humain contre IA maligne   4) IA contre IA (20 parties)")
        choix = input("Mode : ").strip()
        if choix == "1":
            return JoueurHumain("Vous"), JoueurIA("IA")
        if choix == "2":
            return JoueurHumain("Joueur 1"), JoueurHumain("Joueur 2")
        if choix == "3":
            if JoueurIAMalin is None:
                print("IA maligne indisponible (fichier bonus_ia_malin.py manquant).")
                continue
            return JoueurHumain("Vous"), JoueurIAMalin("IA maligne")
        if choix == "4":
            return None
        print("Choix invalide.")


def main():
    joueurs = creer_joueurs()
    if joueurs is None:                              # mode IA contre IA
        afficher_scores(tournoi_ia(20))
        return
    joueur_x, joueur_o = joueurs
    scores = {joueur_x.nom: 0, joueur_o.nom: 0, "Nuls": 0}
    while True:
        gagnant = jouer_partie(joueur_x, joueur_o)
        scores["Nuls" if gagnant is None else gagnant.nom] += 1
        afficher_scores(scores)
        if input("Rejouer ? (o/n) ").strip().lower() != "o":
            break
        joueur_x, joueur_o = joueur_o, joueur_x      # l'autre joueur commence la partie suivante


if __name__ == "__main__":
    try:
        main()
    except (EOFError, KeyboardInterrupt):
        print("\nÀ bientôt !")
