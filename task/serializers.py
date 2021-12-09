from rest_framework import serializers
from .models import Task, AddTask


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'


class AddTaskSerializer(serializers.ModelSerializer):
    tasks = serializers.StringRelatedField(many=True)

    class Meta:
        model = AddTask
        read_only_fields = ['user']
        fields = '__all__'

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep["tasks"] = TaskSerializer(instance.tasks.all(), many=True).data
        return rep
