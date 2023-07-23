"""
The DEFAULT configeration for the hyper perameters used in the back end of the system
"""
import numpy as np
from config_functions import (
    activation_functions,
    crossover_weight_functions,
    weight_huristics,
)


# Used in: main.py

NUMBER_OF_GENERATIONS_DEFAULT: int = 1
MAX_GENERATION_SIZE_DEFAULT: int = 2

STARTING_FITNESS_THRESHOLD_DEFAULT: float = 3.0
DESIERED_FIT_GENERATION_SIZE_DEFAULT: int = 10


# Used in: environment_main .py

ENV_MAP_DEFAULT: np.array = [
    [1, 1, 1, 1, 3, 2],
    [1, 1, 1, 1, 3, 1],
    [1, 1, 1, 1, 1, 1],
    [1, 1, 1, 2, 1, 3],
    [2, 1, 1, 1, 1, 1],
    [2, 2, 3, 1, 3, 2],
]

ENVIRONMENT_START_STATE_DEFAULT: int = 8
MAX_EPISODE_DURATION_DEFAULT: int = 10


WEIGHT_INITALIZATION_HEURISTIC_DEFAULT: callable = (
    weight_huristics.he_weight_init_generator
)

HIDDEN_LAYER_ACTIVATION_FUNCTION_DEFAULT: callable = (
    activation_functions.rectified_linear_activation_activation_function
)
OUPUT_LAYER_ACTIVATION_FUNCTION_DEFAULT = activation_functions.soft_argmax_activation

WEIGHTS_CROSSOVER_FUNCTIONS_DEFAULT: callable = (
    crossover_weight_functions.crossover_weights_average
)
