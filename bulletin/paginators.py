from rest_framework.pagination import PageNumberPagination


class BulletinPagination(PageNumberPagination):
    """
    Пагинатор для объявлений (bulletin).
    :param page_size: Значение по умолчанию — сколько объектов выводить на страницу, если клиент не указал явно.
    :param page_size_query_param: Позволяет клиенту (например, в Postman или фронте) переопределить page_size
        через URL, например: ?page_size=5.
    :param max_page_size: Ограничивает максимум, который может запросить клиент через ?page_size=...
    """

    page_size = 4
    page_size_query_param = "page_size"
    max_page_size = 10


class ReviewPagination(PageNumberPagination):
    """
    Пагинатор для отзывов (review).
    :param page_size: Значение по умолчанию — сколько объектов выводить на страницу, если клиент не указал явно.
    :param page_size_query_param: Позволяет клиенту (например, в Postman или фронте) переопределить page_size
        через URL, например: ?page_size=5.
    :param max_page_size: Ограничивает максимум, который может запросить клиент через ?page_size=...
    """

    page_size = 4
    page_size_query_param = "page_size"
    max_page_size = 10
