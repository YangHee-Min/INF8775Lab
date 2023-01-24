from conv import conv


def subDivide(matrix):
    n = len(matrix)
    returnDict = {
        "1.1": [],
        "1.2": [],
        "2.1": [],
        "2.2": [],
    }

    for i, row in enumerate(matrix):
        if i < n/2:
            returnDict["1.1"].append(row[:(n//2)])
            returnDict["1.2"].append(row[n//2:])
        else:
            returnDict["2.1"].append(row[:(n//2)])
            returnDict["2.2"].append(row[n//2:])

    return returnDict


def recompose(dictIn):
    c = []
    for i in range(len(dictIn["1.1"])):
        c.append(dictIn["1.1"][i])
        for elem in dictIn["1.2"][i]:
            c[-1].append(elem)
    for i in range(len(dictIn["2.1"])):
        c.append(dictIn["2.1"][i])
        for elem in dictIn["2.2"][i]:
            c[-1].append(elem)
    return c


def add(matrixA, matrixB):
    c = []
    for i in range(len(matrixA)):
        row = []
        for j in range(len(matrixB)):
            row.append(matrixA[i][j] + matrixB[i][j])
        c.append(row)
    return c


def substract(matrixA, matrixB):
    c = []
    for i in range(len(matrixA)):
        row = []
        for j in range(len(matrixB)):
            row.append(matrixA[i][j] - matrixB[i][j])
        c.append(row)
    return c


def strassen(matrixA, matrixB):
    if len(matrixA) > 1:
        subA = subDivide(matrixA)
        subB = subDivide(matrixB)

        m1 = strassen(add(subA["1.1"], subA["2.2"]),
                      add(subB["1.1"], subB["2.2"]))
        m2 = strassen(add(subA["2.1"], subA["2.2"]), subB["1.1"])
        m3 = strassen(subA["1.1"], substract(subB["1.2"], subB["2.2"]))
        m4 = strassen(subA["2.2"], substract(subB["2.1"], subB["1.1"]))
        m5 = strassen(add(subA["1.1"], subA["1.2"]), subB["2.2"])
        m6 = strassen(substract(subA["2.1"], subA["1.1"]),
                      add(subB["1.1"], subB["1.2"]))
        m7 = strassen(substract(subA["1.2"], subA["2.2"]),
                      add(subB["2.1"], subB["2.2"]))

        c1 = add(substract(add(m1, m4), m5), m7)
        c2 = add(m3, m5)
        c3 = add(m2, m4)
        c4 = add(add(substract(m1, m2), m3), m6)

        returnDict = {
            "1.1": c1,
            "1.2": c2,
            "2.1": c3,
            "2.2": c4,
        }

        return recompose(returnDict)
    else:
        return [[matrixA[0][0] * matrixB[0][0]]]


def strassen(matrixA, matrixB):
    if len(matrixA) > 1:
        subA = subDivide(matrixA)
        subB = subDivide(matrixB)

        m1 = strassen(add(subA["1.1"], subA["2.2"]),
                      add(subB["1.1"], subB["2.2"]))
        m2 = strassen(add(subA["2.1"], subA["2.2"]), subB["1.1"])
        m3 = strassen(subA["1.1"], substract(subB["1.2"], subB["2.2"]))
        m4 = strassen(subA["2.2"], substract(subB["2.1"], subB["1.1"]))
        m5 = strassen(add(subA["1.1"], subA["1.2"]), subB["2.2"])
        m6 = strassen(substract(subA["2.1"], subA["1.1"]),
                      add(subB["1.1"], subB["1.2"]))
        m7 = strassen(substract(subA["1.2"], subA["2.2"]),
                      add(subB["2.1"], subB["2.2"]))

        c1 = add(substract(add(m1, m4), m5), m7)
        c2 = add(m3, m5)
        c3 = add(m2, m4)
        c4 = add(add(substract(m1, m2), m3), m6)

        returnDict = {
            "1.1": c1,
            "1.2": c2,
            "2.1": c3,
            "2.2": c4,
        }

        return recompose(returnDict)
    else:
        return [[matrixA[0][0] * matrixB[0][0]]]


def strassen_threshold(matrixA, matrixB, threshold):
    if len(matrixA) > threshold:
        subA = subDivide(matrixA)
        subB = subDivide(matrixB)

        m1 = strassen_threshold(add(subA["1.1"], subA["2.2"]),
                                add(subB["1.1"], subB["2.2"]), threshold)
        m2 = strassen_threshold(
            add(subA["2.1"], subA["2.2"]), subB["1.1"], threshold)
        m3 = strassen_threshold(subA["1.1"], substract(
            subB["1.2"], subB["2.2"]), threshold)
        m4 = strassen_threshold(subA["2.2"], substract(
            subB["2.1"], subB["1.1"]), threshold)
        m5 = strassen_threshold(
            add(subA["1.1"], subA["1.2"]), subB["2.2"], threshold)
        m6 = strassen_threshold(substract(subA["2.1"], subA["1.1"]),
                                add(subB["1.1"], subB["1.2"]), threshold)
        m7 = strassen_threshold(substract(subA["1.2"], subA["2.2"]),
                                add(subB["2.1"], subB["2.2"]), threshold)

        c1 = add(substract(add(m1, m4), m5), m7)
        c2 = add(m3, m5)
        c3 = add(m2, m4)
        c4 = add(add(substract(m1, m2), m3), m6)

        returnDict = {
            "1.1": c1,
            "1.2": c2,
            "2.1": c3,
            "2.2": c4,
        }

        return recompose(returnDict)
    else:
        return conv(matrixA, matrixB)
