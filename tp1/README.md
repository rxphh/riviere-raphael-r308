# TP1 - Gestion de données et mini-jeux

Se lancer depuis ce dossier : `cd tp1`

| Partie | Fichier        | Commande                | Contenu |
|--------|----------------|-------------------------|---------|
| A      | `partie_a.py`  | `python partie_a.py`    | Dictionnaire nom -> note, moyenne, meilleur étudiant, sauvegarde/chargement `nom:note` |
| B      | `partie_b.py`  | `python partie_b.py`    | Devine le nombre (10 essais, bornes personnalisables, rejouable) |
| C      | `partie_c.py`  | `python partie_c.py`    | `choisir_mot` (majuscules) et `masque` |
| D      | `partie_d.py`  | `python partie_d.py`    | Pendu (7 erreurs), ASCII art, mode 2 joueurs |

## Bonus
- **Hall of fame** : scores dans `scores.txt` (`Ana:2.0`), relu au lancement, créé à la première victoire.
- **Tournoi** : mode 2 joueurs (choix `2`), le mot est saisi sans s'afficher.
- **Défi accents/majuscules** : `ÉLÉPHANT` et `Python` fonctionnent (lettres comparées sans accent ni casse).

## Gestion d'erreurs
Fichier absent, ligne mal formée, note non numérique (`9,5` accepté), saisie invalide : pas de plantage.
