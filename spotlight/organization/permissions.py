from rest_framework import permissions


class OrganizationUserOwner(permissions.BasePermission):
    """Проверка на владение обьектом"""

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return request.user.is_staff or request.user.is_authenticated and obj.organization_admin == request.user
