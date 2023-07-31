"""The crossing over of parnet brains to from a compounded new brain"""
from copy import deepcopy
import random
from typing import final
from random import randint
from ANN.Brain.brain_instance import BrainInstance
import numpy as np
from ANN.config import config


MUTATION_THRESHOLD: final = 50


def weights_crossover(parents: list[BrainInstance]) -> tuple[np.array, np.array]:
    """Select and compund two parents weight sets to"""
    weights_crossover_function: callable = config.WEIGHTS_CROSSOVER_FUNCTIONS

    val: int = len(parents)
    weightings: list[float] = tuple(val / i for i in range(1, val + 1))

    parent_a, parent_b = random.choices(parents, weights=weightings, k=2)

    parent_a: BrainInstance = deepcopy(parent_a)
    parent_b: BrainInstance = deepcopy(parent_b)

    new_input_to_hidden_weight = weights_crossover_function(
        parent_a.hidden_weights, parent_b.hidden_weights
    )

    new_hidden_to_output_weights = weights_crossover_function(
        parent_a.output_weights, parent_b.output_weights
    )

    if randint(0, 100) > MUTATION_THRESHOLD:
        random_selection = random.randint(0, 1)
        if random_selection == 0:
            new_input_to_hidden_weight = apply_mutation(new_input_to_hidden_weight)

        if random_selection == 1:
            new_hidden_to_output_weights = apply_mutation(new_hidden_to_output_weights)

    return (new_input_to_hidden_weight, new_hidden_to_output_weights)


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
