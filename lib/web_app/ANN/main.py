"""Main File"""
from copy import deepcopy
from typing import Generator

from ANN.Environment.environment_main import MazeEnvironment
from ANN.Agent.maze_agent import MazeAgent
from ANN.Brain.brain_generation import new_brain_generator
from ANN.Brain.brain_instance import BrainInstance

# from ANN.DataBase.database_main import save_brain_instance, get_and_format_db_data
from ANN.DataBase.database_all_brains import save_all_brain_instance

from ANN.Logging.loggin_decorator import with_generation_logging

from web_app.web_page import db_functions

from ANN.config import config


@with_generation_logging
def new_generation(generation_num: int) -> list:
    """New generation"""

    fitness_threshold: float = config.STARTING_FITNESS_THRESHOLD
    desiered_fit_generation_size: int = config.DESIERED_FIT_GENERATION_SIZE
    generation_status: bool = True
    current_generation_size: int = 0
    parents: list[BrainInstance] = []

    # For logging purposes
    fit_brains: list[BrainInstance] = []
    all_brains: list[BrainInstance] = []

    if generation_num > 0:
        # Getting from the Fit Brains Model
        parents: list[BrainInstance] = db_functions.get_and_format_db_data(
            generation_num=(generation_num - 1), model_type="fit"
        )
        fitness_threshold: float = calculate_new_fitnees_threshold(parents)

    brain_generator: Generator = new_brain_generator(
        parents=parents,
        generation_num=generation_num,
        generation_size=config.MAX_GENERATION_SIZE,
    )

    while len(fit_brains) < desiered_fit_generation_size:
        current_generation_size += 1

        # Basic Guard
        if current_generation_size >= config.MAX_GENERATION_SIZE:
            generation_status = False
            break

        agent_instance: MazeAgent = MazeAgent(
            enviroment=MazeEnvironment(),
            agent_brain=next(brain_generator),
        )

        brain = agent_instance.run_agent()

        if brain.fitness > fitness_threshold:
            ret_brain = deepcopy(brain)
            fit_brains.append(brain)
            db_functions.save_brain_instance(brain_instance=ret_brain, model_type="fit")

        all_brains.append(brain)
        all_brain_instance = deepcopy(brain)

        db_functions.save_brain_instance(
            brain_instance=all_brain_instance, model_type="general"
        )
    print(
        f"Generation Complete - Fit agents: {len(fit_brains)} - Genertion size: {current_generation_size} Generation No*: {generation_num} Fitness Threshold: {fitness_threshold}"
    )
    return fit_brains, all_brains, generation_status


def main_system() -> int:
    """Main handling"""
    print("SYSTEM : RUNNING MAIN SYSTEM")
    total_generations: int = 0

    for gen_num in range(0, config.NUMBER_OF_GENERATIONS):
        # can order here based on all vs fit gens
        fit_gen, all_gen, generation_status = new_generation(gen_num)
        total_generations = gen_num
        if generation_status is False:  # The new generation has failed
            print(f"SYSTEM => The genration has failed {gen_num}")
            break

    print("SYSTEM => Completed Main Function ")
    return total_generations


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
    main_system()
    # data = get_selected_generations([1])
    # print_data(data)
