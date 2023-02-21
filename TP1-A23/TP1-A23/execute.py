from read_matrix import read_matrix
from conv import conv
from strassen import strassen, strassen_threshold
from method import Method
from time import time_ns as time


def execute(ex1, ex2, method=Method.CONV, is_print=False, is_time=False):
    timestamp1 = time()
    m1 = read_matrix(ex1)
    m2 = read_matrix(ex2)
    timestamp2 = time()
    loading_time = timestamp2 - timestamp1

    timestamp_start_conv = time()
    if method is Method.STRASSEN:
        m_out = strassen(m1, m2)
    if method is Method.STRASSEN_THRESHOLD:
        m_out = strassen_threshold(m1, m2, 2)
    else:
        m_out = conv(m1, m2)
    timestamp_finish_conv = time()
    execution_time = timestamp_finish_conv - timestamp_start_conv

    if is_print:
        print("Final matrix content:")
        print(m_out)
    if is_time:
        print("Total loading time: %sms" % loading_time)
        print("Total execution time: %sms" % execution_time)

    return execution_time


if __name__ == "__main__":
    print(execute("ex6_0", "ex6_1", Method.CONV))
