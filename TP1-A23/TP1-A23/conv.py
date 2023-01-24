def conv(listA, listB):
    n = len(listA)
    listC = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                listC[i][j] += listA[i][k] * listB[k][j]
    return listC
