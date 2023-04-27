import random
from answer import generate_txt_file
from gen_enc import count_all_islands, count_islands, create_configuration, generate_enclosure, generate_enclosure_with_coords, generate_enclosures, get_edges, get_possible_next_coords, remove_none_rows_cols, remove_value
from pointage import calculPointage, calculate_theoretical_max
from gen_enc import print_table
from read_values import read_file
from typing import List, Dict
import numpy as np
import copy
from math import inf
import time


def execute(filepath: str, is_print: bool):
    """
    PSEUDO CODE:
    tant que critère d' arrêt
        choisir s dans Vsi de façon aléatoire ;
        si f (s) ≥ f (si) alors
            si+1 ← s ;
        sinon
            pi = e ^-(f (si ) - f (s))/θi
            si+1 ← s avec probabilité pi
            si+1 ← si avec probabilité 1 - pi
        i ← i + 1 ;

    """
    (enc_count, m_set_count, min_dist, enclosure_id_to_size,
     min_dist_set, weights) = read_file(filepath)

    current_enclosure_config = create_configuration(
        enclosure_id_to_size, min_dist_set)
    current_enclosure_config = simulated_annealing(initial_config=current_enclosure_config, id_to_map=enclosure_id_to_size, enc_count=enc_count, min_dist_set=min_dist_set,
                                                   min_dist=min_dist, weights=weights, initial_temperature=100)
    if is_print:
        print_table(current_enclosure_config)
    return current_enclosure_config


def simulated_annealing(initial_config, id_to_map, enc_count, min_dist_set, min_dist, weights, initial_temperature):
    current_enclosure_config = initial_config
    current_cost = calculate_cost(current_enclosure_config, enc_count,
                                  min_dist_set, min_dist, weights)
    temperature = initial_temperature
    print_table(current_enclosure_config)
    enc_count_to_regen = enc_count - 1  # number of enclosures we are gonna regenerate
    iteration = 0
    best_score = -inf
    best_config = []
    theoretical_max = calculate_theoretical_max(weights, len(min_dist_set))
    acceptance_prob = 1
    while True:  # set a small temperature threshold
        print(f'iteration {iteration}: {current_cost}')
        new_enc_config = perturb(
            current_enclosure_config, enc_count, enc_count_to_regen, id_to_map)
        new_cost = calculate_cost(new_enc_config, enc_count,
                                  min_dist_set, min_dist, weights)

        cost_diff = new_cost - current_cost
        if new_cost > best_score:
            best_config = new_enc_config
            best_score = new_cost
            generate_txt_file(best_config, enc_count)
        if cost_diff > 0:
            current_enclosure_config = copy.deepcopy(new_enc_config)
            enc_count_to_regen = 1 if round(
                enc_count_to_regen * acceptance_prob) < 1 else round(enc_count_to_regen * acceptance_prob)
            # enc_count_to_regen = len(min_dist_set) if enc_count_to_regen < len(
            #     min_dist_set) else round(enc_count_to_regen - 1)
            current_cost = new_cost
        else:
            acceptance_prob = acceptance_probability(
                cost_diff, temperature, enc_count)
            random_number = np.random.rand()
            if acceptance_prob > random_number:
                current_enclosure_config = copy.deepcopy(new_enc_config)
                current_cost = new_cost
        temperature = cooling_schedule(temperature)
        iteration += 1


def calculate_cost(new_enc_config, enc_count,
                   min_dist_set, min_dist, weights):
    return calculPointage(new_enc_config, enc_count,
                          min_dist_set, min_dist, weights)


# Higher cooling fraction = more exploration
def cooling_schedule(temperature, cooling_fraction=0.995):
    return fixed_fraction_cooling(temperature, cooling_fraction)


def fixed_fraction_cooling(initial_temperature, cooling_fraction):
    temperature = initial_temperature
    while True:
        temperature *= cooling_fraction
        return temperature


def perturb(enclosure_config, enc_count, enc_count_to_regen, id_to_map: Dict[int, int]):
    # todo remove following line after
    enc_count_to_regen = enc_count - \
        1 if enc_count <= enc_count_to_regen else enc_count_to_regen
    new_config = copy.deepcopy(enclosure_config)
    encs_to_put_back = []
    for i in range(enc_count_to_regen):
        is_new_config_valid = False
        iteration = 0
        while not is_new_config_valid:
            test_config = copy.deepcopy(new_config)
            edge_coords = get_edges(test_config)
            rand_index = random.randint(0, len(edge_coords) - 1)
            (row, col) = edge_coords[rand_index]

            label = new_config[row][col]
            if label == None:
                raise Exception("border node value cannot be None")
            remove_value(test_config, label)

            island_count = count_islands(test_config)
            if (island_count == 1):
                new_config = test_config.copy()
                is_new_config_valid = True
                encs_to_put_back.append((label, id_to_map[label]))
            else:
                if (iteration >= 5):
                    continue
                iteration += 1
    random.shuffle(encs_to_put_back)
    for enc_label_to_coord in encs_to_put_back:
        id, size = enc_label_to_coord
        edge_coords = get_edges(new_config)

        next_coords = []
        while len(next_coords) < 1:
            rand_index = random.randint(0, len(edge_coords) - 1)
            (row, col) = edge_coords[rand_index]
            next_coords = get_possible_next_coords(new_config, row, col)
        row, col = next_coords[random.randint(0, len(next_coords) - 1)]
        new_config = generate_enclosure_with_coords(
            table=new_config, id_size=(id, size), row=row, col=col)[0]
    new_config = remove_none_rows_cols(new_config)
    return new_config


def acceptance_probability(cost_diff, temperature, sample_size):
    scaled_cost_diff = cost_diff / ((sample_size ** 2) * 100)
    if scaled_cost_diff > 0:
        return 1.0
    else:
        return np.exp(scaled_cost_diff / temperature)


if __name__ == "__main__":
    filepath = "D:/POLY/H2023/INF8775/INF8775Lab/tp3/TP3-H23/n20_m15_V-74779.txt"
    is_print = True
    answer_grid = execute(filepath, is_print)
