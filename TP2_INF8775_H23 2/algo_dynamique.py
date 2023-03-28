from PIL import Image, ImageDraw
from itertools import chain, combinations
import math
import time
from visualisation import get_coords, get_cost_path
from time import process_time_ns as time
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

# https://stackoverflow.com/questions/1482308/how-to-get-all-subsets-of-a-set-powerset


def generatePowerset(s):
    if not s:
        return [[]]
    else:
        subsets = generatePowerset(s[1:])
        return subsets + [[s[0]] + subset for subset in subsets]


def powerset(s):
    setGen = generatePowerset(s)
    returnArray = []

    for generated in setGen:
        if len(generated) > 1:
            returnArray.append(sorted(generated))
        else:
            returnArray.append(generated)

    returnArray.sort(key=len)

    return returnArray


def getPreviousSubset(subset):
    allSubsets = powerset(subset)
    returnSubsets = []

    for subsets in allSubsets:
        if len(subsets) == len(subset)-1:
            returnSubsets.append(sorted(subsets))

    return returnSubsets


def difference(listA, listB):
    setA = set(listA)
    setB = set(listB)
    return setA.difference(setB).pop()


def TSP(coords):
    dynamic_array = {}
    path = []

    starting_point = coords.pop(0)
    N = len(coords)

    precedingNode = dict()

    # powerSet == index en j
    powerSet = powerset(coords)

    for point in coords:
        dynamic_array[point] = [None] * len(powerSet)
    # pour chacun des subsets (gauche a droite)
    for subset in powerSet:
        # pour chacun des points (haut en bas)
        for point in list(dynamic_array.keys()):

            # Si on est dans la premiere colone
            if len(subset) == 0:
                dynamic_array[point][0] = math.dist(starting_point, point)
                continue

            # si le point n'est pas dans le subset -> on le considere
            if point not in subset:

                # on trouve tous les subsets des grandeur len(subset) - 1
                possiblePaths = getPreviousSubset(subset)

                # declare une datastructure pour garder en memoire les distances possibles
                distances = {}

                # pour chacun des chemins possible
                for possiblePath in possiblePaths:
                    # on trouve le dernier point
                    previousPoint = difference(subset, possiblePath)
                    # on trouve la distance du chemin possible
                    distance = dynamic_array[previousPoint][powerSet.index(
                        possiblePath)]
                    previousPointToCurrent = math.dist(previousPoint, point)

                    # on trouve la distance totale du chemin
                    totalDistance = distance + previousPointToCurrent

                    possiblePath.append(previousPoint)
                    distances[previousPoint] = totalDistance

                if len(distances) > 0:
                    for possiblePoint, distance in distances.items():
                        if distance == min(distances.values()):
                            dynamic_array[point][powerSet.index(
                                subset)] = distance
                            precedingNode[powerSet.index(
                                subset)] = possiblePoint
    if len(subset) == N:
        returnPath = [starting_point]

        # pour chacun des chemins possible
        for possiblePath in possiblePaths:
            possiblePath = sorted(possiblePath)
            # on trouve le dernier point
            previousPoint = difference(subset, possiblePath)
            # on trouve la distance du chemin possible
            distance = dynamic_array[previousPoint][powerSet.index(
                possiblePath)]
            previousPointToCurrent = math.dist(previousPoint, point)

            # on trouve la distance totale du chemin
            totalDistance = distance + previousPointToCurrent

            possiblePath.append(previousPoint)
            distances[previousPoint] = totalDistance

        if len(distances) > 0:
            for possiblePoint, distance in distances.items():
                if distance == min(distances.values()):
                    dynamic_array[point][powerSet.index(subset)] = distance
                    precedingNode[powerSet.index(subset)] = possiblePoint

        while len(returnPath) < N+1:
            previousPoint = precedingNode[powerSet.index(subset)]
            returnPath.append(previousPoint)
            subset.remove(previousPoint)

        returnPath.append(starting_point)
        returnPath.reverse()
        return returnPath


def execution_time_dyn(filename):
    start_time = time()
    coords = get_coords(filename)
    optimal_path = TSP(coords)
    end_time = time()
    execution_time = end_time - start_time
    cost = get_cost_path(optimal_path)
    return execution_time, cost


def run_dyn():
    prefix = "./examples/N"
    sizes = [10, 14]
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
    run_dyn()
