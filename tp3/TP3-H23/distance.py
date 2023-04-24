import random
from gen_enc import read_file, generate_enclosures, print_table

def getVoisins(x, y, longeurMaxX, longeurMaxY):
    returnList = []
    
    x_1 = x-1
    x_2 = x+1
    y_1 = y-1
    y_2 = y+1

    if x_1 >= 0:
        returnList.append((x_1, y))
    if x_2 < longeurMaxX:
        returnList.append((x_2, y))
    if y_1 >= 0:
        returnList.append((x, y_1))
    if y_2 < longeurMaxY:
        returnList.append((x, y_2))
    return returnList

"""
PSEUDO CODE

graphe 
contourDepart = []
Fonction cheminPlusCourt(g:Graphe, contourDepart: [])
    noeudsVisiter = []

    nouveauContours = liste FIFO 
    contourDepart -> nouveauContours
    distancesAvecNoeud = map<id-> distance>
    distance = 0

    while True: 
        pour chaque noeud dans nouveauContours: 
            si id noeud pas dans distanceAvecNoeud:
                ajouter <id, distance> -> distancesAvecNoeud
            
            pour chaque voisin de noeud :
                if not (voisin in noeudsVisiter or voisin in nouveauContour or graphe[voisin] == originalId):
                    ajouter voisin -> nouveauContoursasd
    
    Si toutes les distances recceuillis -> return distances
"""
def findAllShortestPath(graph, nouveauContour, n):
    distances = dict()
    couleurInit = graph[nouveauContour[0][1]][nouveauContour[0][0]]

    noeudVisiter = []
    contoursDepart = []
    distance = 0
    
    while len(nouveauContour) > 0:
        contoursDepart = nouveauContour
        nouveauContour = []
        
        while len(contoursDepart)> 0:
            noeud = contoursDepart.pop();
            valeur = graph[noeud[1]][noeud[0]]
            
            if ((valeur not in distances.keys()) and (valeur is not couleurInit) and (valeur is not None)):
                distances[valeur] = distance
                if len(distances.keys())==n-1:
                    return distances
            
            voisins = getVoisins(noeud[0], noeud[1], len(graph[0]), len(graph))
            for voisin in voisins:
                if not ((voisin in noeudVisiter) or (voisin in nouveauContour)):
                    nouveauContour.append(voisin)
            
            noeudVisiter.append(noeud)
        distance +=1
"""
TROUVER LES CONTOURS DES ENCLOS

Fonction trouverContours(g:graphe, depart:(x, y)):
    closedList = [] # tous les noeuds consituant un contours 
    openList = fifo # tous les noeuds a visiter
    openlist.add(depart)
    
    while openList not empty:
        u = openlist.defiler()
        si calculerNbVoisin(u) <= 4 
            closedList.ajouter(u)
        sinon 
            pour chacun des voisins
                si (pas dans open ni dans close list et que c'est le meme type d'enclos)
                    openList.add(voisin)
    
    return closedList
"""

def findContours(graph, start):
    contours = []
    noeudAVisiter = [start]
    noeudVisiter = []
    couleurInitiale = graph[start[1]][start[0]]   

    while len(noeudAVisiter)>0:
        u = noeudAVisiter.pop()
        voisins = getVoisins(u[0], u[1], len(graph[0]), len(graph))

        for voisin in voisins: 
            if ((graph[voisin[1]][voisin[0]] != couleurInitiale) and (u not in contours)):
                contours.append(u)
            elif ((graph[voisin[1]][voisin[0]] == couleurInitiale) and (voisin not in noeudVisiter) and (voisin not in noeudAVisiter)):
                noeudAVisiter.append(voisin)

        noeudVisiter.append(u)
    return contours


def findEnclos(graph, index):
    noeudAVisiter = []
    noeudVisiter = []
    
    noeudInit = (random.randint(0, len(graph)-1), random.randint(0, len(graph[0])-1))
    
    noeudAVisiter.append(noeudInit)
    
    while len(noeudAVisiter) > 0:
        u = noeudAVisiter.pop()
        
        if graph[u[1]][u[0]] == index:
            return u
        
        voisins = getVoisins(u[1], u[0], len(graph[0]), len(graph))
        for voisin in voisins: 
            if ((voisin not in noeudVisiter) or (voisin not in noeudAVisiter)):
                noeudAVisiter.append(voisin)
        
        noeudVisiter.append(u)
        
                
def findAllDistances(graph, n):
    allDistances = {}
    for i in range(n):
        enclos = findEnclos(graph, i)
        contours = findContours(graph, enclos)
        shortestPaths = findAllShortestPath(graph, contours, n)
        allDistances[i] = shortestPaths
        
    for i in allDistances.keys():
        print(i, "  : ", allDistances[i])
        print("\n******************")
    
    return allDistances
        
    
if __name__ == '__main__':
    filename =  "/Users/charles-antoinelaurin/depot_distant/H23/INF8775Lab/tp3/TP3-H23/n20_m15_V-74779.txt"
    (enc_count, m_set_count, min_dist, id_to_size, weights) = read_file(filename)
    
    table = generate_enclosures(id_to_size)
    print_table(table)
    
    findAllDistances(table, enc_count)
    