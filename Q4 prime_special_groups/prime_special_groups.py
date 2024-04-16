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
    
def BTest(a, n):
    s = 0
    t = n-1
    while t%2 == 1:
        s += 1
        t /= 2
    x = (a**t)%n
    if x == 1 or x == n-1 :
        return True
    for i in range (1, s): # should be s-1 but s bc i stops at the index before the end
        x = (x**2)%n
        if x == n-1:
            return True
    return False

# trouve le prochain nombre premier
def nextPrime(n):
    isPrime = False
    i = n
    while not isPrime:
        n += 1
        isPrime = BTest(i)
    return i #the next prime

def main(args):
    n = int(args[0])
    output_file = args[1]

    # 1 <= n <= 100
    # TODO: calculer la sommme du n-ème ensemble spécial
    
    # TODO: obtenir les nombres premiers
    # on sait deja que ca commence à 3
    # if n < 3,825,123,056,546,413,051, it is enough to test a = 2, 3, 5, 7, 11, 13, 17, 19, and 23
    # https://www.wikiwand.com/en/Miller%E2%80%93Rabin_primality_test
    # donc :
    tabA = [2, 3, 5, 7, 11, 13, 17, 19, 23]
    
    # à partir de 3, just do next prime to go to the next prime number instead of iterating through each integer ever
    # or maybe no need and i can just call isPrime every time
    # par contre i can already skip every even integer which cuts the time off by a lot, same for multiples of 5
    
    # every time the sum returned is a prime number incrémente le n
    answer = 0

    # answering
    write(output_file, str(answer))

    

# NE PAS TOUCHER
# DO NOT TOUCH
if __name__ == "__main__":
    main(sys.argv[1:])
