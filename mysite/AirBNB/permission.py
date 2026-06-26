from rest_framework import permissions


class IsOwnerOrAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        if not request.user.is_authenticated:
            return False
        return(
                (obj.user == request.user and request.user.role=='Хост') or request.user.role=='Администратор'
        )

class ReviewPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return (
            obj.user == request.user or
            request.user.role == 'Администратор'
        )

class MessagePermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return (
            obj.sender == request.user or
            obj.receiver == request.user or
            request.user.role == 'Администратор'
        )

class AvailabilityPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return (
            obj.property.user == request.user or
            request.user.role == 'Администратор'
        )