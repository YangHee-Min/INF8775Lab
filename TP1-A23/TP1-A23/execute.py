from read_matrix import read_matrix
from conv import conv
from strassen import strassen, strassen_threshold
from method import Method
from time import process_time_ns as time


def execute(ex1, ex2, method=Method.CONV, is_print=False, is_time=False):
    timestamp1 = time()
    m1 = read_matrix(ex1)
    m2 = read_matrix(ex2)
    timestamp2 = time()
    loading_time_ms = (timestamp2 - timestamp1) / 1_000_000

    timestamp_start_conv = time()
    if method is Method.STRASSEN:
        m_out = strassen(m1, m2)
    if method is Method.STRASSEN_THRESHOLD:
        m_out = strassen_threshold(m1, m2, 2)
    else:
        m_out = conv(m1, m2)
    timestamp_finish_conv = time()
    execution_time_ms = (timestamp_finish_conv -
                         timestamp_start_conv) / 1_000_000

    if is_print:
        for row in m_out:
            row_str = ""
            for element in row:
                row_str += f"{element} "
            print(f"{row_str}")
    if is_time:
        print(execution_time_ms)

    return execution_time_ms
