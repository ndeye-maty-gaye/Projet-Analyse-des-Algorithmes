import random

# Génération d'un tableau 2D aléatoire
def generer_tableau(lignes, colonnes, min_val=0, max_val=50):
    """
    Génère un tableau 2D de dimensions (lignes x colonnes) avec des entiers aléatoires.
    """
    if not (isinstance(lignes, int) and isinstance(colonnes, int)):
        raise ValueError("lignes et colonnes doivent être des entiers")
    if lignes <= 0 or colonnes <= 0:
        raise ValueError("lignes et colonnes doivent être > 0")
    return [[random.randint(min_val, max_val) for _ in range(colonnes)] for _ in range(lignes)]


# Utilitaires

def aplatir(table):
    """Aplati un tableau 2D en une liste 1D."""
    if not table or not isinstance(table, list) or not isinstance(table[0], list):
        raise ValueError("Le tableau doit être une liste de listes non vide.")
    return [element for ligne in table for element in ligne]


def reconstruire(liste, lignes, colonnes):
    """Reconstruit un tableau 2D à partir d'une liste 1D."""
    if len(liste) != lignes * colonnes:
        raise ValueError("La taille de la liste ne correspond pas aux dimensions données.")
    return [liste[i * colonnes:(i + 1) * colonnes] for i in range(lignes)]
def afficher_tableau(tab):
    """Affiche le tableau 2D ligne par ligne."""
    for ligne in tab:
        print("\t".join(str(x) for x in ligne))



# TRI À BULLE
def tri_bulle(table):
    """
    Le tri à bulle est un algorithme qui compare les éléments voisins
    et les échange s'ils ne sont pas dans le bon ordre, jusqu'à obtenir une liste triée.

    Exemple avec tableau 2D aléatoire :
    [[5, 2, 9],
     [1, 7, 3]]

    Aplatir → [5, 2, 9, 1, 7, 3]

    Comparaisons successives :
    [5,2] → échange → [2,5,9,1,7,3]
    [9,1] → échange → [2,5,1,9,7,3]

    Résultat final :
    [1,2,3,5,7,9]
    """
    tab = aplatir(table)
    n = len(tab)
    tab = tab.copy()
    for i in range(n):
        for j in range(0, n - i - 1):
            if tab[j] > tab[j + 1]:
                tab[j], tab[j + 1] = tab[j + 1], tab[j]
    return reconstruire(tab, len(table), len(table[0]))


# TRI PAR SÉLECTION
def tri_selection(table):
    """
    Le tri par sélection consiste à chercher le plus petit élément
    et à le placer à sa position correcte.

    Exemple :
    [5, 2, 9, 1, 7, 3]

    Étape 1 :
    minimum = 1 → placé au début
    [1,2,9,5,7,3]

    Étapes suivantes :
    on répète jusqu'à trier toute la liste.
    """
    tab = aplatir(table)
    n = len(tab)
    tab = tab.copy()
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if tab[j] < tab[min_index]:
                min_index = j
        tab[i], tab[min_index] = tab[min_index], tab[i]
    return reconstruire(tab, len(table), len(table[0]))


# TRI PAR INSERTION
def tri_insertion(table):
    """
    Le tri par insertion consiste à prendre chaque élément
    et à l'insérer à la bonne position dans la partie déjà triée.

    Exemple :
    [5, 2, 9, 1]

    Étapes :
    5 → ok
    2 → inséré avant 5 → [2,5,9,1]
    9 → ok
    1 → devient premier → [1,2,5,9]
    """
    tab = aplatir(table)
    tab = tab.copy()
    for i in range(1, len(tab)):
        key = tab[i]
        j = i - 1
        while j >= 0 and tab[j] > key:
            tab[j + 1] = tab[j]
            j -= 1
        tab[j + 1] = key
    return reconstruire(tab, len(table), len(table[0]))


# TRI RAPIDE
def tri_rapide(table):
    """
    Le tri rapide divise la liste en deux parties autour d'un pivot,
    puis trie chaque partie séparément.

    Exemple :
    [5, 2, 9, 1]

    pivot = 5
    gauche = [2,1]
    droite = [9]

    Résultat final :
    [1,2,5,9]
    """

    def quicksort(tab):
        if len(tab) <= 1:
            return tab

        pivot = tab[0]
        gauche = [x for x in tab[1:] if x <= pivot]
        droite = [x for x in tab[1:] if x > pivot]

        return quicksort(gauche) + [pivot] + quicksort(droite)

    tab = aplatir(table)
    tab = quicksort(tab.copy())
    return reconstruire(tab, len(table), len(table[0]))


