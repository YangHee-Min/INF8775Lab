from PIL import Image, ImageDraw
from itertools import chain, combinations
import math

# https://stackoverflow.com/questions/1482308/how-to-get-all-subsets-of-a-set-powerset
def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

def getPreviousSubset(subset):
    allSubsets = powerset(subset)
    returnSubsets = []
    
    for subsets in allSubsets:
        if len(subsets) == len(subset)-1:
            returnSubsets.append(subsets)
    
    return returnSubsets


def TSP(coords):
    dynamic_array = {}
    starting_point = coords.pop(0)
    
    N = len(coords)
    
    # powerSet == index en j
    powerSet = powerset(coords)
    
    for point in coords: 
        dynamic_array[point] = [None * len(powerSet)]
    
    # pour chacun des subsets (gauche a droite)
    for subset in powerSet:
        # pour chacun des points (haut en bas)
        for point in list(dynamic_array.keys()):
            
            # si le point n'est pas dans le subset -> on le considere
            if point not in subset:
                
                # on trouve tous les subsets des grandeur len(subset) - 1
                possiblePaths = getPreviousSubset(subset)
                
                # declare une datastructure pour garder en memoire les distances possibles
                distances = {}
                
                # pour chacun des chemins possible
                for possiblePath in possiblePaths:
                    # on trouve le dernier point 
                    previousPoint = subset.difference(possiblePath)
                    # on trouve la distance du chemin possible
                    distance = dynamic_array[previousPoint][powerSet.index(possiblePath)]
                    previousPointToCurrent = math.dist(previousPoint, point)
                    
                    # on trouve la distance totale du chemin
                    totalDistance = distance + previousPointToCurrent
                    
                    possiblePath.append(previousPoint)
                    distance[totalDistance] = possiblePath
                
                
                    
                    
                    

        
if __name__ == "__main__":
    f = open("N50_0", "r")
    coords = []
    N = int(f.readline())
    print(f"N : {N} ")

    for i in range(N):
        line = f.readline()
        coords.append(tuple(int(coord) for coord in line.split("  ")))
    
    path = TSP(coords)
    print(len(path))
    
    
    