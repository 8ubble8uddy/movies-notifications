from typing import Optional

from aiokafka import AIOKafkaProducer
from kafka.admin import KafkaAdminClient, NewTopic

from core.config import CONFIG
from core.enums import KafkaTopics

kafka: Optional[AIOKafkaProducer] = None


def create_topics():
    """Функция для создания топиков в Kafka."""
    admin_client = KafkaAdminClient(
        bootstrap_servers='{host}:{port}'.format(host=CONFIG.kafka.host, port=CONFIG.kafka.port),
    )
    topics = admin_client.list_topics()
    admin_client.create_topics(
        new_topics=[
            NewTopic(
                name=topic,
                num_partitions=1,
                replication_factor=1,
            ) for topic in KafkaTopics.__members__ if topic not in topics
        ],
    )
    admin_client.close()


async def start():
    """Функция для подключения к хранилищу событий Kafka."""
    global kafka
    kafka = AIOKafkaProducer(
        bootstrap_servers='{host}:{port}'.format(host=CONFIG.kafka.host, port=CONFIG.kafka.port),
        value_serializer=lambda value: bytes(value, 'UTF-8'),
        key_serializer=lambda key: bytes(key, 'UTF-8'),
    )
    create_topics()
    await kafka.start()


async def stop():
    """Функция для отключения от хранилища событий Kafka."""
    await kafka.stop()


async def get_kafka():
    """Функция для объявления соединения с Kafka, которая понадобится при внедрении зависимостей.

    Returns:
        AIOKafkaProducer: Соединение с Kafka
    """
    return kafka
