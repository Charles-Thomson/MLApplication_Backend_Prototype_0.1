"""
The configeration for the hyper perameters used in the back end of the system
"""
import numpy as np


# Used in: main.py


NUMBER_OF_GENERATIONS: int = 10
MAX_GENERATION_SIZE: int = 1000
MAX_EPISODE_DURATION: int = 10

STARTING_FITNESS_THRESHOLD: float = 3.0
DESIERED_FIT_GENERATION_SIZE: int = 10

ENV_MAP: np.array = [
    [1, 1, 1, 1, 3, 2],
    [1, 1, 1, 1, 3, 1],
    [1, 1, 1, 1, 1, 1],
    [1, 1, 1, 2, 1, 3],
    [2, 1, 1, 1, 1, 1],
    [2, 2, 3, 1, 3, 2],
]


# Used in: main.py

ENVIRONMENT_START_STATE: int = 8
