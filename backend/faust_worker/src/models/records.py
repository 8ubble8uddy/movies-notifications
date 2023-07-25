import faust


class Notification(faust.Record):
    """Модель публикации уведолмения."""

    notification_id: str
    title: str
    text: str


class NewUser(faust.Record):
    """Модель публикации нового пользователя."""

    user_id: str
    email: str


class LikeComment(faust.Record):
    """Модель публикации лайка комментарию."""

    user_id: str
    comment_id: str
