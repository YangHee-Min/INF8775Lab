from read_values import read_file
from gen_enc import generate_enclosures
from island import CalculDistance

from datetime import datetime

def calculerSousEnsemble(allDistances, m, k):
    valid = True
    for a in m:
        for b in m:
            if a != b:
                if allDistances[a][b] > k:
                    valid = False
    
    if valid:
        return pow(len(m), 2)
    else:
        return 0
    

def calculPointage(graph, n, m, k, weight):
    calculDistance = CalculDistance(graph, n)
    allDistances = calculDistance.findAllDistances()
    
    print(allDistances)
    
    v = calculerSousEnsemble(allDistances, m, k)
    
    totalWeight = 0
    for i in range(n):
        for j in range(i+1, n):
            totalWeight += weight[i][j] * allDistances[i][j]
            totalWeight += weight[j][i] * allDistances[j][i]
    
    return v - totalWeight
    

if __name__ =="__main__":
    timestamp1 = datetime.now()
    filename =  "/Users/charles-antoinelaurin/depot_distant/H23/INF8775Lab/tp3/TP3-H23/n1000_m500_V-8435325196.txt"
    (enc_count, m_set_count, min_dist, id_to_size, weights, m_set) = read_file(filename)
    table = generate_enclosures(id_to_size)
    
    timestamp2 = datetime.now()
    print(timestamp2 - timestamp1)
    
    score = calculPointage(table, enc_count, m_set, min_dist, weights)
    timestamp3 = datetime.now()
    print(timestamp3 - timestamp2)
    print(score)
    