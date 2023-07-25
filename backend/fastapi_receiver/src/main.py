import logging

import uvicorn
from fastapi import APIRouter, FastAPI
from fastapi.responses import ORJSONResponse

from api.urls import routes
from core.config import CONFIG
from core.logger import LOGGING
from db import kafka

app = FastAPI(
    title=CONFIG.fastapi.title,
    description='Сервис для публикации и регистрации событий',
    version='1.0.0',
    docs_url='/openapi',
    openapi_url='/openapi.json',
    default_response_class=ORJSONResponse,
)


@app.on_event('startup')
async def startup():
    """Подключаемся к брокеру сообщений Kafka при старте сервера."""
    await kafka.start()


@app.on_event('shutdown')
async def shutdown():
    """Отключаемся от брокера сообщений Kafka при выключении сервера."""
    await kafka.stop()


app.include_router(APIRouter(routes=routes), prefix='/api/v1')


if __name__ == '__main__':
    uvicorn.run(
        'main:app',
        host=CONFIG.fastapi.host,
        port=CONFIG.fastapi.port,
        log_config=LOGGING,
        log_level=logging.DEBUG,
    )
