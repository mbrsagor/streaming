from rest_framework import viewsets, status
from rest_framework.response import Response

from core.models.student import Module, Student
from core.serializers.student_serializer import ModuleSerializer, StudentSerializer


class ModuleViewSet(viewsets.ModelViewSet):
    queryset = Module.objects.all()
    serializer_class = ModuleSerializer


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def create(self, request, *args, **kwargs):
        data = request.data
        new_student = Student.objects.create(
            name=data['name'], age=data['age'], grade=data['grade']
        )
        new_student.save()

        for module in data['modules']:
            module_obj = Module.objects.get(module_name=module['module_name'])
            new_student.modules.add(module_obj)

        serializer = StudentSerializer(new_student)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
