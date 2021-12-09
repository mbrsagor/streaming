from django.urls import path
from task.views.task_view import TaskAPIView, TaskUpdateDeleteAPIView
from task.views.add_task_view import CreateAddTaskView

urlpatterns = [
    path('tasks/', TaskAPIView.as_view(), name='task'),
    path('tasks/<int:pk>/', TaskUpdateDeleteAPIView.as_view(), name='task_update_delete'),
    path('add-task/', CreateAddTaskView.as_view(), name='add_task'),
]
