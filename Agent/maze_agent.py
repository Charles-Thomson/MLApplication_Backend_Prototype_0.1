"""Maze agent creation and action process"""
from Environment.environemnt_main import MazeEnvironment


class MazeAent:
    """Maze agent instance"""

    def __init__(self, enviroment: object, agent_brain: object):
        self.environment: MazeEnvironment = enviroment
        self.brain: object = agent_brain

    def run_agent(self) -> tuple:
        """Run the agent through the environment"""
        path: list = []
        fitness: float = 0.0
        termination: bool = False

        while termination is False:
            observation_data = self.environment.get_environemnt_observation()
            action = self.brain.detemin_action(observation_data)

            n_s, ter, rew, _ = self.environment.step(action)

            path.append(n_s)
            termination = ter
            fitness += rew

        # May move fit and path inside of the brain
        return self.brain, fitness, path
