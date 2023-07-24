"""The environment"""
from functools import partial
import numpy as np

from gym import Env
from Environment.environment_sightdata import collect_observation_data

import config


class MazeEnvironment(Env):
    """Generate a new environment"""

    def __init__(self):
        self.environment_map: np.array = np.array(config.ENV_MAP)

        self.nrow, self.ncol = self.environment_map.shape

        self.max_steps = config.MAX_EPISODE_DURATION
        self.step_count = 0

        self.states_visited: list[int] = []
        self.agent_state = config.ENVIRONMENT_START_STATE

        self.to_coords = partial(to_coords, ncol=self.ncol)
        self.to_state = partial(to_state, self.ncol)
        self.get_location_value = partial(get_location_value, self.environment_map)

    def render(self) -> None:
        pass

    def get_environemnt_observation(self) -> np.array:
        """Returns a sight observation from the environment beased on the agent location"""

        return collect_observation_data(
            self.agent_state, self.ncol, self.environment_map
        )

    def step(self, action: int) -> tuple[int, float, bool, list]:
        """Carray out the given action from the agent in ralition to the environment"""
        new_state_x, new_state_y = self.process_action(action)
        termination: bool = self.termination_check(new_state_x, new_state_y)
        reward: float = 0.0

        if termination is False:
            new_state = self.to_state((new_state_x, new_state_y))
            reward: float = self.calculate_reward(new_state)
        else:
            new_state: int = 255
            reward: float = 0.0

        info: list = []  # Gym requierment

        self.states_visited.append(new_state)
        self.agent_state = new_state
        self.step_count += 1
        return new_state, termination, reward, info

    def termination_check(self, new_state_x: int, new_state_y: int) -> bool:
        """Check for termination"""

        termination_conditions: list = [
            new_state_x < 0,
            new_state_y < 0,
            self.step_count >= self.max_steps,
            self.get_location_value((new_state_x, new_state_y))
            == 2,  # Upper Index guard
        ]

        if any(termination_conditions):
            return True

        return False

    def remove_goal(self, agent_state):
        """Check if agent reached goal - if True remove goal"""
        loc_x, loc_y = self.to_coords(state=agent_state)
        self.environment_map[loc_x, loc_y] = 1

    def calculate_reward(self, new_state: int):
        """Calculate the reward of the agents last action"""
        value_at_new_state = self.get_location_value(self.to_coords(state=new_state))

        if new_state in self.states_visited:
            return 0.0

        match value_at_new_state:
            case 0:  # Open Tile
                return 0.15

            case 2:  # Obstical
                return 0.0

            case 3:  # goal
                self.remove_goal(new_state)
                return 3.0

    def process_action(self, action: int) -> tuple[int]:
        """Apply the given action to the location of the agent in the env"""
        hrow, hcol = self.to_coords(state=self.agent_state)

        match action:
            case 0:  # Up + Left
                hrow -= 1
                hcol -= 1

            case 1:  # Up
                hrow -= 1

            case 2:  # Up + Right
                hrow -= 1
                hcol += 1

            case 3:  # left
                hcol -= 1

            case 4:  # No Move
                pass

            case 5:  # Right
                hcol += 1

            case 6:  # Down + Left
                hrow += 1
                hcol -= 1

            case 7:  # Down
                hrow += 1

            case 8:  # Down + Right
                hcol += 1
                hrow += 1

        return (hrow, hcol)


def to_coords(ncol: int, state: int):
    """Convert state value to map coords"""
    return divmod(state, ncol)


def to_state(ncol: int, coords: tuple[int, int]):
    """Convert map coords to state value"""
    return (coords[0] * ncol) + coords[1]


def get_location_value(env_map: np.array, coords: tuple):
    """Get the value of a location in the env"""
    try:
        value = env_map[coords[0]][coords[1]]
        return value
    except IndexError:
        return 2  # Termination condition
