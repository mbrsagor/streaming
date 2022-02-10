from rest_framework import serializers

from core.models.person import Person, Group


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = [
            'id', 'name', 'persons'
        ]
