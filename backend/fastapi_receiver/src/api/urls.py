from fastapi.routing import APIRoute

from api.v1 import views

routes = [
    APIRoute(
        path='/new_user',
        methods=['POST'],
        summary='Опубликовать нового пользователя',
        endpoint=views.publish_new_user,
    ),
    APIRoute(
        path='/like_comment',
        methods=['POST'],
        summary='Опубликовать лайк комментарию',
        endpoint=views.publish_like_comment,
    ),
    APIRoute(
        path='/notification',
        methods=['POST'],
        summary='Опубликовать уведомление для пользователей',
        endpoint=views.publish_notification,
    ),
]
