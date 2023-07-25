from http import HTTPStatus

from fastapi import Body, Depends, HTTPException, Response

from services.post_event import PostEventService, get_post_event_service
from core.enums import KafkaTopics
from models import events


async def publish_new_user(
    new_user: events.NewUser = Body(title='Новый пользователь'),
    kafka: PostEventService = Depends(get_post_event_service),
) -> Response:
    """Представление для публикации события о новом пользователе.

    Args:
        new_user: Событие `новый пользователь`
        kafka: Объект для публикации события в Kafka

    Raises:
        HTTPException: Ошибка 400, если сервер Kafka недоступен

    Returns:
        Response: HTTP-ответ с кодом 200
    """
    ok = await kafka.produce(topic=KafkaTopics.new_users, event=new_user)
    if not ok:
        raise HTTPException(status_code=HTTPStatus.BAD_REQUEST)
    return Response(status_code=HTTPStatus.CREATED)


async def publish_like_comment(
    like_comment: events.LikeComment = Body(title='Лайк комментарию'),
    kafka: PostEventService = Depends(get_post_event_service),
) -> Response:
    """Представление для публикации события о лайке комментарию.

    Args:
        like_comment: Событие `лайк комментарию`
        kafka: Объект для публикации события в Kafka

    Raises:
        HTTPException: Ошибка 400, если сервер Kafka недоступен

    Returns:
        Response: HTTP-ответ с кодом 200
    """
    ok = await kafka.produce(topic=KafkaTopics.comment_likes, event=like_comment)
    if not ok:
        raise HTTPException(status_code=HTTPStatus.BAD_REQUEST)
    return Response(status_code=HTTPStatus.CREATED)


async def publish_notification(
    notification: events.Notification = Body(title='Уведомление пользователей'),
    kafka: PostEventService = Depends(get_post_event_service),
) -> Response:
    """Представление для публикации событии об уведомлении для пользователей.

    Args:
        notification: Событие `уведомление пользователей`
        kafka: Объект для публикации события в Kafka

    Raises:
        HTTPException: Ошибка 400, если сервер Kafka недоступен

    Returns:
        Response: HTTP-ответ с кодом 200
    """
    ok = await kafka.produce(topic=KafkaTopics.notifications, event=notification)
    if not ok:
        raise HTTPException(status_code=HTTPStatus.BAD_REQUEST)
    return Response(status_code=HTTPStatus.CREATED)
