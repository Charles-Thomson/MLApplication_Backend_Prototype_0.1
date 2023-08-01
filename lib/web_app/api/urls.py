from django.urls import path
from . import views

urlpatterns = [
    path("", views.get_routes),
    path("get_data/", views.get_data),
    path("get_fittest_brain/", views.get_fittest_brain),
    path("get_fittest_from_each_generation/", views.get_fittest_from_each_generation),
    path("run_main_system/<str:data>/", views.run_main_system),
]
