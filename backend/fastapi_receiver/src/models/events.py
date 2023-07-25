from datetime import datetime
from uuid import UUID

from pydantic import EmailStr

from models.base import KafkaEvent


class NewUser(KafkaEvent):
    """Модель события для публикации нового пользователя."""

    user_id: UUID
    email: EmailStr

    @property
    def key(self) -> str:
        """Свойство с ключом события для партиционирование по дате.

        Returns:
            str: Ключ партиционирования
        """
        return datetime.now().strftime('%m/%d/%Y, %H:%M:%S')


class LikeComment(KafkaEvent):
    """Модель события для публикации лайка комментарию пользователя."""

    user_id: UUID
    comment_id: UUID

    @property
    def key(self) -> str:
        """Свойство с ключом события для партиционирование по пользователям и комментариям.

        Returns:
            str: Ключ партиционирования
        """
        return '{user}::{comment}'.format(user=self.user_id, comment=self.comment_id)


class Notification(KafkaEvent):
    """Модель события для публикации уведомления пользователям."""

    notification_id: UUID
    title: str
    text: str

    @property
    def key(self) -> str:
        """Свойство с ключом события для партиционирование по дате.

        Returns:
            str: Ключ партиционирования
        """
        return datetime.now().strftime('%m/%d/%Y, %H:%M:%S')
