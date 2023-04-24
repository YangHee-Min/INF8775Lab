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
    
    def test_find_voisin(self):
        voisins = getVoisins(6, 0, len(GRAPH[0]))
        print(voisins)
        

    def test_find_contours(self):
        contours = findContours(GRAPH, (3, 3))
        contours.sort()
        print(contours)
    
    def test_find_distances(self):
        contours = findContours(GRAPH, (3, 3))
        distances = findAllShortestPath(GRAPH, contours, 4)
        print(distances)
    
    
if __name__ == '__main__':
    unittest.main()


