from rest_framework import serializers
from django.contrib.auth import password_validation

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
        fields = '__all__'

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['auth'] = UserSerializer(instance.auth).data
        return response
