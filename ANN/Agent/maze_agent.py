"""Maze agent creation and action process"""
import numpy as np


class MazeAgent:
    """Maze agent instance"""

    def __init__(self, enviroment: object, agent_brain: object):
        self.environment: object = enviroment
        self.brain: object = agent_brain

    def run_agent(self) -> tuple:
        """Run the agent through the environment"""
        path: list[int] = []
        fitness_by_step: list[float] = []
        fitness: float = 0.0
        termination: bool = False

        while termination is False:
            observation_data = self.environment.get_environemnt_observation()
            action = self.brain.determin_action(observation_data)

            n_state, termination_status, reward, _ = self.environment.step(action)

            path.append(n_state)
            termination = termination_status
            fitness += reward
            fitness_by_step.append(fitness)

        # May move fit and path inside of the brain

        self.brain.fitness = fitness
        self.brain.traversed_path = path
        self.brain.fitness_by_step = np.array(fitness_by_step)

        return self.brain
