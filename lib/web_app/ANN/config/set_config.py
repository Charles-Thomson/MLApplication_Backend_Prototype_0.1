"""setting of the config file"""
import numpy as np
from ANN.config import config
from ANN.config_functions import (
    activation_functions,
    crossover_weight_functions,
    weight_huristics,
)


def this_set_config(data: dict) -> None:
    """Set the config file based on the API data"""

    print("SYSTEM: IN SET CONFIG")
    print(type(data))
    print(str(data["NUMBER_OF_GENERATIONS"]))

    config.NUMBER_OF_GENERATIONS = int(data["NUMBER_OF_GENERATIONS"])
    config.MAX_GENERATION_SIZE = int(data["MAX_GENERATION_SIZE"])

    config.STARTING_FITNESS_THRESHOLD = float(data["STARTING_FITNESS_THRESHOLD"])
    config.DESIERED_FIT_GENERATION_SIZE = int(data["DESIRED_FIT_GENERATION_SIZE"])

    env_map_string: str = data["ENV_MAP"]
    env_map_unshaped: np.array = np.fromstring(env_map_string, dtype=int, sep=",")
    reshape_val: int = int(data["ENV_MAP_DIMENSIONS"])
    env_map_shaped: np.array = env_map_unshaped.reshape(reshape_val, -1)
    config.ENV_MAP = env_map_shaped

    config.ENVIRONMENT_START_STATE = int(data["ENVIRONMENT_START_STATE"])
    config.MAX_EPISODE_DURATION = int(data["MAX_EPISODE_DURATION"])

    hurisitcs_name: str = data["WEIGHT_INITIALIZATION_HEURISTIC"]
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

    weight_crossover_function_name: str = data["WEIGHTS_CONCATENATION_FUNCTION"]
    config.WEIGHTS_CROSSOVER_FUNCTIONS = (
        crossover_weight_functions.CROSSOVER_WEIGHT_FUNCTIONS[
            weight_crossover_function_name
        ]
    )

    print(config.ENV_MAP, config.STARTING_FITNESS_THRESHOLD)
