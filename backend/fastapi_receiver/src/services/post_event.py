import logging
from functools import lru_cache

from aiokafka import AIOKafkaProducer
from aiokafka.errors import KafkaError
from fastapi import Depends

from core.enums import KafkaTopics
from db.kafka import get_kafka
from models.base import KafkaEvent


class PostEventService:
    """Сервис для отправки события в брокер сообщений Kafka."""

    def __init__(self, kafka: AIOKafkaProducer):
        """При инициализации класса принимает клиентское приложение-продюсер Kafka.

        Args:
            kafka: Продюсер Kafka
        """
        self.kafka = kafka

    async def produce(self, topic: KafkaTopics, event: KafkaEvent) -> bool:
        """Основной метод публикации события в поток.

        Args:
            topic: Топик в Kafka
            event: Событие для публикции

        Returns:
            bool: Отправлено сообщение или нет
        """
        try:
            result = await self.kafka.send_and_wait(topic.name, event.value, event.key)
        except KafkaError as exc:
            logging.error(exc)
            return False
        logging.info(result)
        return True


@lru_cache()
def get_post_event_service(kafka: AIOKafkaProducer = Depends(get_kafka)) -> PostEventService:
    """Функция для создания объекта сервиса PostEventService в едином экземпляре (синглтона).

    Args:
        kafka: Соединение с Kafka

    Returns:
        PostEventService: Сервис для отправки события в Kafka
    """
    return PostEventService(kafka)
