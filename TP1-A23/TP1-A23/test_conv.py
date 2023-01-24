from read_matrix import read_matrix
from conv import conv


def main():
    ex1 = "ex2_0"
    ex2 = "ex2_1"
    m1 = read_matrix(ex1)
    m2 = read_matrix(ex2)
    m_out = conv(m1, m2)
    print(m_out)


if __name__ == "__main__":
    main()
