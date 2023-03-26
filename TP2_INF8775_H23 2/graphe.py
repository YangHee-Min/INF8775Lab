import math

class Graph:
    def __init__(self, coords):
        self.adj = {}
        self.nVertices = len(coords)
        for coord in coords: 
            self.adj[coord] = []
        
    def addCouple(self, p1, p2):
        self.adj[p1].append(p2)
        self.adj[p2].append(p1)
        
    def verifyCycle(self, p1, p2, visited):
        visited.append(p1)
        if p1[0] == p2[0] and p1[1] == p2[1]:
            return True
        if len(self.adj[p1]) > 0:
            for adjacent in self.adj[p1]: 
                if adjacent not in visited and self.verifyCycle(adjacent, p2, visited):
                    return True
        elif len(self.adj[p2]) > 0:
            for adjacent in self.adj[p2]: 
                if self.verifyCycle(adjacent, p1, visited):
                    return True
        return False
    
    def allNodesLinked(self):
        sumNode = 0
        for line in self.adj.values():
            sumNode += len(line)
            
        if sumNode/2 < (self.nVertices -1):
            return False
        else :
            return True
        
    def visitNode(self, coord, path):
        path.append(coord)
        for child in self.adj[coord]:
            if child not in path:
                path = self.visitNode(child, path)
        return path
        
def TSP(coords):
    return MST(coords)


def MST(coords):
    graph = Graph(coords)
    distances = {}
    
    for i in coords:
        for j in coords :
            if i != j :
                distance = math.dist(i, j)
                distances[distance] = (i,j)

    keylist = list(distances.keys())
    keylist.sort()
    
    for key in keylist:
        p1, p2 = distances[key]
        if not graph.verifyCycle(p1, p2, []) and not graph.allNodesLinked():
            graph.addCouple(p1, p2)
        if graph.allNodesLinked():
            firstNode = coords[0]
            returnPath = graph.visitNode(firstNode, [])
            return returnPath.append(returnPath[0])

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