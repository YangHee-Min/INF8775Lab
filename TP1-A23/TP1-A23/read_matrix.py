import numpy


def read_matrix(filename):
    file = open(filename, 'r')
    data = []
    row_count = 0
    for row in file:
        if row_count != 0:
            data.append([int(x) for x in row.split()])
        row_count += 1
    data = numpy.array(data)
    return data


def get_dim_matrix(filename):
    file = open(filename, 'r')
    exp = int(file.readline().strip('\n'))
    return 2 ** exp
