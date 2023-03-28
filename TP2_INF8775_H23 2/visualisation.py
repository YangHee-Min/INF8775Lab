import math
import sys
from PIL import Image, ImageDraw
# from algo_glouton import TSP as TSP_GLOUTON
# from algo_mst import TSP as TSP_MST
# from algo_dynamique import TSP as TSP_DYN


def get_coords(file_name):
    f = open(file_name, "r")
    coords = []
    N = int(f.readline())
    print(f"N : {N} ")

    for i in range(N):
        line = f.readline()
        coords.append(tuple(int(coord) for coord in line.split("  ")))
    return coords

# Create visual support


def draw_points(path, filename):
    img = Image.new('RGB', (2000+2, 2000+2), (255, 255, 255))
    draw = ImageDraw.Draw(img)

    for i, coord in enumerate(path):
        # print point
        x1, y1 = coord
        # create Point
        draw.point((x1 + 1, y1 + 1), fill=(0, 0, 0))
        # print path to next
        if i < len(path)-1:
            x2, y2 = path[i+1]
            # create line
            draw.line((x1+1, y1+1, x2+1, y2+1), fill=(0, 0, 0), width=1)

    # Save Image
    img.save(f"{filename}.png")


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


if __name__ == "__main__":
    filename = "./examples/N5_0"
    # coords = get_coords(filename)
    # list_greedy = TSP_GLOUTON(coords)
    # print(get_cost_path(list_greedy))

    coords = get_coords(filename)
    # list_mst = TSP_MST(coords)
    draw_points(list_mst, "testMST")
    print(get_cost_path(list_mst))

    # file_name = "N15_"
    # for i in range(5):
    #     file = file_name + str(i)
    #     draw_points(TSP_GLOUTON(get_coords(file)), file+"_GLOUTON")
    # file_name = "N50_"
    # for j in range(5):
    #     file = file_name + str(j)
    #     draw_points(TSP_MST(get_coords(file)), file+"_TSP")
    """
    file_name = "N15_"
    for k in range(1):
        file= file_name + str(j)
        draw_points(TSP_DYN(get_coords(file)), file+"_DYNAMIQUE")
    """
