from rest_framework import permissions


class IsUserPlaceOwner(permissions.BasePermission):
    """Проверка на владение обьектом"""

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return request.user.is_staff or request.user.is_authenticated and obj.place_admin == request.user


class IsUserHavePermissionCreatePlace(permissions.BasePermission):
    """Проверка на статус организации"""

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        if request.user.is_authenticated:
            return True
