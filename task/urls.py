from django.urls import path
from .views import TaskAPIView

urlpatterns = [
    path('tasks/', TaskAPIView.as_view(), name='task')
]
