from enum import Enum


class KafkaTopics(Enum):
    """Класс с перечислением топиков в Kafka."""

    new_users = 'new_users'
    comment_likes = 'comment_likes'
    notifications = 'notifications'
