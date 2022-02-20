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

    def create_or_update_module(self, modules):
        modules_ids = []
        for module in modules:
            module_instance, create = Module.objects.update_or_create(pk=module.get('id'), defaults=module)
            modules_ids.append(module_instance.pk)
        return modules_ids

    def create(self, validated_data):
        module = validated_data.pop('modules', [])
        student = Student.objects.create(**validated_data)
        student.modules.set(self.get_or_create_module(module))
        return student

    def update(self, instance, validated_data):
        modules = validated_data.pop('modules', [])
        instance.modules.set(self.create_or_update_module(modules))
        fields = ['student_id', 'name', 'age', 'grade']
        for field in fields:
            try:
                setattr(instance, field, validated_data[field])
            except KeyError:  # validated_data may not contain all fields during HTTP PATCH
                pass
        instance.save()
        return instance

    class Meta:
        model = Student
        fields = [
            'id', 'name', 'age', 'grade', 'modules'
        ]
