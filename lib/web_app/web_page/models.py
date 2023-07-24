"""The Model for the DB"""
from django.db import models


# Create your models here.
class AllBrainInstanceModel(models.Model):
    """Model for the Brain Instances"""

    title = models.CharField(max_length=350)
    brain_id = models.CharField(max_length=350)
    generation_num = models.CharField(max_length=350)
    hidden_weights = models.CharField(max_length=350)
    output_weights = models.CharField(max_length=350)
    fitness = models.CharField(max_length=350)
    traversed_path = models.CharField(max_length=350)
    fitness_by_step = models.CharField(max_length=350)

    def __str__(self):
        return str(self.title)


class FitBrainInstanceModel(models.Model):
    """Model for the Brain Instances"""

    title = models.CharField(max_length=350)
    brain_id = models.CharField(max_length=350)
    generation_num = models.CharField(max_length=350)
    hidden_weights = models.CharField(max_length=350)
    output_weights = models.CharField(max_length=350)
    fitness = models.CharField(max_length=350)
    traversed_path = models.CharField(max_length=350)
    fitness_by_step = models.CharField(max_length=350)

    def __str__(self):
        return str(self.title)
