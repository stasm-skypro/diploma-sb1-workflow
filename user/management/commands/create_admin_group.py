from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.core.management.base import BaseCommand

from bulletin.models import Bulletin, Review


class Command(BaseCommand):
    """
    Кастомная команда. Создаёт группу 'Администраторы' и наделяёт её правами просматривать и редактировать курсы
    и уроки.
    """

    help = "Создает группу 'Администраторы' с правами на на CRUD-операции с объявлениями и отзывами всех пользователей"

    def handle(self, *args, **kwargs):
        # Получаем или создаём группу Администраторы
        group, created = Group.objects.get_or_create(name="Администраторы")

        # Извлекаем разрешения по ContentType для моделей Bulletin и Review
        bulletin_perms = Permission.objects.filter(
            content_type=ContentType.objects.get_for_model(Bulletin),
            codename__in=["add_bulletin", "change_bulletin", "delete_bulletin"],
        )
        review_perms = Permission.objects.filter(
            content_type=ContentType.objects.get_for_model(Review),
            codename__in=["add_review", "change_review", "delete_review"],
        )

        # Назначаем права группе
        group.permissions.set(list(bulletin_perms) + list(review_perms))

        self.stdout.write(self.style.SUCCESS('Группа "Администраторы" создана и права назначены'))
