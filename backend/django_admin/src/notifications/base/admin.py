from django.contrib import admin

from notifications.models import UserNotification


class UserNotificationInline(admin.TabularInline):
    """Класс для вставки пользователей в админку уведомлений."""

    model = UserNotification
    autocomplete_fields = ('user',)
    readonly_fields = ('was_sent',)
