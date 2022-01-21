from rest_framework import views, status, permissions
from rest_framework.response import Response

from task.models import AddTask
from task.serializers import AddTaskSerializer
from util.custom_response import prepare_success_response, prepare_create_success_response, prepare_error_response


class CreateAddTaskView(views.APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        serializer = AddTaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(prepare_create_success_response(serializer.data), status=status.HTTP_201_CREATED)
        return Response(prepare_error_response(serializer.errors), status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        task = AddTask.objects.all()
        serializer = AddTaskSerializer(task, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
