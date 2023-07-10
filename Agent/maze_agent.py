"""Maze agent creation and action process"""


class MazeAgent:
    """Maze agent instance"""

    def __init__(self, enviroment: object, agent_brain: object):
        self.environment: object = enviroment
        self.brain: object = agent_brain

    def run_agent(self) -> tuple:
        """Run the agent through the environment"""
        path: list = []
        fitness: float = 0.0
        termination: bool = False

        while termination is False:
            observation_data = self.environment.get_environemnt_observation()
            action = self.brain.determin_action(observation_data)

            n_state, termination_status, reward, _ = self.environment.step(action)

            path.append(n_state)
            termination = termination_status
            fitness += reward

        # May move fit and path inside of the brain

        self.brain.fitness = fitness
        self.brain.traversed_path = path

        return self.brain
