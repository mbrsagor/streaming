from rest_framework import permissions
from datetime import datetime, timedelta, timezone

class PermissionHelperMixin(object):
    def admin_editable_only(self):
        if self.action not in ['list', 'retrieve']:
            return [permissions.IsAdminUser()]
        else:
            return []

    def authenticated_user_editable_only(self):
        if self.action not in ['list', 'retrieve']:
            return [permissions.IsAuthenticated()]
        else:
            return []

class AuthorAllStaffAllButEditOrReadOnly(permissions.BasePermission):
    edit_methods = ("PUT", "PATCH")

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True

    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser:
            return True
        if request.method in permissions.SAFE_METHODS:
            return True
        if obj.author == request.user:
            return True
        if request.user.is_staff and request.method not in self.edit_methods:
            return True
        return False


class ExpiredObjectSuperuserOnly(permissions.BasePermission):

    def object_expired(self, obj):
        expired_on = timezone.make_aware(datetime.now() - timedelta(minutes=10))
        return obj.created < expired_on

    def has_object_permission(self, request, view, obj):
        if self.object_expired(obj) and not request.user.is_superuser:
            return False
        else:
            return True


class IsStaff(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.user.is_staff:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        if request.user.is_staff:
            return True
        return False


class IsOwner(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        if obj.author == request.user:
            return True
        return False