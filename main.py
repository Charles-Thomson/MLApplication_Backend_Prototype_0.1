"""Main File"""
import numpy as np
from copy import deepcopy
from typing import Generator, final
from Environment.environment_main import MazeEnvironment
from Agent.maze_agent import MazeAgent
from Brain.brain_generation import new_brain_generator
from Brain.brain_instance import BrainInstance
from DataBase.database_main import save_brain_instance, get_and_format_db_data

from Logging.loggin_decorator import with_generation_logging


MAX_GENERATION_SIZE: final = 500
MAX_EPISODE_DURATION: final = 40


@with_generation_logging
def new_generation(generation_num: int, env_map: np.array) -> list:
    """New generation"""

    generation_status: bool = True
    fitness_threshold: float = 3.0
    current_generation_size: int = 0
    parents: list[BrainInstance] = []
    desiered_fit_generation_size: int = 10

    # For logging purposes
    fit_brains: list[BrainInstance] = []
    all_brains: list[BrainInstance] = []

    if generation_num > 0:
        parents: list[BrainInstance] = get_and_format_db_data(generation_num - 1)
        fitness_threshold: float = calculate_new_fitnees_threshold(parents)

    brain_generator: Generator = new_brain_generator(
        parents=parents,
        generation_num=generation_num,
        generation_size=MAX_GENERATION_SIZE,
    )

    while len(fit_brains) < desiered_fit_generation_size:
        current_generation_size += 1

        # Basic Guard
        if current_generation_size >= MAX_GENERATION_SIZE:
            generation_status = False
            break

        agent_instance: MazeAgent = MazeAgent(
            enviroment=MazeEnvironment(MAX_EPISODE_DURATION, env_map),
            agent_brain=next(brain_generator),
        )

        brain = agent_instance.run_agent()

        if brain.fitness > fitness_threshold:
            ret_brain = deepcopy(brain)
            fit_brains.append(brain)
            save_brain_instance(ret_brain)

        all_brains.append(brain)
    print(
        f"Generation Complete - Fit agents: {len(fit_brains)} - Genertion size: {current_generation_size} Generation No*: {generation_num} Fitness Threshold: {fitness_threshold}"
    )
    return fit_brains, all_brains, generation_status


def main_system(number_of_generations: int, env_map: np.array) -> None:
    """Main handling"""

    for gen_num in range(0, number_of_generations):
        fit_gen, all_gen, generation_status = new_generation(gen_num, env_map)
        if generation_status is False:  # The new generation has failed
            print(f"SYSTEM => The genration has failed {gen_num}")
            break
    print("SYSTEM => Completed Main Function ")


def get_selected_generations(selected_generations: list[int]) -> list[BrainInstance]:
    """Pull the highest fitness brain from the given generations"""
    data: list[BrainInstance] = []
    for gen in selected_generations:
        generation_data = get_and_format_db_data(gen)
        data.append(generation_data[0])  # take the highest fitness

    return data


# Needs to be refactored out
def calculate_new_fitnees_threshold(parents: list[BrainInstance]) -> float:
    """Return a fitness threshold 10% higher then given pervious generation threshold"""
    total_fitness = sum(instance.fitness for instance in parents)
    average_fitness = total_fitness / len(parents)
    new_threshold = average_fitness + ((average_fitness / 100) * 5)

    return new_threshold


def print_data(data: list[BrainInstance]):
    """debug data print"""
    for i in data:
        print(i.fitness)


if __name__ == "__main__":
    main_system(10)
    data = get_selected_generations([1])
    print_data(data)
