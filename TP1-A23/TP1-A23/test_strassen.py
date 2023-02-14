from strassen import *
from read_matrix import read_matrix
from execute import execute
from method import Method


def main():
    ex1 = "ex2_0"
    ex2 = "ex2_1"
    # execute(ex1, ex2, method=Method.CONV, is_print=True, is_time=True)
    execute(ex1, ex2, method=Method.STRASSEN, is_print=True, is_time=True)
    # execute(ex1, ex2, method=Method.STRASSEN, is_time=True)
    # execute(ex1, ex2, method=Method.STRASSEN_THRESHOLD,
    # is_print=False, is_time=True)
    # m1 = read_matrix(ex1)
    # m2 = read_matrix(ex2)
    # convMatrix = conv(m1, m2)
    # strassenMatrix = strassen(m1, m2)
    # for i in range(len(m1)):
    #     strassen_threshold_m = strassen_threshold(m1, m2, i+1)
    #     if strassen_threshold_m != strassenMatrix or strassen_threshold_m != convMatrix:
    #         print("ERROR")
    #         return
    # print("SUCCESS WE GOOD BOYS")


if __name__ == "__main__":
    main()
