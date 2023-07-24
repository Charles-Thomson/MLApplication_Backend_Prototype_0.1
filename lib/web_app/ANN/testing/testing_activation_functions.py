"""Testing weight initilisations"""
from math import sqrt
from numpy.random import randn, rand


# Xavier
# Used on sigmoid or tanh activation functions


def xavier() -> None:
    """Xavier weight initilisation"""
    nodes_in_previous_layer = 9  # nodes in previous layer / inputs to this layer

    # Range of the weights
    lower_bounds, upper_bounds = -(1.0 / sqrt(nodes_in_previous_layer)), (
        1.0 / sqrt(nodes_in_previous_layer)
    )

    # Generate random numbers
    numbers = rand(1000)

    # scale to the given range
    scaled = lower_bounds + numbers * (upper_bounds - lower_bounds)

    print(lower_bounds, upper_bounds)
    print(scaled.min(), scaled.max())
    print(scaled.mean(), scaled.std())


def normalized_xavier() -> None:
    """Normalized Xavier weight initilisation"""
    nodes_in_previous_layer = 9  # Inputs to layer
    nodes_in_next_layer = 9  # Outputs from layer

    # Range of the weights
    lower_bounds, upper_bounds = -(
        sqrt(6.0) / sqrt(nodes_in_previous_layer + nodes_in_next_layer)
    ), (sqrt(6.0) / sqrt(nodes_in_previous_layer + nodes_in_next_layer))

    # Rnd numbers
    numbers = rand(1000)

    # scale to the given range
    scaled = lower_bounds + numbers * (upper_bounds - lower_bounds)

    print(lower_bounds, upper_bounds)
    print(scaled.min(), scaled.max())
    print(scaled.mean(), scaled.std())


# HE weight initilization
# used for rectified linear activation function (ReLU)


def he() -> None:
    """HE weight initialization function"""
    input_nodes = 10

    # Range for the weights
    std = sqrt(2.0 / input_nodes)  # deviation

    # Rnd numbers
    numbers = randn(1000)

    # Scale numbers
    scaled = numbers * std

    print(std)
    print(scaled.min(), scaled.max())
    print(scaled.mean(), scaled.std())


he()
