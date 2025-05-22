# API endpoints for bulletin and review
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet

from .models import Bulletin, Review
from .paginators import BulletinPagination, ReviewPagination
from .serializers import BulletinSerializer, ReviewSerializer


class BulletinViewSet(ModelViewSet):
    """
    API endpoint, который позволяет просматривать, редактировать и удалять объявления.
    :param queryset: объекты Bulletin
    :param serializer_class: сериализатор класса Bulletin
    :param permission_classes: классы уровней доступа
    :param pagination_class: пагинатор
    :filter_backends: фильтры
    :filterset_fields: поля для фильтрации
    """

    queryset = Bulletin.objects.all()

    serializer_class = BulletinSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    pagination_class = BulletinPagination

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["title"]


class ReviewViewSet(ModelViewSet):
    """
    API endpoint, который позволяет просматривать, редактировать и удалять отзывы.
    :param queryset: объекты Review
    :param serializer_class: сериализатор класса Review
    :param permission_classes: классы уровней доступа
    :param pagination_class: пагинатор
    """

    queryset = Review.objects.all()

    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    pagination_class = ReviewPagination
