from web_page import models
import numpy as np


def format_brain_instance_for_DB(brain_instance: object) -> object:
    """Convert a brain instance into a format for the Djago DB"""
    brain_instance.set_attributes_to_bytes()


def save_as_fit_brain_instance(brain_instance: object) -> models.FitBrainInstanceModel:
    """Save the brain instance as a fit instance"""
    brain_instance.set_attributes_to_bytes()

    new_db_brain_instance = models.FitBrainInstanceModel(
        brain_id=brain_instance.brain_id,
        generation_num=brain_instance.generation_num,
        hidden_weights=brain_instance.hidden_weights,
        output_weights=brain_instance.output_weights,
        fitness=brain_instance.fitness,
        traversed_path=brain_instance.traversed_path,
        fitness_by_step=brain_instance.fitness_by_step,
    )

    return new_db_brain_instance