# TRI PAR FUSION
def tri_fusion(table):
    """
    Le tri par fusion consiste à diviser la liste en sous-listes,
    les trier, puis les fusionner.

    Exemple :
    [5,2,9,1]

    Découpage :
    [5,2] et [9,1]

    Tri :
    [2,5] et [1,9]

    Fusion :
    [1,2,5,9]
    """

    def fusion(gauche, droite):
        resultat = []
        i = j = 0

        while i < len(gauche) and j < len(droite):
            if gauche[i] < droite[j]:
                resultat.append(gauche[i])
                i += 1
            else:
                resultat.append(droite[j])
                j += 1

        resultat.extend(gauche[i:])
        resultat.extend(droite[j:])
        return resultat

    def merge_sort(tab):
        if len(tab) <= 1:
            return tab

        milieu = len(tab) // 2
        gauche = merge_sort(tab[:milieu])
        droite = merge_sort(tab[milieu:])

        return fusion(gauche, droite)

    tab = aplatir(table)
    tab = merge_sort(tab.copy())
    return reconstruire(tab, len(table), len(table[0]))


# RECHERCHE LINÉAIRE
def recherche_lineaire(table, valeur):
    """
    La recherche linéaire consiste à parcourir tous les éléments
    jusqu'à trouver la valeur recherchée.

    Exemple :
    [[5,2,9],
     [1,7,3]]

    Recherche 7 :
    on parcourt ligne par ligne → trouvé en position (1,1)
    """
    for i in range(len(table)):
        for j in range(len(table[0])):
            if table[i][j] == valeur:
                return (i, j)
    return None


# RECHERCHE BINAIRE
def recherche_binaire(table, valeur):
    """
    La recherche binaire consiste à diviser la liste triée en deux
    pour trouver rapidement une valeur.

    Exemple :
    [1,2,3,5,7,9]

    Recherche 7 :
    milieu = 5 → aller à droite → trouvé
    """
    tab = aplatir(table)
    gauche, droite = 0, len(tab) - 1
    while gauche <= droite:
        milieu = (gauche + droite) // 2
        if tab[milieu] == valeur:
            return milieu
        elif tab[milieu] < valeur:
            gauche = milieu + 1
        else:
            droite = milieu - 1
    return None


# RECHERCHE PAR DICHOTOMIE
def recherche_dichotomie(table, valeur):
    """
    La recherche par dichotomie est une version récursive
    de la recherche binaire.

    Elle applique le même principe de division en deux,
    mais avec des appels récursifs.
    """

    def dichotomie(tab, valeur, gauche, droite):
        if gauche > droite:
            return None

        milieu = (gauche + droite) // 2

        if tab[milieu] == valeur:
            return milieu
        elif tab[milieu] < valeur:
            return dichotomie(tab, valeur, milieu + 1, droite)
        else:
            return dichotomie(tab, valeur, gauche, milieu - 1)

    tab = aplatir(table)
    return dichotomie(tab, valeur, 0, len(tab) - 1)


# Démonstration si exécuté directement
if __name__ == "__main__":
    print("Démonstration du module_tableau :\n")
    lignes, colonnes = 3, 3
    tab = generer_tableau(lignes, colonnes)
    print("Tableau généré :")
    afficher_tableau(tab)
    print("\nTri à bulle :")
    afficher_tableau(tri_bulle(tab))
    print("\nTri par sélection :")
    afficher_tableau(tri_selection(tab))
    print("\nTri par insertion :")
    afficher_tableau(tri_insertion(tab))
    print("\nTri rapide :")
    afficher_tableau(tri_rapide(tab))
    print("\nTri par fusion :")
    afficher_tableau(tri_fusion(tab))
    valeur = tab[0][0]
    print(f"\nRecherche linéaire de {valeur} :", recherche_lineaire(tab, valeur))
    tab_trie = tri_fusion(tab)
    print(f"Recherche binaire de {valeur} :", recherche_binaire(tab_trie, valeur))
    print(f"Recherche dichotomie de {valeur} :", recherche_dichotomie(tab_trie, valeur))