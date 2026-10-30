# TP2 - POO et jeu du Morpion

Se lancer depuis ce dossier : `cd tp2`

| Partie | Fichier             | Commande                    | Contenu |
|--------|---------------------|-----------------------------|---------|
| A      | `partie_a.py`       | `python partie_a.py`        | Classe `Grille` : `afficher`, `jouer`, `est_gagnant`, `est_plein` |
| B      | `partie_b.py`       | `python partie_b.py`        | `JoueurHumain` (clavier) et `JoueurIA` (hasard), même méthode `prochain_coup(tab, symbole)` |
| C      | `partie_c.py`       | `python partie_c.py`        | Jeu complet : tours alternés, coups validés, victoire/nul, score multi-parties, 2 humains |
| Bonus  | `bonus_ia_malin.py` | `python bonus_ia_malin.py`  | `JoueurIAMalin` : gagne si possible, sinon bloque, sinon hasard |

## Convention
Un coup est `(x, y)` avec `x` = ligne et `y` = colonne, de 0 à 2.
Exemple : `(0, 2)` = première ligne, troisième colonne.

## Gestion d'erreurs
Case occupée, coup hors grille (`x = 3`, `x = -1`), saisie qui n'est pas deux nombres : message affiché,
le même joueur rejoue, pas de plantage.

## Modes de jeu (`partie_c.py`)
1. Humain contre IA (hasard)
2. Deux humains
3. Humain contre IA maligne (nécessite `bonus_ia_malin.py`)
4. IA contre IA : 20 parties, chaque partie finit par une victoire ou un nul
