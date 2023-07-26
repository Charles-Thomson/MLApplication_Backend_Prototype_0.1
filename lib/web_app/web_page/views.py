"""Django Views"""

from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods

from ANN.Brain.brain_instance import BrainInstance

import numpy as np

from web_page.models import AllBrainInstanceModel, FitBrainInstanceModel

from web_page import brain_instance_handling


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


@require_http_methods(["POST"])
def add_fit(request):
    """Add a new Brain Instance"""

    test_brain = BrainInstance(
        brain_type="fit",
        brain_id=1,
        generation_num=2,
        hidden_weights=np.array(
            [
                [1.2, 2.0, 3.0],
                [4.0, 5.0, 6.0],
                [7.0, 8.9, 9.0],
                [1.2, 2.0, 3.0],
                [4.0, 5.0, 6.0],
                [7.0, 8.9, 9.0],
                [1.2, 2.0, 3.0],
                [4.0, 5.0, 6.0],
                [7.0, 8.9, 12.0],
            ]
        ),
        output_weights=np.array(
            [[1.0, 2.0, 3.0], [4.0, 5.3, 6.0], [7.0, 8.0, 9.0]], dtype=np.float64
        ),
        fitness=20.1,
        traversed_path=[2, 4, 5, 6, 7],
        fitness_by_step=[2.3, 4.5, 6.7, 8.9],
    )

    new_brain_instance = brain_instance_handling.brain_instance_to_model(
        brain_instance=test_brain, model_type="fit"
    )
    new_brain_instance.save()
    get_instances()
    return redirect("index")


def get_instances() -> None:
    """Get a brain Instance back from the model"""

    brain_model_1: FitBrainInstanceModel = FitBrainInstanceModel.objects.get(id=2)
    print(brain_model_1)

    brain_instance_1: BrainInstance = brain_instance_handling.model_to_brain_instance(
        brain_model_1
    )

    brain_instance_1.get_attributes_from_bytes()

    print(brain_instance_1.hidden_weights)
    print(brain_instance_1.brain_type)


@require_http_methods(["POST"])
def add_all(request):
    """Add a new Brain Instance"""
    title = request.POST["title_a"]
    brain_type = "general"
    brain_id = request.POST["brain_instance_id_a"]
    generation_num = request.POST["generation_number_a"]
    hidden_weights = "[5,6,7,8]"
    output_weights = "[5,6,7,8]"
    fitness = "0.5"
    traversed_path = "[2,4,6,8,10]"
    fitness_by_step = "[1.0, 4.0, 6.0 , 10.4, 12.7]"

    new_brain_instance = AllBrainInstanceModel(
        title=title,
        brain_type=brain_type,
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


def delete(request, brain_id):
    """Delete a Brain Instance"""
    this_brain_instance = FitBrainInstanceModel.objects.get(id=brain_id)
    this_brain_instance.delete()
    return redirect("index")
