# API endpoints for bulletin and review
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet

from .models import Bulletin, Review
from .paginators import BulletinPagination, ReviewPagination
from .serializers import BulletinSerializer, ReviewSerializer


class BulletinViewSet(ModelViewSet):
    queryset = Bulletin.objects.all()
    serializer_class = BulletinSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["title"]
    pagination_class = BulletinPagination

    # TODO: Возможно убрать пагинацию для отдельнго url /ads/
    # @action(detail=False, methods=["get"], url_path="spec_pag")
    # def spec_pag(self, request):
    #     """
    #     Кастомный эндпоинт для /ads/ с пагинацией по 4 объекта.
    #     """
    #     # Установим нужный пагинатор
    #     paginator = AdsPagination()
    #     queryset = self.get_queryset()
    #     page = paginator.paginate_queryset(queryset, request)
    #     if page is not None:
    #         serializer = self.get_serializer(page, many=True)
    #         return paginator.get_paginated_response(serializer.data)
    #     serializer = self.get_serializer(queryset, many=True)
    #     return Response(serializer.data)


class ReviewViewSet(ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    pagination_class = ReviewPagination
