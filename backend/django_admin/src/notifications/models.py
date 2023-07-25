from django.db import models
from django.utils.translation import gettext_lazy as _

from notifications.base.enums import DeliveryMethod
from notifications.base.models import TimeStampedMixin, UUIDMixin

DEFAULT_LENGTH = 255


class User(UUIDMixin):
    """Модель для пользователя с настройками уведомлений."""

    email = models.EmailField(_('email'), max_length=DEFAULT_LENGTH)
    delivery_method = models.CharField(
        _('delivery_method'),
        choices=DeliveryMethod.choices,
        default=DeliveryMethod.EMAIL,
        max_length=DEFAULT_LENGTH,
    )

    class Meta:
        """Метаданные."""

        db_table = 'users'
        verbose_name = _('user')
        verbose_name_plural = _('users')


class Notification(UUIDMixin, TimeStampedMixin):
    """Модель для уведомления."""

    title = models.CharField(_('title'), max_length=DEFAULT_LENGTH)
    text = models.TextField(_('text'), blank=True)
    users = models.ManyToManyField(
        User,
        through='UserNotification',
        related_name='notifications',
    )

    class Meta:
        """Метаданные."""

        db_table = 'notifications'
        verbose_name = _('notification')
        verbose_name_plural = _('notifications')


class UserNotification(UUIDMixin, TimeStampedMixin):
    """Модель для истории отправки уведомления пользователю."""

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name=_('user'),
    )
    notification = models.ForeignKey(
        Notification,
        on_delete=models.CASCADE,
        verbose_name=_('notification'),
    )
    was_sent = models.BooleanField(_('was_sent'), default=False)

    class Meta:
        """Метаданные."""

        db_table = 'user_notifications'
        verbose_name = _('user notifications')
        verbose_name_plural = _('user notifications')
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'notification'],
                name='unique_user_notification',
            ),
        ]
