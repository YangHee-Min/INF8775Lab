import heapq
import math


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
            new_cluster = cluster1.union(cluster2)
            for coord in new_cluster:
                clusters[coord] = new_cluster
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
