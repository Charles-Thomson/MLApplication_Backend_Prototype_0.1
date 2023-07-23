from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    # Method call name from views - name used on the HTML side
    path("add", views.add, name="add"),
    path("delete/<int:todo_id>", views.delete, name="delete"),
    path("update/<int:todo_id>", views.update, name="update"),
]
