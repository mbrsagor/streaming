from rest_framework import serializers

from core.models.student import Module, Student


class ModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Module
        fields = [
            'id', 'module_name', 'class_room', 'module_desc'
        ]


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        depth = 1
        fields = [
            'id', 'name', 'age', 'grade', 'modules'
        ]
