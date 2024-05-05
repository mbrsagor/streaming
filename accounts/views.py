from rest_framework import views, generics, status, permissions
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from django.core.mail import send_mail

from .models import User, Profile
from .serializers import UserRegistrationSerializer, UserSerializer, ProfileSerializer, ResetPasswordSerializer, \
    PasswordChangeSerializer
from utils.response import prepare_create_success_response, prepare_success_response, prepare_error_response


class SendMessage(views.APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request):
        try:
            message = send_mail('Subject here', 'Here is the message.', 'x@gmail.com',
                                ['xyz.cse@gmail.com'],
                                fail_silently=False)
            return Response(message, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(str(e))


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


class PasswordResetView(views.APIView):
    permission_classes = (permissions.AllowAny,)
    queryset = User.objects.all()

    def get_object(self):
        email = self.request.data.get('email')
        obj = get_object_or_404(self.queryset, email=email)
        return obj

    def post(self, request, *args, **kwargs):
        try:
            user = self.get_object()
            user.send_reset_password_email()
            return Response({}, status=status.HTTP_200_OK)
        except Exception as ex:
            return Response(prepare_error_response(str(ex)))


class PasswordResetConfirmView(views.APIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = ResetPasswordSerializer

    def post(self, request, *args, **kwargs):
        try:
            serializer = ResetPasswordSerializer(data=request.data)
            if not serializer.is_valid():
                return Response(prepare_error_response(serializer.errors), status=status.HTTP_400_BAD_REQUEST)
            return Response(prepare_success_response('Password updated successfully.'), status=status.HTTP_200_OK)
        except Exception as ex:
            return Response(prepare_error_response(str(ex)))


class ChangePasswordView(generics.UpdateAPIView):
    # permission_classes = (permissions.AllowAny,)
    queryset = User.objects.all()
    serializer_class = PasswordChangeSerializer


class LogoutAPIView(views.APIView):
    def post(self, request):
        response = Response()
        response.delete_cookie('jwt')
        response.data = prepare_success_response('User logout successfully')
        return response


"""
class CreateUserAPIView(views.APIView):
    """
    name: Create a new user API
    Desc: Store owner can create new user for manage their own account.
    Method: POST
    URL: /api/auth/create-user/
    :param
    """

    def post(self, request):
        try:
            serializer = auth_serializer.CreateUserSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                # Add menu for the user
                menus = request.data['menus']
                user_id = serializer.data['id']
                add_user_menu = MenuAddToUser.objects.create(user_id=user_id)
                add_user_menu.menus.add(*menus)
                return Response(response.prepare_success_response(messages.CREATE_USER), status=status.HTTP_201_CREATED)
            return Response(response.prepare_error_response(serializer.errors), status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(response.prepare_error_response(str(e)), status=status.HTTP_400_BAD_REQUEST)

"""
