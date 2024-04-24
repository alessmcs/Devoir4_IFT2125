# Nom, Matricule
# Nom, Matricule

import math
import random
import sys


def write(fileName, content):
    """Écrire la sortie dans un fichier/write output in file"""
    file = open(fileName, "w")
    file.write(content)
    file.close()


# faire de l'exponentiation modulaire
def expoMod(a, t, n):
    res = 1
    a = a % n
    while (t > 0):
        if (t & 1):
            res = (res * a) % n
        t = t >> 1
        a = (a * a) % n
    return res


# GeeksForGeeks & wikipedia
def millerRabin(t, n):
    # choix de a, selon le critère de Miller
    a = 0
    while not (1 <= a <= n - 2):
        # if n < 3,825,123,056,546,413,051, it is enough to test a = 2, 3, 5, 7, 11, 13, 17, 19, and 23
        # https://www.wikiwand.com/en/Miller%E2%80%93Rabin_primality_test
        tabA = [2, 3, 5, 7, 11, 13, 17, 19, 23]
        randIndex = random.randrange(0, len(tabA) - 1)
        a = tabA[randIndex]

    x = expoMod(a, t, n)

    if (x == 1 or x == n - 1):
        return True

    while (t != n - 1):
        x = (x * x) % n
        t *= 2
        if (x == 1):
            return False;
        if (x == n - 1):
            return True

    return False


# test tiré de # https://www.geeksforgeeks.org/primality-test-set-3-miller-rabin/
def BTest(n, k):
    # cas extrêmes
    if (1 < n <= 3 or n == 5):
        return True
    if (n <= 1 or n % 2 == 0 or n % 3 == 0 or n % 11 == 0):
        return False

    t = n - 1
    while (t % 2 == 0):
        t //= 2

    # répéter miller-rabin plusieurs fois pour accuracy
    for i in range(k):
        if (millerRabin(t, n) == False):
            return False

    return True


# trouve le prochain nombre premier
def nextPrime(n):
    isPrime = False
    i = n
    while not isPrime:
        i += 1
        isPrime = BTest(i, 4)
    return i  # the next prime


# tester si a et b forment une paire spéciale
def testPaireSpeciale(a, b):
    if BTest(int(str(a) + str(b)), 4) and BTest(int(str(b) + str(a)), 4):
        return True
    else:
        return False


def deep_first_search(node, clique, adjacence, visited):
    visited.add(node)
    clique.add(node)
    for voisin in adjacence[node]:
        if voisin not in visited and (voisin not in clique):
            deep_first_search(voisin, clique, adjacence, visited)


# def clique_4_premier(adjacence, cliquesExistantes) :

# def etendre_clique(cliqueActuelle):
#     if len(cliqueActuelle) == 4:
#         special_pair = all(testPaireSpeciale(a, b) for a in cliqueActuelle for b in cliqueActuelle if a != b)
#         if special_pair:
#             cliques.add(cliqueActuelle)
#     elif len(cliqueActuelle) < 4:
#         for voisin in adjacence[cliqueActuelle[-1]]:
#             if all(voisin in adjacence[node] for node in cliqueActuelle):
#                 etendre_clique(adjacence[voisin])

# cliques = [set(c) for c in cliquesExistantes]
# for node in adjacence:
#     etendre_clique(adjacence[node])
# return cliques

# code d'info theo figure it out tmr

# def trouver4clique(adj):
#     noeudsValides = []
#     for node in adj:
#         # on va seulement regarder les noeuds qui ont au moins 3 voisins, car ceux qui ont moins seront pas dans la 4-clique
#         if len(adj[node]) >= 3: 
#             noeudsValides.append(node)

#     for node in adj:
#         cliqueTrouvee = set()
#         for i in adj[node]:

#SAM Excellent code pr backtrack, c le meme que le mien hehehe
def cliqueBacktrack(cliquesExistantes, graphe, noeudActuel, cliqueActuelle):
    clique = cliqueActuelle
    # si le noeud actual a moins de 3 voisins, return
    if len(clique) > 5:
        return
    if len(graphe[noeudActuel]) < 3:
        return

    if len(clique) == 4:
        # une fois qu'on a trouvé une clique de taille 4, verifier si c'est special
        special = True
        for i in range(len(clique)):
            for j in range(i + 1, len(clique)):
                # print(clique[i])
                # print(clique[j])
                # print()
                if not testPaireSpeciale(clique[i], clique[j]):
                    special = False
        if special == True and set(clique) not in cliquesExistantes:
            cliquesExistantes.append(set(clique))
        return
    else:
        for voisin in graphe[noeudActuel]:
            # and i not in v
            if voisin not in clique:
                peuxAjouter = True
                for elem in cliqueActuelle:
                    if not testPaireSpeciale(elem, voisin):
                        peuxAjouter = False
                if peuxAjouter:
                    tentative_clique = clique.copy()
                    tentative_clique.append(voisin)
                    cliqueBacktrack(cliquesExistantes, graphe, noeudActuel, tentative_clique)
                    # we only swim up every time a 4-clique is found, so update cliquesExistantes for the current instance and keep searching
    return


