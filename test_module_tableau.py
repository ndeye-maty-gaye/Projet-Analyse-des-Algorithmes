import module_tableau as mt
import random

# 1. Génération du tableau
lignes, colonnes = 3, 3
table = mt.generer_tableau(lignes, colonnes)



# 2. AFFICHAGE HORIZONTAL (2D réel)
def afficher_tableau(titre, tab):
    print(f"\n{titre} : {tab}")


# 3. TEST DES TRI
def tester_tri(nom, fonction_tri):
    print(f"\n{nom}")

    afficher_tableau("Tableau initial", table)

    table_trie = fonction_tri(table)

    afficher_tableau("Tableau trié", table_trie)

    return table_trie



if __name__ == "__main__":
    tri_bulle = tester_tri("TRI À BULLE", mt.tri_bulle)
    tri_selection = tester_tri("TRI PAR SÉLECTION", mt.tri_selection)
    tri_insertion = tester_tri("TRI PAR INSERTION", mt.tri_insertion)
    tri_rapide = tester_tri("TRI RAPIDE", mt.tri_rapide)
    tri_fusion = tester_tri("TRI PAR FUSION", mt.tri_fusion)

    # 4. UTILITAIRE POSITION
    def index_to_position(index, colonnes):
        if index is None:
            return None
        return (index // colonnes, index % colonnes)

    # 5. TEST DES RECHERCHES
    def tester_recherche(nom, fonction, table_trie):
        print(f"\n{nom}")
        afficher_tableau("Tableau trié", table_trie)
        # Valeur existante (prise dans le tableau)
        valeurs = [x for ligne in table_trie for x in ligne]
        valeur_existante = random.choice(valeurs)
        print("\nValeur existante recherchée :", valeur_existante)
        res = fonction(table_trie, valeur_existante)
        if isinstance(res, tuple):
            pos = res
        else:
            pos = index_to_position(res, colonnes)
        print("Position trouvée :", pos)
        # Valeur inexistante
        valeur_absente = max(valeurs) + 100
        print("\nValeur inexistante recherchée :", valeur_absente)
        res = fonction(table_trie, valeur_absente)
        if isinstance(res, tuple):
            pos = res
        else:
            pos = index_to_position(res, colonnes)
        print("Résultat :", pos)

    # Utilisation du tableau trié (fusion)
    tester_recherche("RECHERCHE LINÉAIRE", mt.recherche_lineaire, tri_fusion)
    tester_recherche("RECHERCHE BINAIRE", mt.recherche_binaire, tri_fusion)
    tester_recherche("RECHERCHE DICHOTOMIQUE", mt.recherche_dichotomie, tri_fusion)

    # FIN
    print("\nFIN DES TESTS")