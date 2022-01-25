from django.db import transaction
from rest_framework import generics
from rest_framework.response import Response

from core.models.role import Role, Permission, AccessControl
from core.role_permissions import IsAdminOrNoAccess
from core.serializers.role_seralizer import RoleSerializer, PermissionSerializer, AccessControlSerializer


class RoleView(generics.ListCreateAPIView):
    permission_classes = (IsAdminOrNoAccess,)
    serializer_class = RoleSerializer
    queryset = Role.objects.all()


class PermissionView(generics.ListCreateAPIView):
    permission_classes = (IsAdminOrNoAccess,)
    serializer_class = PermissionSerializer
    queryset = Permission.objects.all()
    models = (Permission,)


class AccessControlView(generics.ListCreateAPIView):
    permission_classes = (IsAdminOrNoAccess,)
    serializer_class = AccessControlSerializer
    queryset = AccessControl.objects.all()

    def post(self, request, *args, **kwargs):
        with transaction.atomic():
            permissions = request.data.get('permissions')
            permission_instance_list = [p for p in Permission.objects.filter(pk__in=permissions)]
            serializer = AccessControlSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                instance = AccessControl.objects.filter(
                    role_id=request.data.get('role'), url_name=request.data.get('url_name')
                ).first()
                if instance is None:
                    instance = serializer.save()
                if instance:
                    # First Clear all permissions
                    instance.permissions.clear()
                    # Add Permission
                    instance.permissions.add(*permission_instance_list)
                    return Response(serializer.data)
            return Response(serializer.data)
