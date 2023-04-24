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


class Island:
    def __init__(self, grid, n):
        self.grid = grid
        self.n = n
        self.enclos = dict()
        self.distances = [[None for j in range(n)] for i in range(n)]
        
        for i in range(n):
            self.enclos[i] = []
    
    def __findIslands(self):
        for y in range(len(self.grid)):
            for x in range(len(self.grid[0])):
                if self.grid[x][y] != None:
                    self.enclos[self.grid[x][y]].append((x, y))
    
    def findAllDistances(self):
        self.__findIslands()
        
        for i in range(self.n):
            for j in range(self.n):
                if i == j:
                    self.distances[i][j] = 0
                else :
                    distance = findDistance(self.enclos[i], self.enclos[j])
                    self.distances[i][j] = distance
                    self.distances[j][i] = distance
        return self.distances
                
    
if __name__ =='__main__':
    #filename =  "/Users/charles-antoinelaurin/depot_distant/H23/INF8775Lab/tp3/TP3-H23/n100_m50_V-8613404.txt"
    #(enc_count, m_set_count, min_dist, id_to_size, weights, _) = read_file(filename)
    
    #table = generate_enclosures(id_to_size)
    #print_table(table)
    
    graph = [
                [4, None, None, None, 1, 1, 1],
                [4, None, None, None, 1, 1, None],
                [4, 0, 2, 2, 2, 2, 2],
                [4, 0, 2, 2, 2, 2, 2],
                [4, 0, 2, 2, 2, 2, 2],
                [4, 3, 3, 3, 3, 3, 3],
                [4, 4, 4, 4, 4, 4, 4]
            ]
    
    print_table(graph)
    islands = Island(graph, 5)
    distances = islands.findAllDistances()
    
    for line in distances:
        print(line)
    
    
    
    