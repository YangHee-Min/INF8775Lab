import math
from PIL import Image, ImageDraw


def get_coords(file_name):
    f = open(file_name, "r")
    coords = []
    N = int(f.readline())
    print(f"N : {N} ")

    for i in range(N):
        line = f.readline()
        coords.append(tuple(int(coord) for coord in line.split("  ")))
    return coords


def get_cost_path(optimal_path_coords: list):
    total_dist = 0
    current_coords = optimal_path_coords.pop(0)
    for coord in optimal_path_coords:
        total_dist += math.dist(current_coords, coord)
        current_coords = coord
    return total_dist


def get_path(coords: list, optimal_path: list):
    index_path = []
    for coord in optimal_path:
        index = coords.index(coord)
        index_path.append(index)

    second_index = index_path[1]
    # Assuming the last point of the list is the starting point
    before_last_index = index_path[len(index_path) - 2]

    if (before_last_index < second_index):
        index_path.reverse()
    return index_path
