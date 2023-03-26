import math
import queue

# returns the position of the closest point


def shortest_distance(point, coords):
    return_position = -1
    for i, coord in enumerate(coords):
        distance_new_point = math.dist(point, coord)
        if return_position == -1 or distance_new_point < math.dist(point, coords[return_position]):
            return_position = i
    return return_position


def TSP(coords):
    starting_point = coords.pop(0)
    path = [starting_point]

    # while there is still coords not evaluated
    while len(coords) > 0:
        # find shortest point
        starting_point = coords.pop(shortest_distance(starting_point, coords))
        path.append(starting_point)

    path.append(path[0])
    return path
