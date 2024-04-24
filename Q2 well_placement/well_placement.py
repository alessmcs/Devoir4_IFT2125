# Alessandra MANCAS, 20249098
# Océane Hays (20240742)

import sys

def read_problem(input_file):
    """Fonctions pour lire/écrire dans les fichier. Vous pouvez les modifier,
    faire du parsing, rajouter une valeur de retour, mais n'utilisez pas
    d'autres librairies.
    Functions to read/write in files. you can modify them, do some parsing,
    add a return value, but don't use other librairies"""

    # lecture du fichier/file reading
    file = open(input_file, "r")
    lines = file.readlines()

    # traiter les lignes du fichier pour le problème
    # process the file lines for the problem
    lignes = []
    uneLigne = []
    for l in lines: 
        for i in l:
            if i != "\n" and i != " ":
                uneLigne.append(i)
        lignes.append(uneLigne)
        uneLigne = []
    
    file.close()
    return lignes

def lireTerrain(terrain):
    meilleureSomme = 0
    for i in range(len(terrain)):
        if '1' in  terrain[i]:
            for j in range(len(terrain[0])):
                if terrain[i][j] == '1' : 
                    # bfs est plus rapide que dfs lorsque le graphe est très large
                    tempSomme = bfs(terrain, i, j)
                    if tempSomme > meilleureSomme:
                        meilleureSomme = tempSomme
    return meilleureSomme

def calculerAdj(terrain,x,y):
    adj = []
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(terrain) and 0 <= ny < len(terrain[0]) and terrain[nx][ny] == '1':
            adj.append([terrain[nx][ny], nx, ny])
    return adj

# implémenter le pseudocode vu en classe 
def bfs(terrain,x,y):
    queue = []
    queue.append([terrain[x][y],x,y]) # push root 
    somme = 0

    while queue: 
        s = tuple(queue.pop())
        x = s[1]
        y = s[2]
        adj = calculerAdj(terrain, x, y) 
        for a in adj:
            if a[0] == '1':
                queue.append(a)
        if terrain[x][y] == '1':
            terrain[x][y] = '1v'
            somme += 1
    return somme


def write(fileName, content):
    """Écrire la sortie dans un fichier/write output in file"""
    file = open(fileName, "w")
    file.write(content)
    file.close()


def main(args):
    """Fonction main/Main function"""
    input_file = args[0]
    output_file = args[1]
    lignes = read_problem(input_file)

    terrain = lignes[1:] # terrain est le reste de lignes

    # lire le terrain ligne par ligne et voir les 1 dans le voisinage des 1s
    resultat = lireTerrain(terrain)
    print(resultat)

    write(output_file, str(resultat))

# NE PAS TOUCHER
# DO NOT TOUCH
if __name__ == "__main__":
    main(sys.argv[1:])