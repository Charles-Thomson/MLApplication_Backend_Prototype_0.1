"""Django Views"""

from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods

from ANN.Brain.brain_instance import BrainInstance

import numpy as np

from web_page.models import AllBrainInstanceModel, FitBrainInstanceModel

from web_page import brain_instance_handling

import json


def build_svg_path() -> list:
    """Build the svg path strings based on the Brain instance path"""

    # Hard coding sizes to start
    board_size_x, board_size_y = 200, 200
    states_x, states_y = 10, 10

    step_size = board_size_x / states_x
    state_center_point = step_size / 2

    all_brain_instances = AllBrainInstanceModel.objects.all()

    for instance in all_brain_instances:
        svg_commands: list[str] = []

        path: str = instance.traversed_path
        path_list: list[int] = json.loads(path)

        start_location_state: int = path_list.pop(0)
        svg_coords_x, svg_coords_y = state_to_coords(
            start_location_state, states_x, step_size, state_center_point
        )

        start_loc: str = f"M{svg_coords_x},{svg_coords_y}"

        svg_commands.append(start_loc)

        for element in path_list:
            svg_coords_x, svg_coords_y = state_to_coords(
                element, states_x, step_size, state_center_point
            )
            draw_loc: str = f"L{svg_coords_x},{svg_coords_y}"
            svg_commands.append(draw_loc)

        built_svg_str: str = ",".join(svg_commands)
        # print(svg_commands)
        # print(built_svg_str)

        instance.svg_path = built_svg_str

    return all_brain_instances


def state_to_coords(state: int, states_x: int, step_size, state_center_point) -> str:
    """Convert a given state to coords representation

    Gives the coords of the ceter point of the give state
    """

    base_coords = divmod(state, states_x)
    y_state = base_coords[0]
    x_state = base_coords[1]
    svg_coords_x = (x_state * step_size) + state_center_point
    svg_coords_y = (y_state * step_size) + state_center_point

    return svg_coords_x, svg_coords_y


# Create your views here.
def index(request):
    """Get and render all saved brain instances"""

    all_fit_brain_instances = FitBrainInstanceModel.objects.all()
    all_brain_instances = build_svg_path()
    maze_route = "M10,10,L10,30"
    # This is how to return the page
    return render(
        request,
        "flex_base.html",
        {
            "All_BrainInstance_list": all_brain_instances,
            "Fit_BrainInstance_list": all_fit_brain_instances,
            "maze_route": maze_route,
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
