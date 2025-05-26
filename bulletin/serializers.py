# bulletin/serializers.py
from rest_framework import serializers

from .models import Bulletin, Review


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ["id", "text", "author", "created_at"]
        read_only_fields = ["id", "author", "created_at"]

    def create(self, validated_data):
        # автоматически назначаем автора на текущего пользователя
        validated_data["author"] = self.context["request"].user
        return super().create(validated_data)


class BulletinSerializer(serializers.ModelSerializer):
    """
    Преобразует объект модели Bulletin в JSON, чтобы можно было отдавать данные клиенту (в API-ответе).
    """

    reviews = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = Bulletin
        fields = ["id", "title", "price", "description", "author", "created_at", "reviews"]
        read_only_fields = ["id", "author", "created_at"]

    def create(self, validated_data):
        # автоматически назначаем автора на текущего пользователя
        validated_data["author"] = self.context["request"].user
        return super().create(validated_data)
