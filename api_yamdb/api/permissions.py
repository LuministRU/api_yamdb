from rest_framework import permissions


class AdminModOwnerOrReadOnly(permissions.BasePermission):      #для отзывов, комментариев, оценок
    def has_permission(self, request, view):
        return (
            request.method in permissions.SAFE_METHODS
            or request.user.is_authenticated
        )

    def has_object_permission(self, request, view, obj):
        if request.user.is_authenticated:
            return (
                request.method in permissions.SAFE_METHODS
                or obj.author==request.user
                or request.user.role=='admin'
                or request.user.role=='moderator'
            )
        return request.method in permissions.SAFE_METHODS


class AdminOrReadOnly(permissions.BasePermission):      #для списка произведений, категорий и жанров
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return (
                request.method in permissions.SAFE_METHODS
                or request.user.is_staff
                or request.user.role=='admin'
            )
        return request.method in permissions.SAFE_METHODS


class AdminOnly(permissions.BasePermission):        #для списка юзеров
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return (
                request.user.is_staff
                or request.user.role=='admin'
            )
        return False
    def has_object_permission(self, request, view, obj):
        if request.user.is_authenticated:
            return (
                request.user.is_staff
                or request.user.role=='admin'
            )
        return False


class OwnerOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.author == request.user
