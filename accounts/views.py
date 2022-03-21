from rest_framework import views, status, permissions
from rest_framework.response import Response

from .models import User, Profile
from .serializers import UserRegistrationSerializer, UserSerializer, ProfileSerializer
from utils.response import prepare_create_success_response, prepare_success_response, prepare_error_response


class UserRegistrationAPIView(views.APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        try:
            serializer = UserRegistrationSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(prepare_create_success_response(serializer.data), status=status.HTTP_201_CREATED)
            return Response(prepare_error_response(serializer.errors), status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(prepare_error_response(str(e)))


class ProfileAPIView(views.APIView):

    def get(self, request):
        try:
            queryset = Profile.objects.get(id=self.request.user.id)
            serializer = ProfileSerializer(queryset)
            return Response(prepare_success_response(serializer.data), status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            queryset = User.objects.get(id=self.request.user.id)
            serializer = UserSerializer(queryset)
            return Response(prepare_success_response(serializer.data), status=status.HTTP_200_OK)
