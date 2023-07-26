from rest_framework.response import Response
from rest_framework.decorators import api_view
from web_page.models import FitBrainInstanceModel
from api.serializers import BrainSerializer


@api_view(["GET"])
def getData(request):
    BraiInstanceModels = FitBrainInstanceModel.objects.all()
    serializer = BrainSerializer(BraiInstanceModels, many=True)
    return Response(serializer.data)
