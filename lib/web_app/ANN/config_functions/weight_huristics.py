"""
Weight initialization huristics 
"""
from math import sqrt
import numpy as np
from numpy.random import randn, rand


def he_weight_init(layer_connections: tuple[int, int]) -> list[float]:
    """HE weight initalization"""
    input_layer_size, _ = layer_connections
    std = sqrt(2.0 / input_layer_size)
    numbers = randn(500)
    scaled = np.round(numbers * std, decimals=3)

    return scaled


def he_weight_init_generator(layer_connections: tuple[int, int]) -> list[float]:
    """HE weight initalization"""
    input_layer_size, output_layer_size = layer_connections

    std = sqrt(2.0 / input_layer_size)
    n = input_layer_size * output_layer_size
    numbers = randn(n)
    scaled = np.round(numbers * std, decimals=3)
    for element in scaled:
        yield element


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


def xavier_weight_init_generator(layer_connections: tuple[int, int]) -> list[float]:
    """xzavier weight initalizations"""
    input_layer_size, output_layer_size = layer_connections

    upper_bounds, lower_bounds = -(1 / sqrt(input_layer_size)), (
        1 / sqrt(input_layer_size)
    )
    n = input_layer_size * output_layer_size
    numbers = rand(n)

    scaled = np.round(
        lower_bounds + numbers * (upper_bounds - lower_bounds), decimals=3
    )
    for element in scaled:
        yield element


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


def normalized_xavier_weight_init_generator(
    layer_connections: tuple[int, int]
) -> list[float]:
    """normalized xzavier weight initalizations"""
    input_layer_size, output_layer_size = layer_connections
    n = input_layer_size + output_layer_size
    lower_bounds, upper_bounds = -(sqrt(6.0) / sqrt(n)), (sqrt(6.0) / sqrt(n))

    n_numbers = input_layer_size * output_layer_size

    # Numbers
    numbers = rand(n_numbers)
    # Scale numbers to bounds
    scaled = np.round(
        lower_bounds + numbers * (upper_bounds - lower_bounds), decimals=3
    )
    for element in scaled:
        yield element


def get_weight_huristics(huristics_name: str) -> callable:
    """Returns a weight initialization huristic
    Available:
    "HE"
    "xavier"
    "normalized xavier"
    """

    huristics: dict = {
        "HE": he_weight_init_generator,
        "xavier": xavier_weight_init_generator,
        "normalized xavier": normalized_xavier_weight_init_generator,
    }
    return huristics[huristics_name]
