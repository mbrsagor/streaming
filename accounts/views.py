from rest_framework import views, generics, status, permissions
from rest_framework.response import Response

from .models import User, Profile
from .serializers import UserRegistrationSerializer, UserSerializer, ProfileSerializer, PasswordChangeSerializer
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
            profile = Profile.objects.get(id=self.request.user.id)
            serializer = ProfileSerializer(profile)
            return Response(prepare_success_response(serializer.data), status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            user = User.objects.get(id=self.request.user.id)
            serializer = UserSerializer(user)
            return Response(prepare_success_response(serializer.data), status=status.HTTP_200_OK)


class ProfileUpdateDeleteView(views.APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, pk):
        try:
            return Profile.objects.get(id=pk)
        except Profile.DoesNotExist:
            return None

    def put(self, request, pk):
        try:
            profile = self.get_object(pk)
            if profile is not None:
                serializer = ProfileSerializer(profile, data=request.data)
                if serializer.is_valid():
                    serializer.save(user=request.user)
                    return Response(prepare_create_success_response(serializer.data), status=status.HTTP_201_CREATED)
                return Response(prepare_error_response(serializer.errors), status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response(prepare_error_response("No user found for this ID"), status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(prepare_error_response(str(e)))

    def delete(self, request, pk):
        profile = self.get_object(pk)
        if profile is not None:
            profile.delete()
            return Response(prepare_success_response('Profile has been deleted'), status=status.HTTP_200_OK)
        return Response(prepare_error_response('No profile found for this ID '), status=status.HTTP_400_BAD_REQUEST)


class ChangePasswordView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = PasswordChangeSerializer


class LogoutAPIView(views.APIView):
    def post(self, request):
        response = Response()
        response.delete_cookie('jwt')
        response.data = prepare_success_response('User logout successfully')
        return response
