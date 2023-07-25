from typing import Dict

from rest_framework import serializers

from notifications.models import Notification, User, UserNotification


class UserSerializer(serializers.ModelSerializer):
    """Сериализатор модели пользователя."""

    user_notification = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        """Метаданные."""

        fields = ('id', 'email', 'delivery_method', 'user_notification')
        model = User


class UserNotificationSerializer(serializers.ModelSerializer):
    """Сериализатор модели уведомления пользователя."""

    class Meta:
        """Метаданные."""

        fields = ('id', 'notification', 'user', 'was_sent')
        model = UserNotification


class UserNotificationCreateSerializer(serializers.ModelSerializer):
    """Сериализатор модели уведомления пользователя для создания."""

    email = serializers.CharField(write_only=True)
    title = serializers.CharField(write_only=True)
    text = serializers.CharField(write_only=True)

    class Meta:
        """Метаданные."""

        fields = ('id', 'email', 'title', 'text')
        model = UserNotification

    def create(self, validated_data: Dict) -> UserNotification:
        """Переопределение сохранения данных, чтобы создать объекты уведомления и пользователя.

        Args:
            validated_data: Данные после валидации

        Returns:
            UserNotification: Уведомление пользователя
        """
        email = validated_data.pop('email')
        data = {
            'notification': Notification.objects.create(**validated_data),
            'user': User.objects.create(email=email),
        }
        return super().create(data)
