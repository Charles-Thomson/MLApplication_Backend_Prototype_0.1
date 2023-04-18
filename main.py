"""Main File"""

from copy import deepcopy
from typing import Generator, final
from Environment.environment_main import MazeEnvironment
from Agent.maze_agent import MazeAgent
from Brain.brain_generation import gen_zero_generator, setup_generate_generational_brain
from Brain.brain_instance import BrainInstance
from DataBase.database_main import save_brain_instance, get_db_data
from Logging.loggin_decorator import with_generation_zero_logging


MAX_GENERATION_SIZE: final = 50
MAX_EPISODE_DURATION: final = 40


def generation_zero() -> list:
    """Generate the first generation data"""
    print("Starting generation Zero")

    fitness_threshold: float = 1.0
    fit_agents: int = 0
    desiered_fit_generation_size: int = 4

    environment: MazeEnvironment = MazeEnvironment(MAX_EPISODE_DURATION)
    brains: Generator = gen_zero_generator(MAX_GENERATION_SIZE)
    fit_brains: list[BrainInstance] = []

    while fit_agents < desiered_fit_generation_size:
        environment_instance: MazeEnvironment = deepcopy(environment)
        brain: BrainInstance = next(brains)

        agent_instance: MazeAgent = MazeAgent(
            enviroment=environment_instance, agent_brain=brain
        )
        returned_brain: BrainInstance = agent_instance.run_agent()

        if returned_brain.fitness > fitness_threshold:
            # save_brain_instance(returned_brain)  # save to the db
            fit_agents += 1
            fit_brains.append(returned_brain)
            save_brain_instance(returned_brain)

    # return is need for the decorator
    return fit_brains


def new_generation(generation_num: int) -> list:
    """New generation"""

    parents: list[BrainInstance] = db_data_formatting(generation_num=generation_num - 1)
    print(parents)
    fitness_threshold: float = calculate_new_fitnees_threshold(parents)
    print(fitness_threshold)
    fit_agents: int = 0
    desiered_fit_generation_size: int = 4

    environment: MazeEnvironment = MazeEnvironment(MAX_EPISODE_DURATION)
    new_brain = setup_generate_generational_brain(
        parents=parents, generation_num=generation_num
    )

    fit_brains: list[BrainInstance]

    while fit_agents < desiered_fit_generation_size:
        environment_instance: MazeEnvironment = deepcopy(environment)
        brain: BrainInstance = new_brain()
        agent_instance: MazeAgent = MazeAgent(
            enviroment=environment_instance, agent_brain=brain
        )

        returned_brain: BrainInstance = agent_instance.run_agent()

        if returned_brain.fitness > fitness_threshold:
            print(f"New fit brain instance => {returned_brain.brain_id}")
            fit_agents += 1
            fit_brains.append(returned_brain)
            save_brain_instance(returned_brain)


def calculate_new_fitnees_threshold(parents: list[BrainInstance]) -> float:
    """Return a fitness threshold 10% higher then given pervious generation threshold"""
    total_fitness = sum(instance.fitness for instance in parents)
    average_fitness = total_fitness / len(parents)
    new_threshold = average_fitness + ((average_fitness / 100) * 10)

    return new_threshold


def db_data_formatting(generation_num: int) -> list[BrainInstance]:
    """Pull and format the relervent Brain instnce generation from the database"""
    brain_instances: list[BrainInstance] = []
    data = get_db_data(generation_num)
    for instance in data:
        instance.get_attributes_from_bytes()
        brain_instances.append(instance)

    ordered_brian_instances: list[BrainInstance] = sorted(
        brain_instances, key=lambda x: x.fitness, reverse=True
    )

    return ordered_brian_instances


if __name__ == "__main__":
    new_generation_number: int = 2
    data = db_data_formatting(1)
    holder = data[0]
    print(holder.hidden_weights.shape)
    # holder = generation_zero()
    # db_data = get_db_data()
    # new_generation(new_generation_number)
