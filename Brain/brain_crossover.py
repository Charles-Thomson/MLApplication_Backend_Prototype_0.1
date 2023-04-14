"""The crossing over of parnet brains to from a compounded new brain"""
from copy import deepcopy
import random
from typing import final
import numpy as np
from Brain.brain_instance import BrainInstance
from random import randint

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
        apply_mutation()

    return (new_input_to_hidden_weight, new_hidden_to_output_weights)


def avg_of_weights() -> np.array:
    """Generate new weigts set from the avg of two given weights sets"""
    return []


def apply_mutation():
    """Apply a mutation to the weights to give variance"""