# https://fr.wikipedia.org/wiki/Tri_fusion#Algorithme
def triFusion(L):
    if len(L) == 1:
        return L
    else:
        return fusion(triFusion(L[:len(L) // 2]), triFusion(L[len(L) // 2:]))


def fusion(A, B):
    if len(A) == 0:
        return B
    elif len(B) == 0:
        return A
    elif A[0] <= B[0]:
        return [A[0]] + fusion(A[1:], B)
    else:
        return [B[0]] + fusion(A, B[1:])


def trier_ensembles_sommes(cliques):
    global answer
    somme = []
    for clique in cliques:
        somme.append(sum(clique))

    somme_triee = triFusion(somme)

    return somme_triee


def main(args):
    sys.setrecursionlimit(9999999)
    # tester dfs
    # adjacence = {
    #     1 : [2,3,4],
    #     2 : [1,3,4],
    #     3 : [1,2,4],
    #     4 : [1,2,3],
    #     5 : [6,4,2],
    #     6 : [5]
    # }
    # cliquesExistantes = []
    # cliquesTest = cliqueBacktrack(cliquesExistantes, adjacence, 1, [1], {1})
    # print(trier_ensembles_sommes(cliquesTest)[0])

    # # on check pour clique 
    # # continue until desired solution found: un ensemble spécial 
    neme_elem = 3
    # construction du graphe
    edges = [];
    adj = {}
    n = 3;
    adj[3] = [];
    primes = [3]
    reponse = 0
    solution = False
    cliquesExistantes = []
    listeSommes = []

    # rouler le problème 
    # while not solution:
    #     b = nextPrime(n)
    #     primes.append(b)
    #     adj[b] = []
    #     # voir la relation de ce nouveau nb premier avec les autres dans le graphe
    #     for p in primes:
    #         if testPaireSpeciale(p, b) and p != b:
    #             # ajouter l'arête
    #             if b == 1871:
    #                 print('yes2')
    #             edges.append([b, p])
    #             edges.append([p, b])
    #
    #             adj[b].append(p)
    #             adj[p].append(b)
    #     # trouve toutes les cliques de taille 4 une fois qu'on a ajouté un nouveau sommet/arêtes
    #     if b == 827:
    #         print('yes')
    #     if b == 1871:
    #         print('yes2')
    #     cliquesUpdated, visited = cliqueBacktrack([], adj, b, [b], {b})
    #
    #     # on a trouvé une clique
    #     if cliquesUpdated not in cliquesExistantes:
    #         if len(cliquesExistantes) == 0:
    #             cliquesExistantes = cliquesUpdated
    #         elif len(cliquesUpdated) > 0:
    #             cliquesExistantes.append(cliquesUpdated[0])
    #         print(len(cliquesExistantes))
    #
    #     # faire l'ensemble des sommes
    #     if len(cliquesExistantes) == 100:
    #         listeSommes = trier_ensembles_sommes(cliquesExistantes)
    #         reponse = listeSommes[neme_elem - 1]
    #         solution = True
    #
    #     n = b
        # regarder toutes les cliques d'avant et si on a add une clique, calculer sa somme et l'ajouter à la liste de sommes
        # check w/taille de la clique
        # if len(listeSommes) == neme_elem:
        #     reponse = listeSommes[neme_elem]
        #     solution = True


    #Version Sam
    nombre_de_permiers_dans_graphe = 780
    for _ in range(nombre_de_permiers_dans_graphe):
        b = nextPrime(n)
        primes.append(b)
        adj[b] = []
        n = b
    # voir la relation de ce nouveau nb premier avec les autres dans le graphe

    # SAM : Ici on ajoute toutes les arretes d'un seul coup, backtrack plus facile
    for prime1 in range(len(primes)):
        for prime2 in range(prime1 + 1, len(primes)):
            p = primes[prime1]
            b = primes[prime2]

            if testPaireSpeciale(p, b) and p != b:
                # ajouter l'arête
                edges.append([b, p])
                edges.append([p, b])
                adj[b].append(p)
                adj[p].append(b)


    count = 0
    # trouve toutes les cliques de taille 4 une fois qu'on a ajoute toutes les nodes
    for p in primes:
        print(count)
        count += 1
        cliqueBacktrack(cliquesExistantes, adj, p, [p])

    # faire l'ensemble des sommes
    #listeSommes = trier_ensembles_sommes(cliquesExistantes)
    listeSommes = []
    for clique in cliquesExistantes:
        curr = 0
        for elem in clique:
            curr += elem
        listeSommes.append(curr)

    listeSommes.sort()
    print(listeSommes)
    print(cliquesExistantes)
    print("POUR TESTS")
    print(listeSommes[0:3])
    print(listeSommes[6])
    print(listeSommes[25])


    reponse = listeSommes[neme_elem - 1]
    print(reponse)
    return reponse


# NE PAS TOUCHER
# DO NOT TOUCH
if __name__ == "__main__":
    main(sys.argv[1:])
