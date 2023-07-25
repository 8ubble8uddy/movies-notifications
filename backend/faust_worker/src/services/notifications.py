import logging
from http import HTTPStatus
from typing import Dict, Optional

import aiohttp

from core.config import CONFIG
from core.decorators import aiohttp_error_handler


class NotificationsService:
    """Сервис для выполнения API-запросов к микросервису уведомлений в админке."""

    def __init__(self, session: aiohttp.ClientSession):
        """При инициализации принимает HTTP-сессию между сервером и клиентом.

        Args:
            session: Объект для асинхронной работы с HTTP
        """
        self.session = session

    @aiohttp_error_handler
    async def get_notification_users(self, notification_id: str, offset: int, limit: int) -> Optional[Dict]:
        """Получение пользователей по уведомлению.

        Args:
            notification_id: Идентификатор уведомления
            offset: Отступ
            limit: Лимит

        Returns:
            Optional[Dict]: JSON-ответ
        """
        async with self.session.get(
            url='http://{service_url}/{api_endpoint}/'.format(
                service_url=CONFIG.admin.url,
                api_endpoint=f'api/v1/notifications/{notification_id}/users',
            ),
            params={'offset': offset, 'limit': limit},
        ) as response:
            if response.status == HTTPStatus.OK:
                return (await response.json())
            else:
                logging.error(f'HTTP-ошибка - {response.status}, {response}')
                return None

    @aiohttp_error_handler
    async def create_user_notification(self, email: str, title: str, text: str) -> Optional[Dict]:
        """Создание пользователя и уведомление с ним связанное.

        Args:
            email: Электронная почта
            title: Заголовок уведомления
            text: Текст уведомления

        Returns:
            Optional[Dict]: JSON-ответ
        """
        async with self.session.post(
            url='http://{service_url}/{api_endpoint}/'.format(
                service_url=CONFIG.admin.url,
                api_endpoint='api/v1/users_notifications',
            ),
            json={'email': email, 'title': title, 'text': text},
        ) as response:
            if response.status == HTTPStatus.CREATED:
                return (await response.json())
            else:
                logging.error(f'HTTP-ошибка - {response.status}, {response}')
                return None

    @aiohttp_error_handler
    async def set_delivery_status(self, user_notification_id: str, was_sent: bool) -> Optional[Dict]:
        """Установка флага отправилось уведомление или нет.

        Args:
            user_notification_id: Идентификатор уведомления пользователя
            was_sent: Отправлено ли уведомление

        Returns:
            dict | None: JSON-ответ
        """
        async with self.session.patch(
            url='http://{service_url}/{api_endpoint}/'.format(
                service_url=CONFIG.admin.url,
                api_endpoint=f'api/v1/users_notifications/{user_notification_id}',
            ),
            json={'was_sent': was_sent},
        ) as response:
            if response.status == HTTPStatus.OK:
                return (await response.json())
            else:
                logging.error(f'HTTP-ошибка - {response.status}, {response}')
                return None
