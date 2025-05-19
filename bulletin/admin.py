from django.contrib import admin

from .models import Bulletin, Review


@admin.register(Bulletin)
class BulletinAdmin(admin.ModelAdmin):
    """
    Представляет административное представление для объявления.
    """

    list_display = ("title", "price", "author", "created_at")
    list_filter = ("title", "author")
    search_fields = ("title", "author")


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    """
    Представляет административное представление для отзыва.
    """

    list_display = ("text", "author", "ad", "created_at")
    list_filter = ("text", "author", "ad")
    search_fields = ("text", "author", "ad")
