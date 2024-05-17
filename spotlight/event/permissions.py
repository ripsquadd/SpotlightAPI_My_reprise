from rest_framework import permissions


class IsUserEventOwner(permissions.BasePermission):
    """Проверка на владение обьектом"""

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return request.user.is_staff or request.user.is_authenticated and obj.event_admin == request.user


class IsUserHavePermissionCreateEvent(permissions.BasePermission):
    """Проверка на статус организации"""

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        if request.user.is_authenticated:
            return True
