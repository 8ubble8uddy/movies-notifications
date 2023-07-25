import logging
from functools import wraps
from typing import Callable

import aiohttp


def aiohttp_error_handler(func: Callable) -> Callable:
    """Декоратор для обработки ошибки подключения AIOHTTP.

    Args:
        func: Функция для представления запроса

    Returns:
        Callable: Декорируемая функция
    """
    @wraps(func)
    async def wrapper(*args, **kwargs):
        try:
            response = await func(*args, **kwargs)
        except aiohttp.ClientConnectorError as exc:
            logging.critical('Ошибка подключения {exc}'.format(exc=exc))
        return response
    return wrapper
