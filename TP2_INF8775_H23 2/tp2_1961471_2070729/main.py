from algo_glouton import TSP as TSP_GLOUTON
from algo_mst import TSP as TSP_MST
from algo_dynamique import TSP as TSP_DYN
from time import process_time_ns as time


def print_path(coords, path):
    for point in path:
        print(coords.index(point))


def get_path(method, coords):
    path = []
    coords_copy = coords.copy()
    if method == "glouton":
        path = TSP_GLOUTON(coords)
    elif method == "progdyn":
        path = TSP_DYN(coords)
    elif method == "approx":
        path = TSP_MST(coords)

    if coords_copy.index(path[1]) > coords_copy.index(path[-2]):
        path.reverse()

    return path


def load_coords(filepath):
    f = open(filepath, "r")
    coords = []
    N = int(f.readline())
    for i in range(N):
        line = f.readline()
        coords.append(tuple(int(coord) for coord in line.split("  ")))
    return coords


def execute(filepath, method, is_time, is_print):
    coords = load_coords(filepath)
    copy_coords = coords.copy()
    if is_time:
        startTime = time() / 1000000

    path = get_path(method, coords)

    if is_time:
        print((time()/ 1000000)-startTime)

    if is_print:
        print_path(copy_coords, path)
