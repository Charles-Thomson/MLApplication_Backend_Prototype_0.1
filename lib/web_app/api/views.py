import json
from rest_framework.response import Response
from rest_framework.decorators import api_view
from web_page.models import FitBrainInstanceModel
from api.serializers import BrainSerializer
from web_page.db_functions import clear_fit_brain_models

from rest_framework import status

from ANN.main import main_system
from ANN.config import set_config


@api_view(["GET"])
def get_routes(request):
    """Guide on available endpoints"""
    routes: list[dict] = [
        {
            "name": "get_data/",
            "method": "GET",
            "description": "Return all Fit Brain Instances stored",
        },
        {
            "name": "get_fittest_brain/",
            "method": "GET",
            "description": "Get the fittest brain instance",
        },
        {
            "name": "get_fittest_from_each_generation/",
            "method": "GET",
            "description": "Get the fittest brain instance from each generation",
        },
        {
            "name": "get_fittest_from_each_generation/<str:data>",
            "method": "GET",
            "description": "Run the main system",
            "requierd": "Needs to be gven the required config data for the main system - named 'data' ",
        },
    ]
    return Response(routes)


@api_view(["GET"])
def get_data(request):
    data = FitBrainInstanceModel.objects.all()
    ser_data = BrainSerializer(data, many=True)
    return Response(ser_data.data, status=status.HTTP_200_OK)


# Getting the single fittest Brain
@api_view(["GET"])
def get_fittest_brain(request):
    """Get the fit brains of each generations"""
    brain_instance_models: list[
        FitBrainInstanceModel
    ] = FitBrainInstanceModel.objects.all()

    fitest_instance = brain_instance_models.order_by("-fitness").first()

    ser_data = BrainSerializer(fitest_instance)
    return Response(ser_data.data, status=status.HTTP_200_OK)


@api_view(["GET"])
def get_fittest_from_each_generation(request):
    """Get the fittest brain from each generation"""
    num_generations_holder: int = (
        2  # This will be returned by the "Main system" Function
    )

    return_models: FitBrainInstanceModel = []
    brain_instance_models: list[
        FitBrainInstanceModel
    ] = FitBrainInstanceModel.objects.all()

    for gen in range(num_generations_holder):
        this_gen_models = brain_instance_models.filter(generation_num=gen)
        fitest_model = this_gen_models.order_by("-fitness").first()
        if fitest_model is not None:
            return_models.append(fitest_model)

    print(return_models)
    ser_data = BrainSerializer(return_models, many=True)
    return Response(ser_data.data)


# Main API call from front end


@api_view(["GET"])
def run_main_system(request, data):
    """Main API call from front end"""

    clear_fit_brain_models()  # Clear the model to stop last run models interfirance
    set_new_config(data)
    number_of_generations: int = main_system()
    return_payload = generate_return_payload(number_of_generations)
    return Response(return_payload, status=status.HTTP_200_OK)


def set_new_config(data) -> None:
    """Testing showing passed Json Data"""
    recived_data = json.loads(data)
    set_config.this_set_config(recived_data["payloadBody"])


def generate_return_payload(number_of_generations):
    """Get the fittest brain from each generation"""

    return_models: FitBrainInstanceModel = []
    brain_instance_models: list[
        FitBrainInstanceModel
    ] = FitBrainInstanceModel.objects.all()

    for gen in range(0, number_of_generations + 1):
        this_gen_models = brain_instance_models.filter(generation_num=gen)
        highest_fit_model = this_gen_models.order_by("-fitness").first()
        lowest_fitest_model = this_gen_models.order_by("-fitness").last()

        if highest_fit_model is not None and lowest_fitest_model is not None:
            return_models.append(highest_fit_model)
            return_models.append(lowest_fitest_model)

    ser_data = BrainSerializer(return_models, many=True)
    return ser_data.data
