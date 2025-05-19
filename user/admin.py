from django.contrib import admin

from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """
    Представляет административное представление для пользователя.
    """

    list_display = ("email", "first_name", "last_name", "phone", "role", "image")
    list_filter = ("email",)
    search_fields = ("email", "first_name", "last_name", "phone")
