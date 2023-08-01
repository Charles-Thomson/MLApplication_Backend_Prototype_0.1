from django.db import models

from ANN.Brain.brain_instance import BrainInstance

from web_page.models import (
    AllBrainInstanceModel,
    FitBrainInstanceModel,
    AVAILABLE_MODELS,
)

from web_page import brain_instance_handling


def save_brain_instance(brain_instance: BrainInstance, model_type: str) -> None:
    """Save the given Brain Instance to the Django DB"""

    new_brain_instance_as_model: models.Model = (
        brain_instance_handling.brain_instance_to_model(
            brain_instance, model_type=model_type
        )
    )

    new_brain_instance_as_model.save()


def get_and_format_db_data(generation_num: int, model_type: str) -> list[BrainInstance]:
    """Get a brain Instance back from the model for a given generation"""
    brain_instances: list[BrainInstance] = []

    # Need to define which Model to get from

    selected_model: models.Model = AVAILABLE_MODELS.get(model_type)

    db_models: list[models.Model] = selected_model.objects.filter(
        generation_num=generation_num
    )
    for model in db_models:
        rebuilt_brain_instance: BrainInstance = (
            brain_instance_handling.model_to_brain_instance(model)
        )
        rebuilt_brain_instance.get_attributes_from_bytes()
        brain_instances.append(rebuilt_brain_instance)

    ordered_brian_instances: list[BrainInstance] = sorted(
        brain_instances, key=lambda x: x.fitness, reverse=True
    )

    return ordered_brian_instances


def clear_fit_brain_models() -> None:
    """Clear the FitBrainInstance Models from the DB"""
    FitBrainInstanceModel.objects.all().delete()
