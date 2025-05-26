# bulletin/utils.py
from django.core.mail import send_mail

from celery import shared_task


@shared_task
def send_review_notification_email(email, bulletin_id, bulletin_title, bulletin_author, review_author, review_text):
    """
    Отправляет уведомительное письмо владельцу объявления о новом отзыве.

    :param email: Email-адрес владельца объявления, на который отправляется письмо.
    :param bulletin_id: Идентификатор объявления.
    :param bulletin_title: Название объявления.
    :param bulletin_author: Email владельца объявления (для персонализации письма).
    :param review_author: Email пользователя, оставившего отзыв.
    :param review_text: Текст отзыва.
    :return: None
    """
    subject = f"Новый отзыв на ваше объявление: {bulletin_title}"
    message = (
        f"Здравствуйте, {bulletin_author}!\n\n"
        f"Пользователь {review_author} оставил отзыв:\n"
        f"«{review_text}»\n\n"
        f"Ссылка на объявление: http://localhost:8000/api/bulletin/bulletins/{bulletin_id}/\n\n"
        f"С уважением,\nКоманда сайта."
    )
    send_mail(subject, message, "no-reply@example.com", [email])
