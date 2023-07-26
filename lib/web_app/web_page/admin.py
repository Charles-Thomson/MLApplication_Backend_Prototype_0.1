from django.contrib import admin
from .models import (
    AllBrainInstanceModel,
    FitBrainInstanceModel,
    TrainedBrainInstanceModel,
)


# Register your models here.
admin.site.register(AllBrainInstanceModel)
admin.site.register(FitBrainInstanceModel)
admin.site.register(TrainedBrainInstanceModel)
