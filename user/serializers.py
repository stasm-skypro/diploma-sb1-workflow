from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from user.models import User


class RegisterSerializer(serializers.ModelSerializer):
    """
    Представляет сериализатор для регистрации пользователя.
    Attributes:
        email (str): Электронная почта пользователя
        password (str): Пароль пользователя
    """

    # Чтобы не было попыток зарегистрировать одного и того же пользователя дважды
    email = serializers.EmailField(validators=[UniqueValidator(queryset=User.objects.all())])

    # Добавляем подтверждение пароля
    password = serializers.CharField(write_only=True, min_length=8)
    password_confirmation = serializers.CharField(write_only=True)

    def validate(self, attrs):
        """
        Проверяет, что пароли совпадают.
        """
        data = super().validate(attrs)
        if data["password"] != data["password_confirmation"]:
            raise serializers.ValidationError("Пароли не совпадают!")
        return data

    def create(self, validated_data):
        """
        Создает новый объект пользователя.
        """
        # статический анализатор не знает о существовании метода create_user в менеджере модели User
        user = User.objects.create_user(  # type: ignore
            email=validated_data.get("email"), password=validated_data["password"]
        )
        return user

    class Meta:
        """
        Говорит сериализатору, что он работает с моделью User, и обрабатывает только поля email и password.
        """

        model = User
        fields = ("email", "password")


class EmailTokenObtainPairSerializer(TokenObtainPairSerializer):
    username_field = "email"
