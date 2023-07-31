"""The Model for the DB"""
from django.db import models


# Create your models here.
class AllBrainInstanceModel(models.Model):
    """Model for the Brain Instances"""

    brain_type = models.CharField(max_length=100, default="general")
    brain_id = models.CharField(max_length=350)
    generation_num = models.CharField(max_length=350)
    hidden_weights = models.BinaryField()
    output_weights = models.CharField(max_length=350)
    fitness = models.CharField(max_length=350)

    traversed_path = models.CharField(max_length=350)
    fitness_by_step = models.CharField(max_length=350)


class FitBrainInstanceModel(models.Model):
    """Model for the Brain Instances"""

    brain_type = models.CharField(max_length=100, default="fit")
    brain_id = models.CharField(max_length=350)
    generation_num = models.CharField(max_length=350)
    fitness = models.CharField(max_length=350)
    hidden_weights = models.BinaryField()
    output_weights = models.BinaryField()
    traversed_path = models.CharField(max_length=350)
    fitness_by_step = models.CharField(max_length=350)


class TrainedBrainInstanceModel(models.Model):
    """Model for the Brain Instances"""

    brain_type = models.CharField(max_length=100, default="trained")
    brain_id = models.CharField(max_length=350)
    generation_num = models.CharField(max_length=350)
    fitness = models.CharField(max_length=350)
    hidden_weights = models.BinaryField()
    output_weights = models.BinaryField()

    traversed_path = models.CharField(max_length=350)
    fitness_by_step = models.CharField(max_length=350)


AVAILABLE_MODELS: dict[str, models.Model] = {
    "general": AllBrainInstanceModel,
    "fit": FitBrainInstanceModel,
    "trained": TrainedBrainInstanceModel,
}
