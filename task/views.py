from rest_framework import views, status, permissions
from rest_framework.response import Response

from .models import Task
from .serializers import TaskSerializer
from util.custom_response import prepare_success_response, prepare_create_success_response, prepare_error_response
from util.validaiton_task import task_validation


class TaskAPIView(views.APIView):
    permission_classes = [permissions.AllowAny, ]

    def get(self, request):
        task = Task.objects.all()
        serializer = TaskSerializer(task, many=Task)
        return Response(prepare_success_response(serializer.data), status=status.HTTP_200_OK)

    def post(self, request):
        validate_error = task_validation(request.data)
        if validate_error is not None:
            return Response(prepare_error_response(validate_error), status=status.HTTP_400_BAD_REQUEST)
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(prepare_create_success_response(serializer.data), status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
