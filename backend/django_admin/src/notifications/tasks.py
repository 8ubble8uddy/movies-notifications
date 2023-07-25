from uuid import uuid4

from celery import shared_task

from notifications.models import Notification, User
from notifications.utils import publish_notification


@shared_task
def get_new_films(title: str, text: str) -> bool:
    """Функция для генерации уведомления о новых фильмах.

    Args:
        title: Заголовок
        text: Текст

    Returns:
        bool: Выполнилось ли задание
    """
    fake_new_films_from_movies = [{'id': uuid4()} for _ in range(6)]
    notification = Notification.objects.create(
        title=title,
        text=text + '\n' + f'Новые фильмы: {fake_new_films_from_movies}',
    )
    notification.users.add(*User.objects.all())
    publish_notification(notification)
    return True


@shared_task
def bookmark_reminder(title: str, text: str):
    """Функция для генерации уведомления пользователей, которые давно не заходили в закладки.

    Args:
        title: Заголовок
        text: Текст

    Returns:
        bool: Выполнилось ли задание
    """
    fake_users_from_ugc = [{'id': uuid4()} for _ in range(10)]
    users = User.objects.filter(id__in=[user['id'] for user in fake_users_from_ugc])
    if not users:
        return False
    notification = Notification.objects.create(title=title, text=text)
    notification.users.add(*users)
    publish_notification(notification)
    return True
