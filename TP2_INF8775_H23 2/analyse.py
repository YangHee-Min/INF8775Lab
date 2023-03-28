# from algo_glouton import TSP as TSP_GLOUTON
from graphe import TSP as TSP_MST
from algo_dynamique import TSP as TSP_DYN
from visualisation import get_coords, get_cost_path
from time import process_time_ms as time
import pandas as pd


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
    optimal_path = TSP_GLOUTON(coords)
    end_time = time()
    execution_time = end_time - start_time
    cost = get_cost_path(optimal_path)
    return execution_time, cost


def execution_time_dyn(filename):
    start_time = time()
    coords = get_coords(filename)
    optimal_path = TSP_DYN(coords)
    end_time = time()
    execution_time = end_time - start_time
    cost = get_cost_path(optimal_path)
    return execution_time, cost


def execution_time_mst(filename):
    start_time = time()
    coords = get_coords(filename)
    optimal_path = TSP_MST(coords)
    end_time = time()
    execution_time = end_time - start_time
    cost = get_cost_path(optimal_path)
    return execution_time, cost


def run_greedy():
    prefix = "TP2_INF8775_H23 2/examples/N"
    # counts = [8]
    sizes = [64, 128, 256, 512, 1024, 2048]
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


def run_mst():
    prefix = "TP2_INF8775_H23 2/examples/N"
    # counts = [8]
    sizes = [32, 64, 128, 256, 512, 1024]
    example_count = 5
    times, costs = [], []
    for count in sizes:
        average_time = 0
        average_cost = 0
        for i in range(example_count):
            file = f'{prefix}{count}_{i}'
            time, cost = execution_time_mst(file)
            average_time += time
            average_cost += cost
        average_time /= example_count
        average_cost /= example_count
        times.append(average_time)
        costs.append(average_cost)
    create_spreadsheet(sizes, times, costs, "mst")


def run_dyn():
    prefix = "TP2_INF8775_H23 2/examples/N"
    sizes = [4, 8, 16, 24]
    example_count = 5
    times, costs = [], []
    for count in sizes:
        average_time = 0
        average_cost = 0
        for i in range(example_count):
            file = f'{prefix}{count}_{i}'
            time, cost = execution_time_dyn(file)
            average_time += time
            average_cost += cost
        average_time /= example_count
        average_cost /= example_count
        times.append(average_time)
        costs.append(average_cost)
    create_spreadsheet(sizes, times, costs, "dyn")


if __name__ == "__main__":
    # run_greedy()
    # run_mst()
    run_dyn()
