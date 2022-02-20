from rest_framework import serializers

from core.models.student import Module, Student


class ModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Module
        fields = [
            'id', 'module_name', 'class_room', 'module_desc'
        ]


class StudentSerializer(serializers.ModelSerializer):
    modules = ModuleSerializer(many=True)

    def get_or_create_module(self, modules):
        modules_ids = []
        for module in modules:
            module_instance, create = Module.objects.get_or_create(pk=module.get('id'), defaults=module)
            modules_ids.append(module_instance.pk)
        return modules_ids

    def create(self, validated_data):
        module = validated_data.pop('modules', [])
        student = Student.objects.create(**validated_data)
        student.modules.set(self.get_or_create_module(module))
        return student

    class Meta:
        model = Student
        # depth = 1
        fields = [
            'id', 'name', 'age', 'grade', 'modules'
        ]
