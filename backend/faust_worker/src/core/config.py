from functools import lru_cache

from pydantic import BaseModel, BaseSettings, Field


class KafkaConfig(BaseModel):
    """Класс с настройками подключения к Kafka."""

    host: str = 'localhost'
    port: int = 29092

    @property
    def url(self) -> str:
        """Свойство с url-адресом брокера.

        Returns:
            str: URL Kafka
        """
        return 'kafka://{host}:{port}'.format(host=self.host, port=self.port)


class FaustConfig(BaseModel):
    """Класс с настройками подключения к Faust."""

    title: str = 'Worker'


class AdminConfig(BaseModel):
    """Класс с настройками подключения к админ-панели."""

    url: str = 'localhost:8000'


class MainSettings(BaseSettings):
    """Основной класс со всеми настройками."""

    faust: FaustConfig = Field(default_factory=FaustConfig)
    kafka: KafkaConfig = Field(default_factory=KafkaConfig)
    admin: AdminConfig = Field(default_factory=AdminConfig)


@lru_cache()
def get_settings() -> MainSettings:
    """
    Функция для создания объекта настроек в едином экземпляре (синглтона).

    Returns:
        MainSettings: Объект с настройками
    """
    return MainSettings(_env_file='.env', _env_nested_delimiter='_')  # type: ignore[call-arg]


CONFIG = get_settings()
