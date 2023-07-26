from rest_framework import serializers
from web_page.models import FitBrainInstanceModel


class BrainSerializer(serializers.ModelSerializer):
    """Serialize each model instance for the API"""

    class Meta:
        model = FitBrainInstanceModel
        fields = "__all__"
