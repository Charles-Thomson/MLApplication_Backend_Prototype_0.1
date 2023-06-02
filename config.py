"""
The configeration for the hyper perameters used in the back end of the system
"""
import numpy as np

NUMBER_OF_GENERATIONS: int = None
MAX_GENERATION_SIZE: int = None

STARTING_FITNESS_THRESHOLD: float = None
DESIERED_FIT_GENERATION_SIZE: int = None


# Used in: environment_main .py

ENV_MAP: np.array = None

ENVIRONMENT_START_STATE: int = None
MAX_EPISODE_DURATION: int = None


WEIGHT_INITALIZATION_HEURISTIC: callable = None

HIDDEN_LAYER_ACTIVATION_FUNCTION: callable = None
OUPUT_LAYER_ACTIVATION_FUNCTION = None

WEIGHTS_CROSSOVER_FUNCTIONS: callable = None
