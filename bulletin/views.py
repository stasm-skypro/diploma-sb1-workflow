# bulletin/views.py
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet

from .models import Bulletin, Review
from .paginators import BulletinPagination, ReviewPagination
from .permissions import IsAuthenticatedOrReadOnlyForReviews, IsAuthorOrAdminOrReadOnlyForBulletin
from .serializers import BulletinCreateSerializer, BulletinDetailSerializer, BulletinListSerializer, ReviewSerializer
from .utils import send_review_notification_email


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

    search_fields = ["title"]
    ordering_fields = ["title", "price", "created_at"]

    def get_serializer_class(self):  # type: ignore
        if self.action == "list":
            return BulletinListSerializer
        elif self.action == "retrieve":
            return BulletinDetailSerializer
        return BulletinCreateSerializer


class ReviewViewSet(ModelViewSet):
    """
    API endpoint, который позволяет просматривать, редактировать и удалять отзывы.
    :param queryset: Объекты Review
    :param serializer_class: сериализатор класса Review
    :param permission_classes: классы уровней доступа
    :param pagination_class: пагинатор
    """

    queryset = Review.objects.all().order_by("-created_at")

    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticatedOrReadOnlyForReviews]
    pagination_class = ReviewPagination
    filterset_fields = ["bulletin"]  # Позволяет ?bulletin=<id>

    search_fields = ["text", "created_at"]
    ordering_fields = ["created_at"]

    def perform_create(self, serializer):  # type: ignore
        """
        Сохраняет новый отзыв, устанавливая текущего пользователя автором,
        и инициирует отправку уведомительного письма владельцу объявления.

        :param serializer: Экземпляр сериализатора, содержащий проверенные данные отзыва.
        :return: None
        """
        # Назначаем текущего пользователя автором
        review = serializer.save(author=self.request.user)

        # Отправляем письмо владельцу объявления
        bulletin = review.bulletin
        email = bulletin.author.email
        bulletin_id = bulletin.id
        bulletin_title = bulletin.title
        bulletin_author = bulletin.author.email
        review_author = review.author.email
        review_text = review.text

        send_review_notification_email.delay(
            email=email,
            bulletin_id=bulletin_id,
            bulletin_title=bulletin_title,
            bulletin_author=bulletin_author,
            review_author=review_author,
            review_text=review_text,
        )
