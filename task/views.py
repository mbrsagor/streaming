from rest_framework import views, status, permissions
from rest_framework.response import Response

from .models import Task
from .serializers import TaskSerializer
from util.custom_response import prepare_success_response


class TaskAPIView(views.APIView):
    permission_classes = [permissions.AllowAny, ]

    def get(self, request):
        task = Task.objects.all()
        serializer = TaskSerializer(task, many=Task)
        return Response(prepare_success_response(serializer.data), status=status.HTTP_200_OK)

