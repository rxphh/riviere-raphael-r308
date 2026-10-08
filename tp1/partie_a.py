"""TP1 - Partie A : dictionnaire d'étudiants (nom -> note)."""
import math
import os

# fichier placé à côté du script
FICHIER_DEFAUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "etudiants.txt")


def convertir_note(texte):
    """Convertit un texte en float ('12', '9,5', ' 15.0 '). Lève ValueError si invalide."""
    # remplace la virgule par un point, puis convertit en float
    valeur = float(str(texte).strip().replace(",", "."))
    # refuse les valeurs 'nan' et 'inf'
    if math.isnan(valeur) or math.isinf(valeur):
        raise ValueError(f"note invalide : {texte!r}")
    return valeur


def ajouter_etudiant(d, nom, note):
    """Ajoute ou met à jour un étudiant. Lève ValueError si nom vide ou note invalide."""
    nom = str(nom).strip()
    if not nom:
        raise ValueError("le nom ne peut pas être vide")
    # clé = nom, valeur = note (écrase l'ancienne note si le nom existe)
    d[nom] = convertir_note(note)


def moyenne_classe(d):
    """Moyenne arrondie à 2 décimales ; 0.0 si le dictionnaire est vide."""
    # dictionnaire vide : rien à calculer
    if not d:
        return 0.0
    # somme des notes / nombre d'étudiants, arrondi à 2 décimales
    return round(sum(d.values()) / len(d), 2)


def meilleur_etudiant(d):
    """Renvoie (nom, note) du meilleur étudiant, ou None si le dictionnaire est vide."""
    # dictionnaire vide : rien à calculer
    if not d:
        return None
    # max compare les noms d'après leur note
    nom = max(d, key=d.get)
    return nom, d[nom]


def sauvegarder(d, chemin=FICHIER_DEFAUT):
    """Écrit 'nom:note' par ligne. Renvoie True si OK, False en cas d'erreur d'E/S."""
    try:
        # 'w' = écriture ; 'with' ferme le fichier tout seul
        with open(chemin, "w", encoding="utf-8") as f:
            for nom, note in d.items():
                f.write(f"{nom}:{note}\n")
        return True
    # problème de fichier : on affiche l'erreur sans planter
    except OSError as e:
        print(f"Erreur d'écriture ({chemin}) : {e}")
        return False


def charger(chemin=FICHIER_DEFAUT):
    """Recharge le dictionnaire. Fichier absent -> {} ; lignes mal formées ignorées."""
    d = {}
    try:
        # 'r' = lecture
        with open(chemin, "r", encoding="utf-8") as f:
            for numero, ligne in enumerate(f, start=1):
                ligne = ligne.strip()
                if not ligne:
                    continue
                try:
                    # sépare 'nom:note' sur le dernier ':'
                    nom, note = ligne.rsplit(":", 1)  # rsplit : le nom peut contenir ':'
                    ajouter_etudiant(d, nom, note)
                # ligne mal formée : on l'ignore
                except ValueError:
                    print(f"Ligne {numero} ignorée (mal formée) : {ligne!r}")
    # fichier absent : on renvoie un dictionnaire vide
    except FileNotFoundError:
        pass  # premier lancement : on part de zéro
    except (OSError, UnicodeDecodeError) as e:
        print(f"Erreur de lecture ({chemin}) : {e}")
    return d


# Test avec le jeu d'essai du sujet
if __name__ == "__main__":
    classe = {}
    for n, v in [("Alice", 12), ("Bob", 15), ("Claire", 9.5)]:
        ajouter_etudiant(classe, n, v)
    print("Moyenne :", moyenne_classe(classe))          # 12.17
    print("Meilleur :", meilleur_etudiant(classe))      # ('Bob', 15.0)
    if sauvegarder(classe):
        print("Rechargé :", charger())
    print("Vide :", moyenne_classe({}), meilleur_etudiant({}))
