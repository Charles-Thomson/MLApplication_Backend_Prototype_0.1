"""Django Views"""

from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods

from web_page.models import BrainInstanceModel


# Create your views here.
def index(request):
    """Get and render all saved brain instances"""
    all_brain_instances = BrainInstanceModel.objects.all()
    return render(request, "base.html", {"BrainInstance_list": all_brain_instances})


@require_http_methods(["POST"])
def add(request):
    """Add a new Brain Instance"""
    title = request.POST["title"]
    brain_id = request.POST["brain_instance_id"]
    generation_num = request.POST["generation_number"]
    hidden_weights = request.POST["hidden_weights"]
    output_weights = "[5,6,7,8]"
    fitness = "0.5"
    traversed_path = "[2,4,6,8,10]"
    fitness_by_step = "[1.0, 4.0, 6.0 , 10.4, 12.7]"

    new_brain_instance = BrainInstanceModel(
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
    this_brain_instance = BrainInstanceModel.objects.get(id=brain_instance_id)
    this_brain_instance.complete = not this_brain_instance.complete
    this_brain_instance.save()
    return redirect("index")


def delete(request, brain_instance_id):
    """Delete a Brain Instance"""
    this_brain_instance = BrainInstanceModel.objects.get(id=brain_instance_id)
    this_brain_instance.delete()
    return redirect("index")
