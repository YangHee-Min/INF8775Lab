"""
Fonction compareParHeuristique(n1:Nœud, n2:Nœud)
       si n1.heuristique < n2.heuristique 
           retourner 1
       ou si n1.heuristique == n2.heuristique 
           retourner 0
       sinon
           retourner -1

Fonction cheminPlusCourt(g:Graphe, objectif:Nœud, depart:Nœud)
       closedLists = File()
       openList = FilePrioritaire(comparateur = compareParHeuristique)
       openList.ajouter(depart)
       tant que openList n'est pas vide
           u = openList.defiler() 
           si u.x == objectif.x et u.y == objectif.y
               reconstituerChemin(u)
               terminer le programme
           pour chaque voisin v de u dans g
               si non(   v existe dans closedLists 
                            ou v existe dans openList avec un coût inférieur)
                    v.cout = u.cout +1 
                    v.heuristique = v.cout + distance([v.x, v.y], [objectif.x, objectif.y])
                    openLists.ajouter(v)
           closedLists.ajouter(u)
       terminer le programme (avec erreur)
"""

"""
IDEES D'ANALYSE
    -> ON PREND L'ENCLOS AVEC LA PLUS GRANDE SUPERFICIE
    -> ON CHERCHE DE MANIERE ALEATOIRE UNE CASE DE CET ENCLOS
    
        -> PT ON PREND LE PREMIER ENCLOS QUE L'ON TROUVE??
    
    -> ENSUITE ON CHERCHE TOUTES LES DISTANCES AVEC LES ENCLOS 
    
    -> EN TROUVANT LES DISTANCES AVEC LES ENCLOS, ON TROUVE AUSSI UN COTE DE L'ENCLOS VOISIN
"""

def getVoisins(x, y, longeurMax):
    returnList = []
    
    x_1 = x-1
    x_2 = x+1
    y_1 = y-1
    y_2 = y+1

    if x_1 >= 0:
        returnList.append((x_1, y))
    if x_2 < longeurMax:
        returnList.append((x_2, y))
    if y_1 >= 0:
        returnList.append((x, y_1))
    if y_2 < longeurMax:
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
    couleurInit = graph[nouveauContour[0][0]][nouveauContour[0][1]]
    
    noeudVisiter = []
    contoursDepart = []
    
    distance = 0
    while True:
        contoursDepart = nouveauContour
        nouveauContour = []
        while len(contoursDepart)> 0:
            noeud = contoursDepart.pop();
            
            valeur = graph[noeud[0]][noeud[1]]
            if ((valeur not in distances.keys()) and (valeur is not couleurInit) and (valeur is not None)):
                distances[valeur]= distance
            
            voisins = getVoisins(noeud[0], noeud[1], len(graph))
            for voisin in voisins:
                if not ((voisin in noeudVisiter) or (voisin in nouveauContour) or (graph[voisin[0]][voisin[1]] == couleurInit)):
                    nouveauContour.append(voisin)
        distance += 1

        if len(distances.keys())==n-1:
            return distances
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
    couleurInitiale = graph[start[0]][start[1]]    

    while len(noeudAVisiter)>0:
        u = noeudAVisiter.pop()
        voisins = getVoisins(u[1], u[0], len(graph[0]))
        for voisin in voisins: 
            if ((graph[voisin[0]][voisin[1]] != couleurInitiale) and (u not in contours)):
                contours.append(u)
            if((graph[voisin[0]][voisin[1]] == couleurInitiale) and (voisin not in noeudVisiter) and (voisin not in noeudAVisiter)):
                noeudAVisiter.append(voisin)
            elif voisin not in noeudVisiter:
                noeudVisiter.append(voisin)
        noeudVisiter.append(u)
    return contours