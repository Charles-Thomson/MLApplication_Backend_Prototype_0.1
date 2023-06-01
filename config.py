"""
The configeration for the hyper perameters used in the back end of the system
"""
from math import sqrt
import numpy as np
from numpy.random import randn, choice, rand


# Used in: main.py

NUMBER_OF_GENERATIONS: int = 1
MAX_GENERATION_SIZE: int = 2

STARTING_FITNESS_THRESHOLD: float = 3.0
DESIERED_FIT_GENERATION_SIZE: int = 10


# Used in: environment_main .py

ENV_MAP: np.array = [
    [1, 1, 1, 1, 3, 2],
    [1, 1, 1, 1, 3, 1],
    [1, 1, 1, 1, 1, 1],
    [1, 1, 1, 2, 1, 3],
    [2, 1, 1, 1, 1, 1],
    [2, 2, 3, 1, 3, 2],
]

ENVIRONMENT_START_STATE: int = 8
MAX_EPISODE_DURATION: int = 10

# Used in brain_generation.py

# Weight initalizations

# HE -> used with rectified linear activation function ReLU


def he_weight_init(layer_connections: tuple[int, int]) -> list[float]:
    """HE weight initalization"""
    input_layer_size, _ = layer_connections
    std = sqrt(2.0 / input_layer_size)
    numbers = randn(500)
    scaled = np.round(numbers * std, decimals=3)

    return scaled


def xavier_weight_init(layer_connections: tuple[int, int]) -> list[float]:
    """xzavier weight initalizations"""
    input_layer_size, _ = layer_connections

    upper_bounds, lower_bounds = -(1 / sqrt(input_layer_size)), (
        1 / sqrt(input_layer_size)
    )
    numbers = rand(1000)

    scaled = np.round(
        lower_bounds + numbers * (upper_bounds - lower_bounds), decimals=3
    )

    return scaled


def normalized_xavier_weight_init(layer_connections: tuple[int, int]) -> list[float]:
    """normalized xzavier weight initalizations"""
    input_layer_size, output_layer_size = layer_connections
    n = input_layer_size + output_layer_size
    lower_bounds, upper_bounds = -(sqrt(6.0) / sqrt(n)), (sqrt(6.0) / sqrt(n))

    # Numbers
    numbers = rand(500)

    # Scale numbers to bounds
    scaled = np.round(
        lower_bounds + numbers * (upper_bounds - lower_bounds), decimals=3
    )

    return scaled


WEIGHT_INITALIZATION_HEURISTIC: callable = he_weight_init


# ACTIVATION FUNCTIONS


# Linear activations
def linear_activation_function(value: float) -> float:
    """Returns given value - gives linear result"""
    return np.round(value, deciamls=3)


# None Linear activations
def rectified_linear_activation_activation_function(value: float) -> float:
    """ReL activation function - x is 0 or x"""
    return np.round(max(0.0, value), decimals=3)


def leaky_rectified_linear_activation_activation_function(value: float) -> float:
    """Leaky ReL activation function - x is 0.01*x or x"""
    if value > 0:
        return value
    else:
        return 0.01 * value


def sigmoid_activation_fucntion(value: float) -> float:
    """Sigmoidal activation function - x is between 0 -> 1"""
    return 1 / (1 + np.exp(value))


def hyperbolic_tangent_activation_function(value: float) -> float:
    """tanh activation funtion - gives x is between -1.0 and 1.0"""
    return (np.exp(value) - np.exp(-value)) / (np.exp(value) + np.exp(-value))


HIDDEN_LAYER_ACTIVATION_FUNCTION: callable = (
    rectified_linear_activation_activation_function
)


# OUPUT Layer activation functions


def argmax_activation(vector: np.array) -> int:
    """ArgMax output layer activation function"""
    return np.argmax(vector)


def soft_argmax_activation(vector: np.array) -> int:
    """soft argmax oultput layer activation fucntion"""
    vector_exp = np.exp(vector)
    vector_sum = vector_exp / vector_exp.sum()
    return np.argmax(vector_sum)


OUPUT_LAYER_ACTIVATION_FUNCTION = soft_argmax_activation
