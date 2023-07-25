from abc import ABC, abstractmethod
from typing import Callable

import orjson
from pydantic import BaseModel


def orjson_dumps(data: object, *, default: Callable) -> str:
    """Функция для декодирования в unicode для парсирования объектов на основе pydantic класса.

    Args:
        data: Данные для преобразования
        default: Функция для объектов, которые не могут быть сериализованы.

    Returns:
        str: Строка JSON
    """
    return orjson.dumps(data, default=default).decode()


class OrjsonMixin(BaseModel):
    """Миксин для замены стандартной работы с json на более быструю."""

    class Config:
        """Настройки сериализации."""

        json_loads = orjson.loads
        json_dumps = orjson_dumps


class KafkaEvent(ABC, OrjsonMixin):
    """Абстрактная модель события (сообщения), поступающего в брокер сообщений Kafka."""

    @property
    @abstractmethod
    def key(self) -> str:
        """Свойство с ключом события для разделения данных на партиции.

        Returns:
            str: Ключ партиционирования
        """

    @property
    def value(self) -> str:
        """Свойство со значением события, являющееся содержимым сообщения.

        Returns:
            str: Содержимое события
        """
        return self.json()
