from rest_framework import permissions


class IsSuperuserOrIsAdminUser(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_superuser


class IsSuperuserOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        # Allow GET (list) requests to all users
        if request.method in permissions.SAFE_METHODS:
            return True

        # Check if the user is a superuser for other methods (POST, PUT, DELETE)
        return request.user and request.user.is_superuser