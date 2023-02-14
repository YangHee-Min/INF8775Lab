from strassen import *
from read_matrix import read_matrix
from execute import execute
from method import Method


def main():
    ex1 = "ex6_0"
    ex2 = "ex6_1"
    execute(ex1, ex2, method=Method.CONV, is_print=False, is_time=True)
    execute(ex1, ex2, method=Method.STRASSEN, is_print=False, is_time=True)
    execute(ex1, ex2, method=Method.STRASSEN_THRESHOLD,
            is_print=False, is_time=True)


if __name__ == "__main__":
    main()
