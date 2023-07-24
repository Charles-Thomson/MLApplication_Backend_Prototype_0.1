""""""
import numpy as np


# ENV_MAP = [
#     [2, 2, 2, 2, 2, 2],
#     [2, 1, 3, 1, 3, 2],
#     [2, 1, 1, 1, 1, 2],
#     [2, 2, 2, 2, 1, 2],
#     [2, 3, 1, 1, 3, 2],
#     [2, 2, 2, 2, 2, 2],
# ]
# agent_state 14
# n


# better approach t0 the sight data
def new_sight_data() -> None:
    """"""
    a = np.array(ENV_MAP)
    # r = starting row - c = start col
    # to coords call on agent state - unpacked
    r = 2
    c = 2

    values_up: list = a[r - 1 :: -1, c]
    values_up_right: list = np.diagonal(a[r::-1, c:])[1:]
    values_right = a[r, c + 1 :]
    values_down_right: list = np.diagonal(a[r:, c:])[1:]
    values_down: list = a[r + 1 :, c]
    values_down_left: list = np.diagonal(a[r:, c::-1])[1:]
    values_left: list = a[r, c - 1 :: -1]
    values_up_left: list = np.diagonal(a[r::-1, c::-1])[1:]

    # print(values_down_right)

    location_data = [
        values_up_left,
        values_up,
        values_up_right,
        values_left,
        values_right,
        values_down_left,
        values_down,
        values_down_right,
    ]

    observation_data = list(map(check_sight_line, location_data))
    # observation_data = list(chain(*observation_data))
    # print(observation_data)


def check_sight_line(direction_values: list) -> list[float, float, float]:
    """Check along the given sightline and determin activation"""
    for distance, value in enumerate(direction_values):
        if value == 2:
            return [round(0.1 * distance, 3), 1 / (distance + 1), 0.0]
        if value == 3:
            return [round(0.1 * distance, 3), 0.0, 1 / (distance + 1)]


def check_sight_line(sight_line: list[int]) -> list[float]:
    """Return the activation along each sight given sight line"""
    sightline_activation = [0.0, 0.0, 0.0]
    for distance, value in enumerate(sight_line):
        if value == 2:
            sightline_activation[0] = round(0.1 * distance, 3)
            sightline_activation[1] = 1 / (distance + 1)
            sightline_activation[2] = 0.0
            break

        if value == 3:
            sightline_activation[0] = round(0.1 * distance, 3)
            sightline_activation[1] = 0.0
            sightline_activation[2] = 1 / (distance + 1)
            break

    return sightline_activation


new_sight_data()


def to_coords(state: int, ncol: int) -> tuple:
    """Convert state to coords"""
    return divmod(state, ncol)
