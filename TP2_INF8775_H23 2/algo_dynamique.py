from PIL import Image, ImageDraw
from itertools import chain, combinations
import math
import time

# https://stackoverflow.com/questions/1482308/how-to-get-all-subsets-of-a-set-powerset


def generatePowerset(s):
    if not s:
        return [[]]
    else:
        subsets = generatePowerset(s[1:])
        return subsets + [[s[0]] + subset for subset in subsets]

def powerset(s):
    setGen = generatePowerset(s)
    returnArray = []
    
    for generated in setGen:
        if len(generated) > 1:
            returnArray.append(sorted(generated))
        else :
            returnArray.append(generated)

    returnArray.sort(key=len)

    return returnArray


def getPreviousSubset(subset):
    allSubsets = powerset(subset)
    returnSubsets = []

    for subsets in allSubsets:
        if len(subsets) == len(subset)-1:
            returnSubsets.append(sorted(subsets))

    return returnSubsets


def difference(listA, listB):
    setA = set(listA)
    setB = set(listB)
    return setA.difference(setB).pop()


def TSP(coords):
    dynamic_array = {}
    path = []
    
    starting_point = coords.pop(0)
    N = len(coords)

    precedingNode = dict()

    # powerSet == index en j
    powerSet = powerset(coords)
    
    for point in coords:
        dynamic_array[point] = [None] * len(powerSet)
    time0 = time.time()
    # pour chacun des subsets (gauche a droite)
    for subset in powerSet:    
        time1 = time.time()
        # pour chacun des points (haut en bas)
        for point in list(dynamic_array.keys()):
            
            # Si on est dans la premiere colone
            if len(subset) == 0:
                dynamic_array[point][0] = math.dist(starting_point, point)
                continue
            
            # si le point n'est pas dans le subset -> on le considere
            if point not in subset:
                
                # on trouve tous les subsets des grandeur len(subset) - 1
                possiblePaths = getPreviousSubset(subset)

                # declare une datastructure pour garder en memoire les distances possibles
                distances = {}

                # pour chacun des chemins possible
                for possiblePath in possiblePaths:
                    # on trouve le dernier point
                    previousPoint = difference(subset, possiblePath)
                    # on trouve la distance du chemin possible
                    distance = dynamic_array[previousPoint][powerSet.index(possiblePath)]
                    previousPointToCurrent = math.dist(previousPoint, point)

                    # on trouve la distance totale du chemin
                    totalDistance = distance + previousPointToCurrent

                    possiblePath.append(previousPoint)
                    distances[previousPoint] = totalDistance
                
                if len(distances) > 0:
                    for possiblePoint, distance in distances.items():
                        if distance == min(distances.values()):
                            dynamic_array[point][powerSet.index(subset)] = distance
                            precedingNode[powerSet.index(subset)] = possiblePoint   
                                             
        print("Temps pour executer la colone ", powerSet.index(subset), " : ", time.time() - time1)
    if len(subset) == N:
        returnPath = [starting_point]

        # pour chacun des chemins possible
        for possiblePath in possiblePaths:
            possiblePath = sorted(possiblePath)
            # on trouve le dernier point
            previousPoint = difference(subset, possiblePath)
            # on trouve la distance du chemin possible
            distance = dynamic_array[previousPoint][powerSet.index(possiblePath)]
            previousPointToCurrent = math.dist(previousPoint, point)

            # on trouve la distance totale du chemin
            totalDistance = distance + previousPointToCurrent

            possiblePath.append(previousPoint)
            distances[previousPoint] = totalDistance
                
        if len(distances) > 0:
            for possiblePoint, distance in distances.items():
                if distance == min(distances.values()):
                    dynamic_array[point][powerSet.index(subset)] = distance
                    precedingNode[powerSet.index(subset)] = possiblePoint

        while len(returnPath) < N+1:
            previousPoint = precedingNode[powerSet.index(subset)]
            returnPath.append(previousPoint)
            subset.remove(previousPoint)
        
        returnPath.append(starting_point)
        returnPath.reverse()
        
        print("Temps pour executer ", N, " villes : ", time.time()-time0)
        return returnPath
    

if __name__ == "__main__":
    f = open("N5_0", "r")
    coords = []
    N = int(f.readline())
    print(f"N : {N} ")

    for i in range(N):
        line = f.readline()
        coords.append(tuple(int(coord) for coord in line.split("  ")))

    path = TSP(coords)
    print(path)
    print(len(path))
