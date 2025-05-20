# * URL for user *

from django.urls import path

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from user.apps import UserConfig

from .views import RegisterAPIView

app_name = UserConfig.name


urlpatterns = [
    path("register/", RegisterAPIView.as_view(), name="register"),  # регистрация пользователя
    path("login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),  # логин
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),  # обновление токена
]
