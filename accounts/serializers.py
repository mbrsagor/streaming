from rest_framework import serializers
from django.contrib.auth import password_validation
from django.contrib.auth.password_validation import validate_password

from .models import User, Profile


class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(style={'input_type': 'password', 'placeholder': 'Password'})

    class Meta:
        model = User
        fields = (
            'id', 'name', 'email', 'phone_number', 'role', 'password',
            'created_at', 'updated_at'
        )

    def create(self, validated_data):
        user = User.objects.create_user(
            name=validated_data['name'],
            email=validated_data['email'],
            phone_number=validated_data['phone_number'],
            role=validated_data['role'],
            password=validated_data['password'],
        )
        return user

    def validated_password(self, value):
        password_validation.validate_password(value, self.instance)
        return value


# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id', 'name', 'email', 'phone_number', 'role', 'last_login', 'date_joined',
            'is_staff', 'is_active', 'is_superuser'
        )


# Profile Serializer
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        read_only_fields = ('auth',)
        fields = (
            'id', 'auth', 'date_of_birth', 'address', 'current_age',
            'created_at', 'updated_at'
        )

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['auth'] = UserSerializer(instance.auth).data
        return response


class PasswordChangeSerializer(serializers.ModelSerializer):
    """
    User will change password.
    params: given `Old password`, then match `new password` and `confirm password`
    """

    old_password = serializers.CharField(write_only=True, required=True,
                                         style={'input_type': 'password', 'placeholder': 'Old Password'})
    new_password = serializers.CharField(write_only=True, required=True, validators=[validate_password],
                                         style={'input_type': 'password', 'placeholder': 'New Password'})
    confirm_password = serializers.CharField(write_only=True, required=True,
                                             style={'input_type': 'password', 'placeholder': 'Confirm Password'})

    class Meta:
        model = User
        fields = [
            'pk', 'old_password', 'new_password', 'confirm_password'
        ]

    def validate(self, attrs):
        if attrs['new_password'] != attrs['confirm_password']:
            raise serializers.ValidationError({'password': 'Sorry! password not match'})
        return attrs

    def validate_old_password(self, value):
        user = self.context['request'].user
        if not user.check_password(value):
            raise serializers.ValidationError({"old_password": "Old password is not correct"})
        return value

    def update(self, instance, validated_data):
        instance.set_password(validated_data['new_password'])
        instance.save()
        return instance


class ResetPasswordSerializer(serializers.ModelSerializer):
    """
    Reset or Forgot password.
    When user will forgot password after that the serializer will call.
    """
    id = serializers.CharField()
    token = serializers.CharField()

    class Meta:
        model = User
        fields = ('id', 'token', 'password',)
        extra_kwargs = {'password': {'write_only': True}}
