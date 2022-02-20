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

    # Json Body
    """
    {
        "name": "Best practices through leveraged.",
        "age": 28,
        "grade": 444,
        "modules": [
            {
                "module_name": "update new modues",
                "class_room": "new seven",
                "module_desc": "Conveniently reconceptualize go forward collaboration and idea-sharing through extensive information. Progressively actualize enterprise alignments rather than synergistic technology. Synergistically deliver multifunctional best practices through leveraged best practices."
            },
            {
                "module_name": "new last module",
                "class_room": "new nine",
                "module_desc": "Authoritatively transition open-source technology without functional markets. Globally administrate."
            }
        ]
    }
    """
