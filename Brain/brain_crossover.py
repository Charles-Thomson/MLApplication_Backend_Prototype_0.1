"""The crossing over of parnet brains to from a compounded new brain"""
from copy import deepcopy
import random
from typing import final
from random import randint
from Brain.brain_instance import BrainInstance
import numpy as np


MUTATION_THRESHOLD: final = 50


def weights_crossover(parents: list[BrainInstance]) -> tuple[np.array, np.array]:
    """Select and compund two parents weight sets to"""
    val: int = len(parents)
    weightings: list[float] = tuple(val / i for i in range(1, val + 1))

    parent_a, parent_b = random.choices(parents, weights=weightings, k=2)

    parent_a: BrainInstance = deepcopy(parent_a)
    parent_b: BrainInstance = deepcopy(parent_b)

    new_input_to_hidden_weight = avg_of_weights(
        parent_a.hidden_weights, parent_b.hidden_weights
    )

    new_hidden_to_output_weights = avg_of_weights(
        parent_a.output_weights, parent_b.output_weights
    )

    if randint(0, 100) > MUTATION_THRESHOLD:
        random_selection = random.randint(0, 1)
        if random_selection == 0:
            new_input_to_hidden_weight = apply_mutation(new_input_to_hidden_weight)

        if random_selection == 1:
            new_hidden_to_output_weights = apply_mutation(new_hidden_to_output_weights)

    return (new_input_to_hidden_weight, new_hidden_to_output_weights)


def avg_of_weights(weight_set_a: np.array, weight_set_b: np.array) -> np.array:
    """Generate new weigts set from the avg of two given weights sets"""
    new_weight_set_sum: np.array = np.add(weight_set_a, weight_set_b)
    new_weight_set: np.array = np.divide(new_weight_set_sum, 2)
    return new_weight_set


def apply_mutation(weight_set: np.array) -> np.array:
    """Apply a +/- 10% mutation to the weights to give variance"""

    weight_set_shape: tuple = weight_set.shape

    # select random weight from set

    x_loc: int = random.randrange(weight_set_shape[0])
    y_loc: int = random.randrange(weight_set_shape[1])

    weight_to_mutate: float = weight_set[x_loc][y_loc]

    mutation_amount: int = random.randint(1, 10)
    positive_mutation: float = weight_to_mutate - (weight_to_mutate / mutation_amount)
    negitive_mutation: float = weight_to_mutate + (weight_to_mutate / mutation_amount)

    mutation: float = random.choice((positive_mutation, negitive_mutation))

    weight_set[x_loc][y_loc] = mutation

    return weight_set
