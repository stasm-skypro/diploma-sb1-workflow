# user/utils.py
from django.core.mail import send_mail

from celery import shared_task


@shared_task
def send_welcome_email(user_email):
    """
    Отправляет письмо с приветствием.
    """
    subject = "Добро пожаловать!"
    message = "Спасибо за регистрацию!"
    send_mail(subject, message, "no-reply@example.com", [user_email])


def send_password_reset_email(email: str, reset_url: str):
    """
    Отправляет письмо для сброса пароля.
    """
    subject = "Сброс пароля"
    message = f"Для сброса пароля перейдите по ссылке: {reset_url}"
    send_mail(subject, message, "no-reply@example.com", [email])
