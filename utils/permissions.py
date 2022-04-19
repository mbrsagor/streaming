from rest_framework.permissions import BasePermission, SAFE_METHODS


class ModelPermission(BasePermission):

    method_mapper = {
        'GET': 'view',
        'POST': 'add',
        'PUT': 'change',
        'PATCH': 'change',
        'DELETE': 'delete'
    }

    def get_model_permission(self, method, model):
        app_label = model._meta.app_label
        model_name = model._meta.model_name
        permission_name = self.method_mapper.get(method)
        return f'{app_label}.{permission_name}_{model_name}'

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        permission = self.get_model_permission(request.method, view.model)
        return request.user.has_perm(permission)

