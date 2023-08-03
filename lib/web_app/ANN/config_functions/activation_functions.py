"""
Activation functions used in the ANN
"""
import numpy as np

# Linear activations


def linear_activation_function(value: float) -> float:
    """Returns given value - gives linear result"""
    return value


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


# OUPUT Layer activation functions


def argmax_activation(vector: np.array) -> int:
    """ArgMax output layer activation function"""
    return np.argmax(vector)


def soft_argmax_activation(vector: np.array) -> int:
    """soft argmax oultput layer activation fucntion"""
    vector_exp = np.exp(vector)
    vector_sum = vector_exp / vector_exp.sum()
    return np.argmax(vector_sum)


def get_hidden_activation_func(func_name: str) -> callable:
    """Returns a hidden layer activation function -
    Available:
    "Linear"
    "Relu"
    "Leaky Relu"
    "Sigmoid"
    """
    functions: dict = {
        "linear": linear_activation_function,
        "Relu": rectified_linear_activation_activation_function,
        "Leaky Relu": leaky_rectified_linear_activation_activation_function,
        "Sigmoid": sigmoid_activation_fucntion,
    }
    return functions[func_name]


def get_output_activation_func(func_name: str) -> callable:
    """Returns a output layer activation function
    Available:
    "Arg max"
    "Soft max"
    """

    functions: dict = {
        "Arg max": argmax_activation,
        "Soft max": soft_argmax_activation,
    }

    return functions["func_name"]
