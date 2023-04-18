"""The environment"""
import numpy as np

from gym import Env
from Environment.environment_sightdata import collect_observation_data


ENV_MAP = [
    [2, 2, 2, 2, 2, 2],
    [2, 1, 3, 1, 3, 2],
    [2, 1, 1, 1, 1, 2],
    [2, 2, 2, 2, 1, 2],
    [2, 3, 1, 1, 3, 2],
    [2, 2, 2, 2, 2, 2],
]
# goals on 8, 10 ,22,  28


class MazeEnvironment(Env):
    """Generate a new environment"""

    def __init__(self, max_steps: int):
        self.environment_map: np.array = np.array(ENV_MAP)

        self.nrow, self.ncol = self.environment_map.shape

        # keep track of the max call for no of steps
        # Doesnt allow for starting on a lower num of steps and increasing
        self.max_steps = max_steps
        self.step_count = 0
        self.environment_start_state = 13
        self.states_visited: list[int] = []  # acts as path ?
        self.agent_state = self.environment_start_state

        self.to_coords = setup_to_coords(self.ncol)
        self.to_state = setup_to_state(self.ncol)
        self.get_location_value = setup_get_location_value(self.environment_map)

    def render(self) -> None:
        pass

    def get_environemnt_observation(self) -> np.array:
        """Returns a sight observation from the environment beased on the agent location"""
        observation_data = collect_observation_data(
            self.agent_state, self.ncol, self.environment_map
        )
        return observation_data

    def step(self, action: int) -> tuple[int, float, bool, list]:
        """Carray out the given action from the agent in ralition to the environment"""

        new_state: int = self.process_action(action)
        termination: bool = self.termination_check(new_state)
        reward: float = self.calculate_reward(new_state)
        l_list: list = []

        self.states_visited.append(self.agent_state)
        self.agent_state = new_state
        self.step_count += 1

        return new_state, termination, reward, l_list

    def termination_check(self, new_state: int) -> bool:
        """Check for termination"""

        if self.step_count >= self.max_steps:
            return True

        if self.get_location_value(self.to_coords(new_state)) == 2:
            return True

        return False

    def remove_goal(self, agent_state):
        """Check if agent reached goal - if True remove goal"""
        loc_x, loc_y = self.to_coords(agent_state)
        self.environment_map[loc_x, loc_y] = 1

    def calculate_reward(self, new_state: int):
        """Calculate the reward of the agents last action"""
        value_at_new_state = self.get_location_value(self.to_coords(new_state))

        if new_state in self.states_visited:
            return 0

        match value_at_new_state:
            case 1:  # Open Tile
                # return 0.1 + self.episode_length / 100
                return 0.15

            case 2:  # Obstical
                return 0

            case 3:  # goal
                self.remove_goal(new_state)
                return 3

    def process_action(self, action: int) -> tuple[int]:
        """Apply the given action to the location of the agent in the env"""
        hrow, hcol = self.to_coords(self.agent_state)

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

        return self.to_state((hrow, hcol))


def setup_to_coords(ncol: int) -> callable:
    """Convert state to coords"""

    def to_coords(state: int):
        return divmod(state, ncol)

    return to_coords


def setup_to_state(ncol: int) -> callable:
    """Convert coords to state"""

    def to_state(coords):
        return (coords[0] * ncol) + coords[1]

    return to_state


def setup_get_location_value(env_map: np.array) -> callable:
    """Get the loaction on the board at a set state"""

    def get_location_value(coords: tuple):
        return env_map[coords[0]][coords[1]]

    return get_location_value
