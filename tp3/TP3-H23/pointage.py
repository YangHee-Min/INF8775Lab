from distance import findAllDistances

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
    allDistances = findAllDistances(graph, n)
    v = calculerSousEnsemble(allDistances, m, k)
    
    totalWeight = 0
    for i in range(n):
        for j in range(n):
            if i != j:
                totalWeight += weight[i][j] * allDistances[i][j]
    
    return v - totalWeight
    
    
    