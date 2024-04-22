#Nom, Matricule
#Nom, Matricule

import math
import random 
import sys

def write(fileName, content):
    """Écrire la sortie dans un fichier/write output in file"""
    file = open(fileName, "w")
    file.write(content)
    file.close()

# faire de l'exponentiation modulaire 
def expoMod(a,t,n):
    res = 1
    a = a%n
    while (t > 0): 
        if (t & 1):
            res = (res*a) % n
        t = t>>1
        a = (a*a)%n
    return res

# GeeksForGeeks & wikipedia 
def millerRabin(t, n):
     # choix de a, selon le critère de Miller 
    a = 0
    while not( 1 <= a <= n-2):
        # if n < 3,825,123,056,546,413,051, it is enough to test a = 2, 3, 5, 7, 11, 13, 17, 19, and 23
        # https://www.wikiwand.com/en/Miller%E2%80%93Rabin_primality_test
        tabA = [2, 3, 5, 7, 11, 13, 17, 19, 23]
        randIndex = random.randrange(0, len(tabA)-1)
        a = tabA[randIndex]

    x = expoMod(a,t,n)

    if (x == 1 or x == n - 1):
        return True
    
    while (t != n - 1):
        x = ( x * x ) % n
        t *= 2
        if (x == 1):
            return False; 
        if (x == n-1):
            return True
    
    return False

# test tiré de # https://www.geeksforgeeks.org/primality-test-set-3-miller-rabin/  
def BTest(n, k):

    # cas extrêmes 
    if (1 < n <= 3 or n == 5):
        return True 
    if (n <= 1 or n % 2 == 0 or n % 3 == 0 or n % 11 == 0):
        return False 
    
    t = n-1
    while (t%2 == 0):
        t //= 2
    
    # répéter miller-rabin plusieurs fois pour accuracy
    for i in range(k): 
        if (millerRabin(t,n) == False):
            return False
    
    return True

# trouve le prochain nombre premier
def nextPrime(n):
    isPrime = False
    i = n
    while not isPrime:
        i += 1
        isPrime = BTest(i, 4)
    return i #the next prime

# TODO: tester si a et b (nombres premiers) forment une paire spéciale 
def testPaireSpeciale(a,b):
    # tester toutes les permutations possibles entre les 2 nombres et voir si chaque résultat est un nombre premier 
    # utiliser la fonction pour generer les permutations quon a fait dans le devoir 2 
    # & check pour chaque permutation si elle est premiere
    # si une perm n'est pas première, return false direct ce n'est pas une paire spéciale 
    permutations = generate_permutation(int(str(a) + str(b)))
    for p in permutations: 
        totalString = '' 
        for i in p: 
            totalString += i
        
        if not BTest(int(totalString), 4): 
            return False # ce n'est pas une paire spéciale 

    # c'est une paire spéciale
    return True

# selon la fonction en c++ qu'on a implémenté dans le devoir 2
# https://stackoverflow.com/questions/4223349/python-implementation-for-next-permutation-in-stl

# TODO: fix permutation 
def generate_permutation(n):
    premier_str = str(n)

    tab_premier = []
    for letter in premier_str:
        tab_premier.append(letter)

    permutations = [list(tab_premier)]  

    while next_permutation(tab_premier):
        permutations.append(list(tab_premier))  
        
    return permutations

# https://pythonadventures.wordpress.com/2012/03/21/lexicographically-next-permutation/ 
# https://www.wikiwand.com/en/Permutation#Generation_in_lexicographic_order 
def next_permutation(tab):

    i = len(tab) - 2
    # find the largest index k such that tab[k] < tab[k+1]
    while not (i < 0 or tab[i] < tab[i+1]):
        i -= 1
    if i < 0:
        return False # if no such index return last permutation 

    j = len(tab) - 1
    # find the largest value k such that tab[k] < tab[l] 
    while not (tab[j] > tab[i]):
        j -= 1
    # swap the value of tab[i] with tab[j]
    tab[i], tab[j] = tab[j], tab[i]

    # reverse the sequence from tab[i+1] up to the end 
    tab[i+1:] = reversed(tab[i+1:])
    return True

def main(args):
    #n = int(args[0])
    #output_file = args[1]

    # 1 <= n <= 100
    # TODO: calculer la sommme du n-ème ensemble spécial

    # donc :
    # tab = generate_permutation(123)
    # print(tab)


    # k = 4; 
 
    # print("All primes smaller than 100: ")
    # for n in range(1,100):
    #     if (BTest(n, k)):
    #        print(n , end=" ")

    # regarder tous les nombres premiers
    solution = False 
    n = 3
    edges = []
    adj = [0]*3
    
    # # on trouve un nombre premier 
    # # on l'ajoute au graphe en le testant avec tous les autres nombres premiers pour add des arêtes
    # # on check pour clique 
    # # continue until desired solution found: un ensemble spécial 
    primes = [3]
    while not solution: 
        b = nextPrime(n)
        primes.append
        # voir la relation de ce nouveau nb premier avec les autres dans le graphe 
        # TODO: add every prime to the graph or only the ones that are special??
        for p in primes:
            if testPaireSpeciale(p,b):
                # ajouter l'arête
                edges.append([b,p])
                edges.append([p,b])
                adj[p].append(b)
            # TODO; après avoir add le nombre, check s'il y a une clique speciale 
            n = b
        else:  # si n pas premier, passer au prochain 
            n += 1

    print(testPaireSpeciale(67, 3))
    # TODO: fix test paire speciale bc its not working apparentlty

    
    # TODO: find a smarter way to calculate primes so you dont have to start at 0 every time 
    
    # les mettre dans la liste d'adjacence (créer une arête si 2 nombres font une paire spéciale - donc faire un test pour voir s'ils forment une paire speciale )
    #  https://www.geeksforgeeks.org/print-adjacency-list-for-a-directed-graph/ 






    #answer = 0

    # answering
    #write(output_file, str(answer))
    return

    def deep_first_search(node, clique, adjacence, visited) :
        visited.add(node)
        clique.add(node)
        for voisin in adjacence[node] :
            if voisin not in visited :
                deep_first_search(voisin, clique, adjacence, visited)

    def clique_4_premier(adjacence) :
        cliques = []
        visited = set()

        for node in adjacence :
            if node not in visited :
                clique = set()
                deep_first_search(node, clique, adjacence, visited)
                if len(clique) == 4:
                    cliques.append(clique)

        return cliques

    # https://fr.wikipedia.org/wiki/Tri_fusion#Algorithme
    def triFusion(L):
        if len(L) == 1:
            return L
        else:
            return fusion( triFusion(L[:len(L)//2]) , triFusion(L[len(L)//2:]) )

    def fusion(A,B):
        if len(A) == 0:
            return B
        elif len(B) == 0:
            return A
        elif A[0] <= B[0]:
            return [A[0]] + fusion( A[1:] , B )
        else:
            return [B[0]] + fusion( A , B[1:] )


    def trier_ensembles_sommes(cliques, n) :
        global answer
        dict = {}
        somme = []
        for clique in cliques :
            somme.append(sum(clique))
            dict[sum(clique)] = clique

        somme_triee = triFusion(somme)

        return somme_triee[n]
    

# NE PAS TOUCHER
# DO NOT TOUCH
if __name__ == "__main__":
    main(sys.argv[1:])
