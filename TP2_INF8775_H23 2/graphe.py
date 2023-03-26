import math

def TSP(coords):
    mst = build_MST(coords)
    path = evaluate_node(list(mst.keys())[0], mst, [])
    path.append(path[0])
    return path

def evaluate_node(child, tree, path):
    if child not in path: 
        path.append(child)
        childs = list(tree[child])
        for newChild in childs:
            path = evaluate_node(newChild, tree, path)   
        # Connection bi directionnelle 
        for point, childs in tree.items():
            if child in childs and point not in path:
                path = evaluate_node(point, tree, path)
    return path


def find_roots(tree, node, parents):
    for point, childs in tree.items():
        if node in childs:
            parents.append(point)
            parents = find_roots(tree, point, parents)
    return parents

def contains_common_elements(a, b):
    result = [i for i in a if i in b]
    return len(result) > 0


def is_cycling(tree, i, j):
    # check root of each child 
    for child in tree[i]:
        if contains_common_elements(find_roots(tree, j, []), find_roots(tree, child, [])):
            return True
    # check root of every parent
    if contains_common_elements(find_roots(tree, j, []),find_roots(tree, i, [])):
        return True
    return False
    

def build_MST(coords):
    distances = {}
    # get all the distances possibles
    for i in coords:
        for j in coords :
            if i != j :
                distance = math.dist(i, j)
                distances[distance] = (i,j)
    # Keep only the good ones
    MST = {}
    keylist = list(distances.keys())
    keylist.sort()
 
    for k,key in enumerate(keylist):
        i, j = distances[key]
        if i in MST and j in MST:
            # check loop
            if not is_cycling(MST, i, j) and not is_cycling(MST, j, i):
                MST[i].append(j)
            else:
                continue
        elif i in MST.keys():
            MST[i].append(j) 
            MST[j] = []
        elif j in MST.keys(): 
            MST[j].append(i)
            MST[i] = []
        else:
            MST[i] = []
            MST[i].append(j)
            MST[j] = []
    return MST
    

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