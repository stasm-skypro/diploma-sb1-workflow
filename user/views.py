# -----------------------------------------------------------------------------
# API endpoints for User
# -----------------------------------------------------------------------------
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny

from .serializers import RegisterSerializer  # type: ignore[reportUnusedImport]
from .utils import send_welcome_email

# from rest_framework.response import Response
# from rest_framework import status


class RegisterAPIView(CreateAPIView):
    """
    Регистрация нового пользователя.
    Параметры запроса:
    - email (str): Email пользователя;
    - password (str): Пароль не менее 8 символов;

    Клиент (например, фронтенд) отправляет POST-запрос на эндпоинт регистрации (например, /api/register/),
    передавая JSON:
    {
        "email": "user@example.com",
        "password": "secure1234"
    }

    API возвращает успешный ответ, например:
    {
        "message": "Регистрация пользователя user@example.com прошла успешно."
    }
    """

    serializer_class = RegisterSerializer
    permission_classes = (AllowAny,)

    def perform_create(self, serializer):
        """
        Сохраняет новый объект, используя переданный сериализатор.

        Этот метод вызывается после успешной валидации данных.
        Здесь можно переопределить или расширить логику создания объекта,
        например, установить текущего пользователя в качестве владельца
        или выполнить дополнительные действия (логирование, отправка писем и т.п.).

        :param serializer: Валидированный сериализатор, содержащий данные для создания объекта.
        :type serializer: rest_framework.serializers.Serializer
        """
        user = serializer.save(owner=self.request.user)
        send_welcome_email(user.email)

    def create(self, request, *args, **kwargs):
        """
        Обрабатывает POST-запрос на создание нового объекта.

        Метод вызывается при отправке POST-запроса к API-представлению,
        основанному на CreateAPIView. Валидирует входные данные, сохраняет
        новый объект и возвращает ответ с данными или сообщением.

        :param request: HTTP-запрос, содержащий входные данные (обычно JSON).
        :type request: rest_framework.request.Request
        :param args: Дополнительные позиционные аргументы.
        :param kwargs: Дополнительные именованные аргументы.
        :return: HTTP-ответ с сообщением об успешном создании объекта или ошибками валидации.
        :rtype: rest_framework.response.Response
        """
        response = super().create(request, *args, **kwargs)
        email = request.data.get("email")
        response.data = {"message": f"Регистрация пользователя {email} прошла успешно."}
        return response

    # Другой вариант - более простой, но менее правильный с точки зрения архитектуры DRF.
    # def create(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     user = serializer.save(owner=self.request.user)
    #     send_welcome_email(user.email)
    #     return Response(
    #         {"message": f"Регистрация пользователя {user.email} прошла успешно."},
    #         status=status.HTTP_201_CREATED,
    #     )
