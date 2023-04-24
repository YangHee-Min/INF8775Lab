from gen_enc import generate_enclosures
from gen_enc import print_table
from read_values import read_file
from typing import List, Dict
import heapq
import random


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
    (enc_count, m_set_count, min_dist, id_size_map, weights) = read_file(filepath)
    # TODO: use m_set_count and min_dist in fitness function and if not respected score should be very low
    # TODO: Also use weights to determine how valuable an enclosure is
    population_set = gen_population(id_size_map, POPULATION_COUNT)
    maximum_score = m_set_count ** 2
    iteration = 0
    while not is_stop_criteria_met(iteration, population_set[0], maximum_score):
        elite_set = select_elite(population_set)
        crossover_set = gen_crossover_set(elite_set)
        mutation_set = gen_mutation_set(elite_set)

        population_set = select_next_generation(
            elite_set, crossover_set, mutation_set, POPULATION_COUNT)
        iteration += 1

    if is_print:
        print_table(population_set[len(population_set) - 1][1])


def gen_population(id_to_size_map: Dict[int, int], population_count) -> list:
    initial_set = []
    while len(initial_set) < population_count:
        new_map = generate_enclosures(id_to_size_map)
        new_fitness_score = get_fitness_score(new_map)
        # note that heappush puts our highest scores to the end of the priority queue
        initial_set.append((new_fitness_score, new_map))
    initial_set = heapq.nlargest(
        len(initial_set), initial_set, key=heap_comparison_func)
    return initial_set


def is_stop_criteria_met(current_iteration: int, enclosure_map, threshold) -> bool:
    # max iteration
    MAX_ITERATION_COUNT = 5
    if current_iteration >= MAX_ITERATION_COUNT:
        return True

    # TODO: need to change based on the actual input matrix given

    if get_fitness_score(enclosure_map) >= threshold:
        return True

    return False


def select_elite(sorted_heap: list) -> list:
    CUTOFF_PERCENTAGE = 0.3
    total_length = len(sorted_heap)
    cutoff_count = int(round(total_length * CUTOFF_PERCENTAGE))
    return heapq.nlargest(cutoff_count, sorted_heap, key=heap_comparison_func)


def get_fitness_score(enclosure_map: set):
    return random.randint(-100, 100)


def gen_crossover_set(prioritized_maps) -> list:
    crossover_set = prioritized_maps
    # TODO: do crossover between parents
    return crossover_set


def gen_mutation_set(prioritized_maps) -> List:
    mutated_set = prioritized_maps
    # TODO: do mutation
    return mutated_set


def select_next_generation(elite_set, crossover_set, mutation_set, POPULATION_COUNT) -> list:
    next_generation = []
    for score_map in (elite_set + crossover_set + mutation_set):
        next_generation.append(score_map)
    new_generation_count = POPULATION_COUNT if POPULATION_COUNT < len(
        next_generation) else len(next_generation)
    return heapq.nlargest(new_generation_count, next_generation, key=heap_comparison_func)


def heap_comparison_func(elem):
    score, list = elem
    return score


if __name__ == "__main__":
    filepath = "D:/POLY/H2023/INF8775/INF8775Lab/tp3/TP3-H23/n20_m15_V-74779.txt"
    is_print = True
    execute(filepath, is_print)
