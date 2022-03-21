from rest_framework import serializers
from django.contrib.auth import password_validation

from .models import User


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(style={'input_type': 'password', 'placeholder': 'Password'})

    class Meta:
        model = User
        fields = (
            'id', 'name', 'email', 'phone_number', 'role', 'password',
            'created_at', 'updated_at'
        )

    def create(self, validated_data):
        user = User.objects.create(
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
