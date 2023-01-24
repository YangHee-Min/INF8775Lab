from strassen import *
from read_matrix import read_matrix


def main():
    ex1 = "ex6_0"
    ex2 = "ex6_1"
    m1 = read_matrix(ex1)
    m2 = read_matrix(ex2)
    convMatrix = conv(m1, m2)
    strassenMatrix = strassen(m1, m2)
    for i in range(len(m1)):
        strassen_threshold_m = strassen_threshold(m1, m2, i+1)
        if strassen_threshold_m != strassenMatrix or strassen_threshold_m != convMatrix:
            print("ERROR")
            return
    print("SUCCESS WE GOOD BOYS")


if __name__ == "__main__":
    main()
