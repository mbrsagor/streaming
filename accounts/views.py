from rest_framework import views, status, permissions
from rest_framework.response import Response

from .models import User
from .serializers import UserRegistrationSerializer
from utils.response import prepare_create_success_response, prepare_success_response, prepare_error_response


class UserRegistrationAPIView(views.APIView):
    permission_classes = (permissions.AllowAny,)
    parser_classes = UserRegistrationSerializer

    def post(self, request):
        try:
            serializer = UserRegistrationSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(prepare_create_success_response(serializer.data), status=status.HTTP_201_CREATED)
            return Response(prepare_error_response(serializer.errors), status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(prepare_error_response(str(e)))

