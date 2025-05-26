# user/utils.py
from django.core.mail import send_mail

from celery import shared_task


@shared_task
def send_welcome_email(user_email):
    """
    Отправляет пользователю приветственное письмо после регистрации.

    :param user_email: Email-адрес пользователя, которому отправляется приветственное сообщение.
    :return: None
    """
    subject = "Добро пожаловать!"
    message = "Спасибо за регистрацию!"
    send_mail(subject, message, "no-reply@example.com", [user_email])


def send_password_reset_email(email: str, reset_url: str):
    """
    Отправляет письмо со ссылкой для сброса пароля.

    :param email: Email-адрес пользователя, запрашивающего сброс пароля.
    :param reset_url: Уникальная ссылка для сброса пароля.
    :return: None
    """
    subject = "Сброс пароля"
    message = f"Для сброса пароля перейдите по ссылке: {reset_url}"
    send_mail(subject, message, "no-reply@example.com", [email])
