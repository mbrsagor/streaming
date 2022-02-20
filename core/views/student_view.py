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
