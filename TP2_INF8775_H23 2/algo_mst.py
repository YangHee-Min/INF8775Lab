import heapq
import math
from time import process_time_ns as time
import pandas as pd
from visualisation import get_coords, get_cost_path


def TSP(coords: list):
    edges = MST(coords)
    optimal_path = preorder_traversal(edges)
    optimal_path.append(optimal_path[0])
    return optimal_path


def find_clusters(coords):
    clusters = {}
    for coord in coords:
        clusters[coord] = {coord}
    return clusters


def MST(coords):
    clusters = find_clusters(coords)
    edges = []
    pq = []

    for i, coord1 in enumerate(coords):
        for coord2 in coords[i+1:]:
            weight = math.dist(coord1, coord2)
            heapq.heappush(pq, (weight, coord1, coord2))

    while pq:
        weight, coord1, coord2 = heapq.heappop(pq)
        cluster1 = clusters[coord1]
        cluster2 = clusters[coord2]
        if cluster1 is not cluster2:
            # Merge the clusters
            new_cluster = cluster1.union(cluster2)
            for coord in new_cluster:
                clusters[coord] = new_cluster
            # Add the edge to the minimum spanning tree
            edges.append((coord1, coord2))

    return edges


def preorder_traversal(minimum_spanning_tree):
    adj_list = {}
    for u, v in minimum_spanning_tree:
        if u not in adj_list:
            adj_list[u] = []
        adj_list[u].append(v)
        if v not in adj_list:
            adj_list[v] = []
        adj_list[v].append(u)

    visited = set()
    preordered_nodes = []

    def dfs(node):
        visited.add(node)
        preordered_nodes.append(node)
        for neighbor in adj_list[node]:
            if neighbor not in visited:
                dfs(neighbor)

    dfs(minimum_spanning_tree[0][0])

    return preordered_nodes


def run_mst():
    sizes = [8, 10, 12, 14, 16]
    example_count = 5
    times, costs = [], []
    for count in sizes:
        average_time = 0
        average_cost = 0
        for i in range(example_count):
            prefix = "./examples/N"
            file = f'{prefix}{count}_{i}'
            time, cost = execution_time_mst(file)
            average_time += time
            average_cost += cost
        average_time /= example_count
        average_cost /= example_count
        times.append(average_time)
        costs.append(average_cost)
    create_spreadsheet(sizes, times, costs, "mst")


def create_spreadsheet(size_list, execution_time_list, cost_list, file_name_no_extension):
    # Create a DataFrame with the data
    data = {'Size': size_list,
            'Execution Time': execution_time_list, 'Cost': cost_list}
    df = pd.DataFrame(data)

    # Create a new Excel file and write the DataFrame to a worksheet
    with pd.ExcelWriter(f'{file_name_no_extension}.xlsx') as writer:
        df.to_excel(writer, index=False)

# run a bunch of files to get their execution times and put them in an excel


def execution_time_mst(filename):
    start_time = time()
    coords = get_coords(filename)
    optimal_path = TSP(coords)
    end_time = time()
    execution_time = end_time - start_time
    cost = get_cost_path(optimal_path)
    return execution_time, cost


if __name__ == "__main__":
    # files = ["./examples/hard_N52", "./examples/hard_N91",
    #          "./examples/hard_N130", "./examples/hard_N169", "./examples/hard_N199"]
    # for file in files:
    #     coords = get_coords(file)
    #     optimal_path = TSP(coords)
    #     print(get_cost_path(optimal_path))
    run_mst()
