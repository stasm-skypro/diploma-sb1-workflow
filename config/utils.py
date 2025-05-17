import os

from dotenv import load_dotenv

load_dotenv(override=True)


class ImproperlyConfigured(Exception):
    """Ошибка при неправильной настройке окружения."""

    pass


def get_env(var_name: str, default=None, required=False):
    """Получить переменную окружения или выбросить ошибку, если она обязательная."""
    value = os.environ.get(var_name, default)
    if required and value is None:
        raise ImproperlyConfigured(f"Переменная окружения '{var_name}' обязательна, но не установлена.")
    return value
