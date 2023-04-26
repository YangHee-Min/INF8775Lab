import os.path


def verify_path(filename: str):
    if not os.path.exists(filename):
        raise Exception("Le fichier n'existe pas")


def read_file(filename):
    verify_path(filename)

    f = open(filename, "r")
    enc_count, m_set_count, min_dist = [int(val) for val in f.readline().replace("\n",
                                                                                 "").split(' ')]

    m_set = [int(val) for val in f.readline().split(' ')]
    # read next n lines here
    id_to_size = {}
    for i in range(enc_count):
        size = int(f.readline().replace('\n', ''))
        id_to_size[i] = size

    weights = []
    for i in range(enc_count):
        weight_line = [int(val)
                       for val in f.readline().replace('\n', '').split(' ')]
        weights.append(weight_line)
    return (enc_count, m_set_count, min_dist, m_set, id_to_size, weights)
