from django.urls import path
from . import views

urlpatterns = [
    path("", views.get_routes),
    path("get_data/", views.get_data),
    path("get_fittest_brain/", views.get_fittest_brain),
    path("get_fittest_from_each_generation/", views.get_fittest_from_each_generation),
    path("get_brain_by_id/<str:id>/", views.get_brain_by_id),
    path("test_show_json/<str:data>/", views.test_show_json),
    path("test_set_config/<str:data>/", views.test_set_config),
    path("run_main_system/<str:data>/", views.run_main_system),
    path("test_api_call/", views.test_api_call),
]
