from abc import ABC, abstractmethod
from typing import Dict

from models.records import Notification


class DeliveryService(ABC):
    """Абстрактный сервис для доставки уведомления."""

    @classmethod
    @abstractmethod
    def send(cls, user: Dict, notification: Notification) -> bool:
        """Оcновной метод отправки уведомления.

        Args:
            user: Данные пользователя
            notification: Уведомление

        Returns:
            bool: Отправлено ли сообщение
        """


class EmailService(DeliveryService):
    """Сервис для доставки уведомления по электронной почте."""

    @classmethod
    def send(cls, user: Dict, notification: Notification) -> bool:
        """Отправка уведомления через EMAIL.

        Args:
            user: Данные пользователя
            notification: Уведомление

        Returns:
            bool: Отправлено ли сообщение
        """
        return True


class SmsService(DeliveryService):
    """Сервис для доставки уведомления по телефонному номеру."""

    @classmethod
    def send(cls, user: Dict, notification: Notification) -> bool:
        """Отправка уведомления через SMS.

        Args:
            user: Данные пользователя
            notification: Уведомление

        Returns:
            bool: Отправлено ли сообщение
        """
        return True


class PushService(DeliveryService):
    """Сервис для доставки уведомления с помощью технологию Push."""

    @classmethod
    def send(cls, user: Dict, notification: Notification) -> bool:
        """Отправка уведомления через Push.

        Args:
            user: Данные пользователя
            notification: Уведомление

        Returns:
            bool: Отправлено ли сообщение
        """
        return True
