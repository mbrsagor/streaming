from rest_framework import serializers

from core.models.student import Module, Student


class ModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Module
        fields = '__all__'


class StudentSerializer(serializers.ModelSerializer):
    persons = ModuleSerializer(many=True, read_only=True)

    class Meta:
        model = Student
        fields = [
            'id', 'name', 'age', 'grade', 'modules'
        ]
