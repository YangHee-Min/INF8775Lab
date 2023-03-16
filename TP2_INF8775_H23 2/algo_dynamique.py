from PIL import Image, ImageDraw
from itertools import chain, combinations

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
    
    for subset in powerSet:
        for point in list(dynamic_array.keys()):
            if point not in subset:
                possiblePaths = getPreviousSubset(subset)
                distances = {}
                for possiblePath in possiblePaths:
                    previousPoint = subset.difference(possiblePath)
                    distance = dynamic_array[previousPoint][powerSet.index(possiblePath)]
        
        
    
    
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
    
    
    