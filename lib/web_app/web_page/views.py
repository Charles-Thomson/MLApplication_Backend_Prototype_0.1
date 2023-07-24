"""Django Views"""

from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods

from ANN.Brain.brain_instance import BrainInstance

import numpy as np

from web_page.models import FitBrainInstanceModel, AllBrainInstanceModel


# Create your views here.
def index(request):
    """Get and render all saved brain instances"""

    all_fit_brain_instances = FitBrainInstanceModel.objects.all()
    all_brain_instances = AllBrainInstanceModel.objects.all()
    return render(
        request,
        "base.html",
        {
            "All_BrainInstance_list": all_brain_instances,
            "Fit_BrainInstance_list": all_fit_brain_instances,
        },
    )


def format_fit_brain_for_db(brain_instance: object) -> FitBrainInstanceModel:
    """Save the brain instance as a fit instance"""
    # brain_instance.set_attributes_to_bytes()

    new_db_brain_instance = FitBrainInstanceModel(
        brain_id=brain_instance.brain_id,
        generation_num=brain_instance.generation_num,
        hidden_weights=brain_instance.hidden_weights,
        output_weights=brain_instance.output_weights,
        fitness=brain_instance.fitness,
        traversed_path=brain_instance.traversed_path,
        fitness_by_step=brain_instance.fitness_by_step,
    )

    return new_db_brain_instance


@require_http_methods(["POST"])
def add_fit(request):
    """Add a new Brain Instance"""

    test_brain = BrainInstance(
        brain_id=1,
        generation_num=2,
        hidden_weights=np.array([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0], [7.0, 8.0, 9.0]]),
        output_weights=np.array([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0], [7.0, 8.0, 9.0]]),
    )
    new_brain_instance = format_fit_brain_for_db(test_brain)
    new_brain_instance.save()
    return redirect("index")


@require_http_methods(["POST"])
def add_all(request):
    """Add a new Brain Instance"""
    title = request.POST["title_a"]
    brain_id = request.POST["brain_instance_id_a"]
    generation_num = request.POST["generation_number_a"]
    hidden_weights = request.POST["hidden_weights_a"]
    output_weights = "[5,6,7,8]"
    fitness = "0.5"
    traversed_path = "[2,4,6,8,10]"
    fitness_by_step = "[1.0, 4.0, 6.0 , 10.4, 12.7]"

    new_brain_instance = AllBrainInstanceModel(
        title=title,
        brain_id=brain_id,
        generation_num=generation_num,
        hidden_weights=hidden_weights,
        output_weights=output_weights,
        fitness=fitness,
        traversed_path=traversed_path,
        fitness_by_step=fitness_by_step,
    )

    new_brain_instance.save()
    return redirect("index")


def update(request, brain_instance_id):
    """Update a Brain Instance"""
    this_brain_instance = AllBrainInstanceModel.objects.get(id=brain_instance_id)
    this_brain_instance.complete = not this_brain_instance.complete
    this_brain_instance.save()
    return redirect("index")


def delete(request, brain_instance_id):
    """Delete a Brain Instance"""
    this_brain_instance = AllBrainInstanceModel.objects.get(id=brain_instance_id)
    this_brain_instance.delete()
    return redirect("index")
