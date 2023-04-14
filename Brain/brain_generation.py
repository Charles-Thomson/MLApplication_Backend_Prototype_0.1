"""Core functunality and creation of the brains used by agents"""
from typing import final
import uuid
from math import sqrt
from numpy import np
from numpy.random import randn, choice
from brain_instance import BrainInstance


INPUT_LAYER_SIZE: final = 24
INPUT_TO_HIDDEN_CONNECTIONS: final = (24, 9)
HIDDEN_TO_OUTPUT_CONNECTIONS: final = (9, 9)


def setup_generate_generational_brain(
    parents: list[BrainInstance], generation_num: int
):
    """Curry the parents and generation num for this generation"""

    def generate_generational_brain() -> BrainInstance:
        """Generate a Brain Isnatnce with weights based on given parents"""
        hidden_weights, output_weights = brain_generation.parent_crossover(parents)
        brain_id = generate_brain_id()
        new_brain = BrainInstance(
            brain_id, generation_num, hidden_weights, output_weights
        )

        return new_brain

    return generate_generational_brain


def generate_generation_zero(generation_size: int) -> np.array:
    """Generate the zero generation with random weights"""
    generation_zero: list[BrainInstance] = []

    for _ in generation_size:
        hidden_weights: np.array = generate_rand_weights(
            INPUT_LAYER_SIZE, INPUT_TO_HIDDEN_CONNECTIONS
        )
        ouput_weights: np.array = generate_rand_weights(
            INPUT_LAYER_SIZE, HIDDEN_TO_OUTPUT_CONNECTIONS
        )
        brain_id = generate_brain_id()
        generation_no = 0
        new_brain = BrainInstance(
            brain_id, generation_no, hidden_weights, ouput_weights
        )

        generation_zero.append(new_brain)

    return generation_zero


def generate_brain_id() -> str:
    """Generate a random brain_ID"""
    brain_id = uuid.uuid4()
    brain_id = str(brain_id)[10]
    return brain_id


def generate_rand_weights(input_layer_size: int, layer_connections: tuple[int, int]):
    """Generate random weigths between to layers of a specified sizes"""

    sending_layer, reciving_layer = layer_connections
    rand_weights: np.array = [
        [generate_rand_value(input_layer_size) for i in range(reciving_layer)]
        for i in range(sending_layer)
    ]

    return rand_weights


def generate_rand_value(input_layer_size: int) -> float:
    """Generate a rnadom value based on the size of the given input layer - choice, round, randn called from np"""
    std = sqrt(2.0 / input_layer_size)
    numbers = randn(500)
    scaled = numbers * std
    value = choice(scaled)
    value = np.round(value, decimal=3)

    return value
