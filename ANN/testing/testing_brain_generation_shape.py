"""testing brain generation shape"""
from typing import Generator
import numpy as np
from Brain.brain_instance import BrainInstance
from Brain.brain_generation import merged_new_generation_generator


def testing_shape_on_random():
    """testing docstring - f.u"""

    brain_generator: Generator = merged_new_generation_generator(
        [], generation_num=0, generation_size=3
    )

    test_brain = next(brain_generator)

    hidden_shape = test_brain.hidden_weights.shape
    output_shape = test_brain.output_weights.shape

    print(test_brain)
    print(f"Hidden Weights shape => {hidden_shape}")
    print(f"Output Weights shape => {output_shape}")


def testing_shape_on_new_gen():
    """testing docstring - f.u"""

    brain_generator: Generator = merged_new_generation_generator(
        [], generation_num=0, generation_size=6
    )

    brain_a = next(brain_generator)
    brain_b = next(brain_generator)
    brain_c = next(brain_generator)

    parnets = [brain_a, brain_b, brain_c]

    none_random_generator: Generator = merged_new_generation_generator(
        parnets, generation_num=1, generation_size=6
    )

    test_brain = next(none_random_generator)

    hidden_shape = test_brain.hidden_weights.shape
    output_shape = test_brain.output_weights.shape
    brain_generation_num = test_brain.generation_num

    print(brain_generation_num)
    print(f"Hidden Weights shape => {hidden_shape}")
    print(f"Output Weights shape => {output_shape}")

    test_brain.set_attributes_to_bytes()

    # print(f"Hidden Weights => {test_brain.hidden_weights }")

    test_brain.get_attributes_from_bytes()

    print(test_brain.hidden_weights.shape)
    print(test_brain.output_weights.shape)

    new_hidden_shape = test_brain.hidden_weights.reshape(24, -1)
    new_output_shape = test_brain.output_weights.reshape(9, -1)

    print(f"New Hidden Weights shape => {new_hidden_shape.shape}")
    print(f"New Ouput Weights shape => {new_output_shape.shape}")


testing_shape_on_new_gen()
