import unittest 
from distance import *

GRAPH = [[4, None, None, None, 1, 1, 1],
[4, None, None, None, 1, 1, None],
[4, None, 2, 2, 2, 2, 2],
[4, None, 2, 2, 2, 2, 2],
[4, None, 2, 2, 2, 2, 2],
[4, 3, 3, 3, 3, 3, 3],
[4, 4, 4, 4, 4, 4, 4]]



class TestStringMethods(unittest.TestCase):
    
    def __init__(self, methodName: str = "runTest"):
        super().__init__(methodName)
        filename =  "/Users/charles-antoinelaurin/depot_distant/H23/INF8775Lab/tp3/TP3-H23/n20_m15_V-74779.txt"
        (enc_count, m_set_count, min_dist, id_to_size, weights) = read_file(filename)
        table = generate_enclosures(id_to_size)
        self.graph = table
        self.n = enc_count
    
    def test_find_voisin(self):
        voisins = getVoisins(6, 0, len(self.graph[0]), len(self.graph))
        print(voisins)
        

    def test_find_contours(self):
        contours = findContours(self.graph, (3, 3))
        contours.sort()
        print(contours)
    
    """
    def test_find_contours2(self):
        filename =  "/Users/charles-antoinelaurin/depot_distant/H23/INF8775Lab/tp3/TP3-H23/n20_m15_V-74779.txt"
        (enc_count, m_set_count, min_dist, id_to_size, weights) = read_file(filename)
        table = generate_enclosures(id_to_size)
        
        debugMatrix = []
        for line in table:
            newLine = []
            for elem in table[0]:
                newLine.append(None)
            debugMatrix.append(newLine)
        
        for i in range(enc_count):
            enclos = findEnclos(table, i)
            contours = findContours(table, enclos)
        
            for point in contours:
                self.assertEqual(table[point[1]][point[0]], i)
                debugMatrix[point[1]][point[0]] = i
            
            print_table(table)
            print_table(debugMatrix)  
    """
        
    def containsI(self, i):
        for line in self.graph:
                if i in line:
                    return True
        return False
    
    def test_generate(self):
        for i in range(self.n):
            result = self.containsI(i)
            self.assertTrue(result, "Tous les enclos sont sur le board")
       
    """                 
    def test_findAll(self):
        allDistances = findAllDistances(self.graph, self.n)
        
        print(allDistances)
        
        for i in range(self.n):
            for j in range(self.n):
                if i!=j: 
                    print(allDistances[i][j],",  ", allDistances[j][i])
                    self.assertEqual(allDistances[i][j], allDistances[j][i])
                # print(i, "  ", j)
    """
       
        
    def test_find_enclos(self):
        enclos = findEnclos(self.graph, 2)
        print(enclos)
        
    
if __name__ == '__main__':
    unittest.main()


