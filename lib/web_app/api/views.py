import json
from rest_framework.response import Response
from rest_framework.decorators import api_view
from web_page.models import FitBrainInstanceModel
from api.serializers import BrainSerializer
from django.http import JsonResponse
from rest_framework import status

from ANN.main import main_system
from ANN.config import set_config


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
def get_brain_by_id(request, id):
    """Get a brain by it's id"""
    brain_model = FitBrainInstanceModel.objects.get(id=id)
    ser_brain_model = BrainSerializer(brain_model, many=False)
    return Response(ser_brain_model.data)


@api_view(["GET"])
def get_routes(request):
    """Guide on available routes"""
    routes: list[dict] = [
        {"name": "get_data/", "method": "holder", "description": "Holder desription"},
        {
            "name": "get_fittest_brain/",
            "method": "holder",
            "description": "Holder desription",
        },
    ]
    return Response(routes)


# Main API call from fron end
@api_view(["GET"])
def run_main_system(request, data):
    """Main API call from front end"""
    print("SYSTEM: DATA RECIVED")
    set_new_config(data)
    number_of_generations: int = main_system()
    return_payload = generate_return_payload(number_of_generations)
    return Response(return_payload, status=status.HTTP_200_OK)


def set_new_config(data) -> None:
    """Testing showing passed Json Data"""
    recived_data = json.loads(data)

    set_config.this_set_config(recived_data["payloadBody"])
    print("CONFIG DATA SET")


def generate_return_payload(number_of_generations):
    """Get the fittest brain from each generation"""

    # Working from here
    # Need to get the highest and lowest from each gen
    # along with the paths anf fitness by path for each
    # use an update to "tag" which is which and read on the reciving end ?
    # => Will need another field in the brain instance model

    return_models: FitBrainInstanceModel = []
    brain_instance_models: list[
        FitBrainInstanceModel
    ] = FitBrainInstanceModel.objects.all()

    for gen in range(0, number_of_generations + 1):
        this_gen_models = brain_instance_models.filter(generation_num=gen)
        fitest_model = this_gen_models.order_by("-fitness").first()
        if fitest_model is not None:
            return_models.append(fitest_model)

    ser_data = BrainSerializer(return_models, many=True)
    return ser_data.data


# Test Getting the return Data
@api_view(["GET"])
def test_api_call(request):
    """Test api call from front end"""
    print("SYSTM API TEST CALL RECIVED")


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


# TEST SETTING DATA VIA API


@api_view(["GET"])
def test_show_json(request, data):
    """Testing showing passed Json Data"""
    print(data)
    return JsonResponse(data, safe=False)


@api_view(["GET"])
def test_set_config(request, data) -> None:
    """Testing showing passed Json Data"""
    print(data)
    recived_data = json.loads(data)

    set_config.this_set_config(recived_data["payloadBody"])
    print("CONFIG DATA SET")
    return Response(data)
