from conv import conv
import numpy as np


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
        midpoint = len(matrixA) // 2
        subA1_1 = matrixA[:midpoint, :midpoint]
        subA1_2 = matrixA[:midpoint, midpoint:]
        subA2_1 = matrixA[midpoint:, :midpoint]
        subA2_2 = matrixA[midpoint:, midpoint:]

        subB1_1 = matrixB[:midpoint, :midpoint]
        subB1_2 = matrixB[:midpoint, midpoint:]
        subB2_1 = matrixB[midpoint:, :midpoint]
        subB2_2 = matrixB[midpoint:, midpoint:]

        m1 = strassen(add(subA1_1, subA2_2),
                      add(subB1_1, subB2_2))
        m2 = strassen(add(subA2_1, subA2_2), subB1_1)
        m3 = strassen(subA1_1, substract(subB1_2, subB2_2))
        m4 = strassen(subA2_2, substract(subB2_1, subB1_1))
        m5 = strassen(add(subA1_1, subA1_2), subB2_2)
        m6 = strassen(substract(subA2_1, subA1_1),
                      add(subB1_1, subB1_2))
        m7 = strassen(substract(subA1_2, subA2_2),
                      add(subB2_1, subB2_2))

        c1_1 = add(substract(add(m1, m4), m5), m7)
        c1_2 = add(m3, m5)
        c2_1 = add(m2, m4)
        c2_2 = add(add(substract(m1, m2), m3), m6)

        c = np.vstack(np.hstack((c1_1, c1_2)), np.hstack((c2_1, c2_2)))

        return c
    else:
        return [[matrixA[0][0] * matrixB[0][0]]]


def strassen_threshold(matrixA, matrixB, threshold):
    if len(matrixA) > threshold:
        midpoint = len(matrixA // 2)
        subA1_1 = matrixA[:midpoint, :midpoint]
        subA1_2 = matrixA[:midpoint, midpoint:]
        subA2_1 = matrixA[midpoint:, :midpoint]
        subA2_2 = matrixA[midpoint:, midpoint:]

        subB1_1 = matrixA[:midpoint, :midpoint]
        subB1_2 = matrixA[:midpoint, midpoint:]
        subB2_1 = matrixA[midpoint:, :midpoint]
        subB2_2 = matrixA[midpoint:, midpoint:]

        m1 = strassen_threshold(add(subA1_1, subA2_2),
                                add(subB1_1, subB2_2), threshold)
        m2 = strassen_threshold(
            add(subA2_1, subA2_2), subB1_1, threshold)
        m3 = strassen_threshold(subA1_1, substract(
            subB1_2, subB2_2), threshold)
        m4 = strassen_threshold(subA2_2, substract(
            subB2_1, subB1_1), threshold)
        m5 = strassen_threshold(
            add(subA1_1, subA1_2), subB2_2, threshold)
        m6 = strassen_threshold(substract(subA2_1, subA1_1),
                                add(subB1_1, subB1_2), threshold)
        m7 = strassen_threshold(substract(subA1_2, subA2_2),
                                add(subB2_1, subB2_2), threshold)

        c1 = add(substract(add(m1, m4), m5), m7)
        c2 = add(m3, m5)
        c3 = add(m2, m4)
        c4 = add(add(substract(m1, m2), m3), m6)

        c1_1 = add(substract(add(m1, m4), m5), m7)
        c1_2 = add(m3, m5)
        c2_1 = add(m2, m4)
        c2_2 = add(add(substract(m1, m2), m3), m6)

        c = np.vstack(np.hstack((c1_1, c1_2)), np.hstack((c2_1, c2_2)))

        return c
    else:
        return conv(matrixA, matrixB)
