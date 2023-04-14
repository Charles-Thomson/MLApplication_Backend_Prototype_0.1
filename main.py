"""Main File"""

from typing import final


MAX_GENERATION_SIZE: final = 50
MAX_EPISODE_DURATION: final = 40


def first_generation() -> None:
    """Generate the first generation data"""

    fitness_threshold = 0.0
    fit_agents = 0
    desiered_fit_generation_size = 10

    while fit_agents < desiered_fit_generation_size:
        environment = NewEnvironment()
        agent_instance = new_agent()  # a.k.a new brain
        agent_fitness = agent_instance.run()
        if agent_fitness < fitness_threshold:
            continue
        save_agent(agent_instance)  # save to the db
