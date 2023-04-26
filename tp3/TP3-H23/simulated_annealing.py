from gen_enc import generate_enclosures
from island import Island
from pointage import calculPointage
from gen_enc import print_table
from read_values import read_file
from typing import List, Dict
import numpy as np


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
    (enc_count, m_set_count, min_dist, min_dist_set,
     enclosure_id_to_size, weights) = read_file(filepath)

    current_enclosure_config = generate_enclosures(
        enclosure_id_to_size, min_dist_set)
    simulated_annealing(initial_config=current_enclosure_config, enc_count=enc_count, min_dist_set=min_dist_set,
                        min_dist=min_dist, weights=weights, initial_temperature=1.0, cooling_schedule=cooling_schedule)
    if is_print:
        print_table(current_enclosure_config)
    return current_enclosure_config


def simulated_annealing(initial_config, enc_count, min_dist_set, min_dist, weights, initial_temperature, cooling_schedule):
    current_enclosure_config = initial_config
    current_cost = calculate_cost(current_enclosure_config, enc_count,
                                  min_dist_set, min_dist, weights)
    temperature = initial_temperature
    while temperature > 1e-10:  # set a small temperature threshold
        new_enc_config = perturb(current_enclosure_config)
        new_cost = calculate_cost(new_enc_config, enc_count,
                                  min_dist_set, min_dist, weights)

        new_cost = 5

        cost_diff = new_cost - current_cost
        acceptance_prob = acceptance_probability(cost_diff, temperature)
        random_number = np.random.rand()
        if acceptance_prob > random_number:
            current_enclosure_config = new_enc_config
            current_cost = new_cost
        temperature = cooling_schedule(temperature)

    return current_enclosure_config


def calculate_cost(new_enc_config, enc_count,
                   min_dist_set, min_dist, weights):
    return calculPointage(new_enc_config, enc_count,
                          min_dist_set, min_dist, weights)


def cooling_schedule(temperature):
    return fixed_fraction_cooling(initial_temperature=1.0, cooling_fraction=0.95)


def fixed_fraction_cooling(initial_temperature, cooling_fraction):
    temperature = initial_temperature
    while True:
        yield temperature
        temperature *= cooling_fraction


def perturb(enclosure_config):
    # TODO: swap stuff around
    return enclosure_config


def acceptance_probability(cost_diff, temperature):
    if cost_diff < 0:
        return 1.0
    else:
        return np.exp(cost_diff / temperature)


if __name__ == "__main__":
    filepath = "D:/POLY/H2023/INF8775/INF8775Lab/tp3/TP3-H23/n20_m15_V-74779.txt"
    is_print = True
    execute(filepath, is_print)
