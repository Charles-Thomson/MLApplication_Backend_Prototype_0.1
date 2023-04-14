"""Used to look along sight lines from a given location in the environment"""
from itertools import chain
import numpy as np


ENV_MAP = [
    [2, 2, 2, 2, 2, 2],
    [2, 1, 3, 1, 3, 2],
    [2, 1, 1, 1, 1, 2],
    [2, 2, 2, 2, 1, 2],
    [2, 3, 1, 1, 3, 2],
    [2, 2, 2, 2, 2, 2],
]


def collect_observation_data(agent_state: int, ncol: int, env_map: np.array):
    """Collect the observation data based on the agets location in the environment"""
    loc_row, loc_col = to_coords(agent_state, ncol=ncol)

    values_up: list = env_map[loc_row - 1 :: -1, loc_col]
    values_up_right: list = np.diagonal(env_map[loc_row::-1, loc_col:])[1:]
    values_right = env_map[loc_row, loc_col + 1 :]
    values_down_right: list = np.diagonal(env_map[loc_row:, loc_col:])[1:]
    values_down: list = env_map[loc_row + 1 :, loc_col]
    values_down_left: list = np.diagonal(env_map[loc_row:, loc_col::-1])[1:]
    values_left: list = env_map[loc_row, loc_col - 1 :: -1]
    values_up_left: list = np.diagonal(env_map[loc_row::-1, loc_col::-1])[1:]

    sight_lines = [
        values_up_left,
        values_up,
        values_up_right,
        values_left,
        values_right,
        values_down_left,
        values_down,
        values_down_right,
    ]

    observation_data = list(map(check_sight_line, sight_lines))
    observation_data = list(chain(*observation_data))
    return observation_data


def check_sight_line(sight_line: list) -> list[float, float, float]:
    """Check along the given sightline and determin activation"""
    for distance, value in enumerate(sight_line):
        if value == 2:
            return [round(0.1 * distance, 3), 1 / (distance + 1), 0.0]
        if value == 3:
            return [round(0.1 * distance, 3), 0.0, 1 / (distance + 1)]

    return ValueError("No boundry on sightline")


def to_coords(state: int, ncol: int) -> tuple:
    """Convert state to coords"""
    return divmod(state, ncol)

