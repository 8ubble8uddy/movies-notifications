from functools import lru_cache

from pydantic import BaseModel, BaseSettings, Field


class KafkaConfig(BaseModel):
    """Класс с настройками подключения к Kafka."""

    host: str = 'localhost'
    port: int = 29092


class FastApiConfig(BaseModel):
    """Класс с настройками подключения к FastAPI."""

    host: str = '0.0.0.0'
    port: int = 8000
    debug: bool = False
    secret_key: str = 'secret_key'
    title: str = 'Post-only API для публикации событий'


class MainSettings(BaseSettings):
    """Класс с основными настройками проекта."""

    fastapi: FastApiConfig = Field(default_factory=FastApiConfig)
    kafka: KafkaConfig = Field(default_factory=KafkaConfig)


@lru_cache()
def get_settings():
    """Функция для создания объекта настроек в едином экземпляре (синглтона).

    Returns:
        MainSettings: Объект с настройками
    """
    return MainSettings(_env_file='.env', _env_nested_delimiter='_')


CONFIG = get_settings()
