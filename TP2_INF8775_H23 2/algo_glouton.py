import math
from visualisation import get_coords, get_cost_path
from time import process_time_ns as time
import pandas as pd
# returns the position of the closest point


def shortest_distance(point, coords):
    return_position = -1
    for i, coord in enumerate(coords):
        distance_new_point = math.dist(point, coord)
        if return_position == -1 or distance_new_point < math.dist(point, coords[return_position]):
            return_position = i
    return return_position


def TSP(coords):
    if len(coords) < 1:
        return []

    starting_point = coords.pop(0)
    path = [starting_point]

    # while there is still coords not evaluated
    while len(coords) > 0:
        # find shortest point
        starting_point = coords.pop(shortest_distance(starting_point, coords))
        path.append(starting_point)

    path.append(path[0])
    return path


def create_spreadsheet(size_list, execution_time_list, cost_list, file_name_no_extension):
    # Create a DataFrame with the data
    data = {'Size': size_list,
            'Execution Time': execution_time_list, 'Cost': cost_list}
    df = pd.DataFrame(data)

    # Create a new Excel file and write the DataFrame to a worksheet
    with pd.ExcelWriter(f'{file_name_no_extension}.xlsx') as writer:
        df.to_excel(writer, index=False)

# run a bunch of files to get their execution times and put them in an excel


def execution_time_greedy(filename):
    start_time = time()
    coords = get_coords(filename)
    optimal_path = TSP(coords)
    end_time = time()
    execution_time = end_time - start_time
    cost = get_cost_path(optimal_path)
    return execution_time, cost


def run_greedy():
    prefix = "./examples/N"
    # counts = [8]
    sizes = [8, 10, 12, 14, 16]
    example_count = 5
    times, costs = [], []
    for count in sizes:
        average_time = 0
        average_cost = 0
        for i in range(example_count):
            file = f'{prefix}{count}_{i}'
            time, cost = execution_time_greedy(file)
            average_time += time
            average_cost += cost
        average_time /= example_count
        average_cost /= example_count
        times.append(average_time)
        costs.append(average_cost)
    create_spreadsheet(sizes, times, costs, "greedy")


if __name__ == "__main__":
    # files = ["./examples/hard_N52", "./examples/hard_N91",
    #          "./examples/hard_N130", "./examples/hard_N169", "./examples/hard_N199"]
    # for file in files:
    #     coords = get_coords(file)
    #     optimal_path = TSP(coords)
    #     print(get_cost_path(optimal_path))
    run_greedy()
