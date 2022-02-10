from rest_framework import viewsets

from core.models.person import Person, Group
from core.serializers.person_serializer import PersonSerializer, GroupSerializer


class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
