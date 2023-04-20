"""Core functunality and creation of the brains used by agents"""
from typing import final
import uuid
from math import sqrt
import numpy as np
from numpy.random import randn, choice
from Brain.brain_instance import BrainInstance
from Brain.brain_crossover import weights_crossover


INPUT_LAYER_SIZE: final = 24
INPUT_TO_HIDDEN_CONNECTIONS: final = (24, 9)
HIDDEN_TO_OUTPUT_CONNECTIONS: final = (9, 9)


def new_brain_generator(
    parents: list[BrainInstance], generation_num: int, generation_size: int
) -> BrainInstance:
    """Generator for the creation of new brain instances - generation 0 has random weights"""

    for _ in range(generation_size):
        if generation_num == 0:
            hidden_weights: np.array = generate_rand_weights(
                INPUT_LAYER_SIZE, INPUT_TO_HIDDEN_CONNECTIONS
            )
            output_weights: np.array = generate_rand_weights(
                INPUT_LAYER_SIZE, HIDDEN_TO_OUTPUT_CONNECTIONS
            )
        else:
            hidden_weights, output_weights = weights_crossover(parents)

        brain_id: str = generate_brain_id()

        new_brain: BrainInstance = BrainInstance(
            brain_id, generation_num, hidden_weights, output_weights
        )

        yield new_brain


def generate_brain_id() -> str:
    """Generate a random brain_ID"""
    brain_id = uuid.uuid4()
    brain_id = str(brain_id)[:10]
    return brain_id


def generate_rand_weights(
    input_layer_size: int, layer_connections: tuple[int, int]
) -> np.array:
    """Generate random weigths between to layers of a specified sizes"""

    sending_layer, reciving_layer = layer_connections
    rand_weights: np.array = np.array(
        [
            [generate_rand_value(input_layer_size) for i in range(reciving_layer)]
            for i in range(sending_layer)
        ]
    )

    return rand_weights


def generate_rand_value(input_layer_size: int) -> float:
    """Generate a rnadom value based on the size of the given input layer - choice, round, randn called from np"""
    std = sqrt(2.0 / input_layer_size)
    numbers = randn(500)
    scaled = numbers * std
    value = choice(scaled)
    value = np.round(value, decimals=3)

    return value
