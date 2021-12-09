from django.urls import path
from .views import TaskAPIView, TaskUpdateDeleteAPIView

urlpatterns = [
    path('tasks/', TaskAPIView.as_view(), name='task'),
    path('tasks/<int:pk>/', TaskUpdateDeleteAPIView.as_view(), name='task_update_delete'),
]
