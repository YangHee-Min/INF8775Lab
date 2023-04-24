from gen_enc import generate_enclosures
from gen_enc import print_table
from typing import List
import heapq


def execute(filepath: str, is_print: bool):
    """
    PSEUDO CODE:

    P_i: current population
    i: generation count
    f: fitness function

    Generate random population P_0
    i = 0
    while not stop_criteria_met:
        P = selection(P_i, proportion_of_population, f)
        P_c = crossover(P)
        P_m = mutation(P)
        P_next_gen = selection(P_i U P_c U Pm |P_i| f) # keep this size of P_i
        i += 1
    """
    POPULATION_COUNT = 10
    population_set = gen_population(filepath, POPULATION_COUNT)
    iteration = 0
    while not is_stop_criteria_met():
        elite_set = select_elite(population_set)
        crossover_set = gen_crossover_set()
        mutation_set = gen_mutation_set()

        population_set = select_next_generation(
            elite_set, crossover_set, mutation_set, POPULATION_COUNT)
        i += 1

    if is_print:
        print_table(population_set[len(population_set) - 1])


def gen_population(filepath, population_count) -> list:
    initial_set = []
    while len(initial_set) < population_count:
        new_map = generate_enclosures(filepath)
        new_fitness_score = get_fitness_score(new_map)
        # note that heappush puts our highest scores to the end of the priority queue
        heapq.heappush(initial_set, (new_fitness_score, new_map))
    return initial_set


def is_stop_criteria_met(current_iteration: int, enclosure_map) -> bool:
    # max iteration
    MAX_ITERATION_COUNT = 5
    if current_iteration >= MAX_ITERATION_COUNT:
        return True

    # TODO: need to change based on the actual input matrix given
    SOLUTION_FOUND_FITNESS_THRESHOLD = 300
    if get_fitness_score(enclosure_map) > SOLUTION_FOUND_FITNESS_THRESHOLD:
        return True

    return False


def select_elite(sorted_maps: list) -> list:
    CUTOFF_PERCENTAGE = 0.3
    total_length = len(sorted_maps)
    first_element_index = total_length - (total_length * CUTOFF_PERCENTAGE)
    return sorted_maps[first_element_index:len(sorted_maps)]


def get_fitness_score(enclosure_map: set):
    return 100


def gen_crossover_set(prioritized_maps) -> list:
    crossover_set = []
    # TODO: do crossover between parents
    return crossover_set


def gen_mutation_set(prioritized_maps) -> List:
    mutated_set = []
    # TODO: do mutation
    return mutated_set


def select_next_generation(elite_set, crossover_set, mutation_set, POPULATION_COUNT) -> list:
    next_generation = []
    for score_map in (elite_set + crossover_set + mutation_set):
        heapq.heappush(next_generation, score_map)
    first_index = len(next_generation) - \
        POPULATION_COUNT if len(next_generation) - POPULATION_COUNT > 0 else 0
    return next_generation[first_index:len(next_generation)]


if __name__ == "__main__":
    filepath = "D:/POLY/H2023/INF8775/INF8775Lab/tp3/TP3-H23/n20_m15_V-74779.txt"
    is_print = True
    execute(filepath, is_print)