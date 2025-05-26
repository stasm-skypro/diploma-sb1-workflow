# bulletin/views.py
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet

from .models import Bulletin, Review
from .paginators import BulletinPagination, ReviewPagination
from .permissions import IsAuthenticatedOrReadOnlyForReviews, IsAuthorOrAdminOrReadOnlyForBulletin
from .serializers import BulletinCreateSerializer, BulletinDetailSerializer, BulletinListSerialiser, ReviewSerializer


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

    queryset = Bulletin.objects.all().order_by("-created_at")

    permission_classes = [IsAuthorOrAdminOrReadOnlyForBulletin]
    pagination_class = BulletinPagination

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["title"]

    def get_serializer_class(self):  # type: ignore
        if self.action == "list":
            return BulletinListSerialiser
        elif self.action == "retrieve":
            return BulletinDetailSerializer
        return BulletinCreateSerializer


class ReviewViewSet(ModelViewSet):
    """
    API endpoint, который позволяет просматривать, редактировать и удалять отзывы.
    :param queryset: объекты Review
    :param serializer_class: сериализатор класса Review
    :param permission_classes: классы уровней доступа
    :param pagination_class: пагинатор
    """

    queryset = Review.objects.all().order_by("-created_at")

    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticatedOrReadOnlyForReviews]
    pagination_class = ReviewPagination
    filterset_fields = ["bulletin"]  # Позволяет ?bulletin=<id>
