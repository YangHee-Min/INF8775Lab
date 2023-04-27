from gen_enc import read_file, generate_enclosures, print_table

# https://www.geeksforgeeks.org/distance-between-closest-pair-of-islands/


def findDistance(island1, island2):
    dist = float('inf')
    for i in range(len(island1)):
        point1 = island1[i]
        for j in range(len(island2)):
            point2 = island2[j]
            distp1p2 = abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])
            dist = min(dist, distp1p2)
    return dist


class CalculDistance:
    def __init__(self, grid, n):
        self.grid = grid
        self.n = n
        self.enclos = dict()
        self.distances = [[None for j in range(n)] for i in range(n)]

        for i in range(n):
            self.enclos[i] = []
        
    def getVoisins(self, x, y):
        longueurMaxX = len(self.grid[0])
        longueurMaxY = len(self.grid)
        
        returnList = []
    
        x_1 = x-1
        x_2 = x+1
        y_1 = y-1
        y_2 = y+1

        if x_1 >= 0:
            returnList.append((x_1, y))
        if x_2 < longueurMaxX:
            returnList.append((x_2, y))
        if y_1 >= 0:
            returnList.append((x, y_1))
        if y_2 < longueurMaxY:
            returnList.append((x, y_2))
        return returnList
    

    def isExtremite(self, x, y):
        value = self.grid[y][x]
        voisins = self.getVoisins(x, y)
        
        for voisin in voisins: 
            if self.grid[voisin[1]][voisin[0]] != value:
                return True
        
        return False
    
    def __trouverEnclos(self):
        for y in range(len(self.grid)):
            for x in range(len(self.grid[0])):
                if self.grid[y][x] != None and self.isExtremite(x, y):
                    self.enclos[self.grid[y][x]].append((x, y))
    
    def findAllDistances(self):
        self.__trouverEnclos()
        for i in range(self.n):
            for j in range(i+1, self.n):
                distance = findDistance(self.enclos[i], self.enclos[j])
                self.distances[i][j] = distance
                self.distances[j][i] = distance
                    
        return self.distances


if __name__ == '__main__':
    # filename =  "/Users/charles-antoinelaurin/depot_distant/H23/INF8775Lab/tp3/TP3-H23/n100_m50_V-8613404.txt"
    # (enc_count, m_set_count, min_dist, id_to_size, weights, _) = read_file(filename)

    # table = generate_enclosures(id_to_size)
    # print_table(table)

    graph = [
        [4, None, None, None, 1, 1, 1, None],
        [4, None, None, None, 1, 1, None, None],
        [4, 0, 2, 2, 2, 2, 2, None],
        [4, 0, 2, 2, 2, 2, 2, None],
        [4, 0, 2, 2, 2, 2, 2, None],
        [4, 3, 3, 3, 3, 3, 3, None],
        [4, 4, 4, 4, 4, 4, 4, None]
    ]

    print_table(graph)
    islands = Island(graph, 5)
    distances = islands.findAllDistances()

    for line in distances:
        print(line)
