"""setting of the config file"""
import numpy as np
import config
from config_functions import (
    activation_functions,
    crossover_weight_functions,
    weight_huristics,
)


def this_set_config(data: dict) -> None:
    """Set the config file based on the API data"""

    config.NUMBER_OF_GENERATIONS = data["NUMBER_OF_GENERATIONS"]
    config.MAX_GENERATION_SIZE = data["MAX_GENERATION_SIZE"]

    config.STARTING_FITNESS_THRESHOLD = data["STARTING_FITNESS_THRESHOLD"]
    config.DESIERED_FIT_GENERATION_SIZE = data["DESIERED_FIT_GENERATION_SIZE"]

    env_map_as_list: list = data["ENV_MAP"]
    config.ENV_MAP = np.array(env_map_as_list)

    config.ENVIRONMENT_START_STATE = data["ENVIRONMENT_START_STATE"]
    config.MAX_EPISODE_DURATION = data["MAX_EPISODE_DURATION"]

    hurisitcs_name: str = data["WEIGHT_INITALIZATION_HEURISTIC"]
    config.WEIGHT_INITALIZATION_HEURISTIC = weight_huristics.HURISTICS[hurisitcs_name]

    hidden_layer_activation_func_name: str = data["HIDDEN_LAYER_ACTIVATION_FUNCTION"]
    config.HIDDEN_LAYER_ACTIVATION_FUNCTION = (
        activation_functions.HIDDEN_LAYER_ACTIVATION_FUNCTIONS[
            hidden_layer_activation_func_name
        ]
    )

    output_layer_activation_func_name: str = data["OUTPUT_LAYER_ACTIVATION_FUNCTION"]
    config.OUPUT_LAYER_ACTIVATION_FUNCTION = (
        activation_functions.OUTPUT_LAYER_ACTIVATION_FUNCTIONS[
            output_layer_activation_func_name
        ]
    )

    weight_crossover_function_name: str = data["WEIGHTS_CROSSOVER_FUNCTIONS"]
    config.WEIGHTS_CROSSOVER_FUNCTIONS = (
        crossover_weight_functions.CROSSOVER_WEIGHT_FUNCTIONS[
            weight_crossover_function_name
        ]
    )
