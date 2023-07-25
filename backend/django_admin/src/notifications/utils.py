import logging

import requests
from django.conf import settings
from requests.exceptions import ConnectionError, HTTPError

from notifications.models import Notification


def publish_notification(obj: Notification):
    """Публикация события в Kafka через запрос к стороннему микросервису.

    Args:
        obj: Объект уведомления
    """
    try:
        requests.post(
            url='http://{service_url}/api/events/v1/notification'.format(service_url=settings.EVENT_SOURCING_URL),
            json={'notification_id': str(obj.id), 'title': obj.title, 'text': obj.text},
        ).raise_for_status()
    except HTTPError as exc:
        logging.error(f'Не удалось опубликовать событие по причине {exc}')
    except ConnectionError as exc:
        logging.critical(f'Ошибка подключения: {exc}')
    else:
        logging.info('Уведомление создано и передано на обработку!')
