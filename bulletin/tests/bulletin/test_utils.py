# tests/bulletin/test_utils.py
"""
Тест напрямую вызывает синхронную версию задачи, несмотря на то, что она декорирована @shared_task. Это допустимо,
так как .delay() — лишь обёртка. Используется @patch, чтобы замокать send_mail и не отправлять реальные письма.
pytest.mark.django_db добавлен для совместимости, даже если тут не создаются модели.
"""

from unittest.mock import patch

import pytest

from bulletin.utils import send_review_notification_email


@pytest.mark.django_db
@patch("bulletin.utils.send_mail")
def test_send_review_notification_email(mock_send_mail):
    """
    Тестирует функцию отправки email-уведомления о новом отзыве.

    Проверяет, что функция формирует корректное письмо и вызывает send_mail с ожидаемыми аргументами.
    """
    email = "owner@example.com"
    bulletin_id = 42
    bulletin_title = "Продам велосипед"
    bulletin_author = "owner@example.com"
    review_author = "user@example.com"
    review_text = "Отличное объявление!"

    send_review_notification_email(
        email=email,
        bulletin_id=bulletin_id,
        bulletin_title=bulletin_title,
        bulletin_author=bulletin_author,
        review_author=review_author,
        review_text=review_text,
    )

    expected_subject = "Новый отзыв на ваше объявление: Продам велосипед"
    expected_message = (
        f"Здравствуйте, {bulletin_author}!\n\n"
        f"Пользователь {review_author} оставил отзыв:\n"
        f"«{review_text}»\n\n"
        f"Ссылка на объявление: http://localhost:8000/api/bulletin/bulletins/{bulletin_id}/\n\n"
        f"С уважением,\nКоманда сайта."
    )

    mock_send_mail.assert_called_once_with(
        expected_subject,
        expected_message,
        "no-reply@example.com",
        [email],
    )
