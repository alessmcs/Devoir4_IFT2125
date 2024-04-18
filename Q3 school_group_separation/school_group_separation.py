#Nom, matricule
#Nom, matricule

import sys


#Fonction pour lire le fichier d'input. Vous ne deviez pas avoir besoin de la modifier.
#Retourne la liste des noms d'étudiants (students) et la liste des paires qui ne peuvent
#doivent pas être mis dans le même groupe (pairs)
#
#Function to read the input file. You shouldn't have to modify it.
#Returns the list of student names (students) and the list of pairs of students that
#shouldn't be put in the same group (pairs)
def read(fileName):
    # lecture du fichier
    fileIn = open(fileName,"r")
    linesIn = fileIn.readlines()
    fileIn.close()

    nbStudents = int(linesIn[0])
    students = []
    if(nbStudents != 0):
        students = [s.strip() for s in linesIn[1:nbStudents+1]]
    nbPairs = int(linesIn[nbStudents+1])
    pairs = []
    if(nbPairs != 0):
        pairs = [s.strip().split() for s in linesIn[nbStudents+2:nbStudents+nbPairs+2]]

    return students, pairs

#Fonction qui écrit dans le fichier d'output.
#le paramètre content est un string
def write(fileName, content):
    Outputfile = open(fileName, "w")
    Outputfile.write(content)
    Outputfile.close()

#Fonction principale à compléter.

# students : liste des noms des étudiants
# pairs : liste des paires d'étudiants à ne pas grouper ensemble
#         chaque paire est sous format de liste [x, y]

#Valeur de retour : string contenant la réponse. Si c'est impossible, retourner "impossible"
#                   Sinon, retourner en un string les deux lignes représentant les
#                   les deux groupes d'étudants (les étudiants sont séparés par des
#                   espaces et les deux lignes séparées par un \n)
class Node :
    def __init__(self, valeur, liste_voisins, couleur=None):
        self.couleur = couleur
        self.valeur = valeur
        self.liste_voisins = []

    def add_voisin(self, voisin):
        if voisin not in self.liste_voisins :
            self.liste_voisins.append(voisin)


def init_graphe(students):
    noeuds = []
    for i in range(len(students)) :
        noeuds.append(Node(students[i], []))
    return noeuds

def noeud_recherche(trouve, noeuds) :
    for node in noeuds :
        if node.valeur == trouve :
            return node
def connexion(noeuds, pairs) :
    for i in range(len(pairs)) :
        for node in noeuds :
            if pairs[i][0] == node.valeur :
                node.add_voisin(noeud_recherche(pairs[i][1],noeuds))
            elif pairs[i][1] == node.valeur :
                node.add_voisin(noeud_recherche(pairs[i][0], noeuds))

def colorier(node, voisin) :
    if node.couleur == 'Rouge' :
        voisin.couleur = 'Bleu'

    elif node.couleur == 'Bleu' :
        voisin.couleur = 'Rouge'

def coloriage(node, visited) :
    visited.add(node)
    if node.liste_voisins != [] :
        for voisin in node.liste_voisins :
            if voisin not in visited:
                colorier(node, voisin)
                coloriage(voisin, visited)

def createGroups(students, pairs):
    noeuds = init_graphe(students)
    connexion(noeuds, pairs)

    visited = set()
    groupe1 = []
    groupe2 = []
    for node in noeuds :
        if node not in visited:
            node.couleur = 'Rouge'
            coloriage(node, visited)
        if node.couleur == 'Rouge' or node.couleur == None :
            groupe1.append(node.valeur)

        elif node.couleur == 'Bleu' :
            groupe2.append(node.valeur)

    return groupe1, groupe2


#Normalement, vous ne devriez pas avoir à modifier

def main(args):
    #input_file = args[0]
    #output_file = args[1]
    input_file = "input0.txt"

    output_file = "output.txt"
    students, pairs = read(input_file)
    output, output_bis = createGroups(students, pairs)
    write(output_file, ' '.join(output)+ '\n')

    with open(output_file, 'a') as file:
        write(output_file, ' '.join(output_bis))


#Ne pas changer
#Don't change
if __name__ == '__main__':
    main(sys.argv[1:])