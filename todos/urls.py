from django.urls import path
from . import views

urlpatterns = [
    path("tasks/", views.TaskView.as_view(), name="taskspy"),
    path("task/<int:pk>/", views.TaskDetailView.as_view(), name="task-detail"),
]
