from rest_framework.permissions import BasePermission


class IsAdminOrIsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.is_admin or request.user == obj.user