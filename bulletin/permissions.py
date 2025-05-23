from rest_framework import permissions


class IsAuthorOrAdminOrReadOnlyForBulletin(permissions.BasePermission):
    """
    Разрешает безопасные методы всем, изменение/удаление — только автору или администратору.
    """

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user or request.user.groups.filter(name="Администраторы").exists()


class IsAuthorOrAdminOrReadOnlyForReview(permissions.BasePermission):
    """
    Анонимы могут только смотреть отзывы, авторы могут редактировать свои, администраторы — любые.
    """

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user or request.user.groups.filter(name="Администраторы").exists()

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_authenticated
