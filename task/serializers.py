from rest_framework import serializers
from .models import Task, AddTask


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'


class AddTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = AddTask
        fields = (
            'id',
            'title',
            'user',
            'task_name',
            'assign_by',
            'is_active',
            'status',
            'start_date'
            'end_date',
            'created_at',
            'created_at'
        )
