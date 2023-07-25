from django.db.models import F, QuerySet
from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.pagination import LimitOffsetPagination

from api.v1.serializers import UserSerializer, UserNotificationSerializer, UserNotificationCreateSerializer
from notifications.models import Notification, User, UserNotification
from notifications.base.enums import DeliveryMethod


class UserNotificationCreate(generics.CreateAPIView):
    """Высокоуровневый view-класс для создания уведомления пользователя."""

    queryset = UserNotification.objects.all()
    serializer_class = UserNotificationCreateSerializer


class UserNotificationUpdate(generics.UpdateAPIView):
    """Высокоуровневый view-класс для обновления уведомления пользователя."""

    queryset = UserNotification.objects.all()
    serializer_class = UserNotificationSerializer


class UsersListByNotification(generics.ListAPIView):
    """Высокоуровневый view-класс для получения списка пользователей по уведомлению."""

    serializer_class = UserSerializer
    pagination_class = LimitOffsetPagination

    def get_queryset(self) -> QuerySet[User]:
        """Подготовка запроса с пользователями уведомления, за исключением тех, кто отключил оповещения.

        Returns:
            QuerySet[User]: Пользователи в уведомлении
        """
        notification = get_object_or_404(Notification, id=self.kwargs['pk'])
        return notification.users.exclude(delivery_method=DeliveryMethod.NONE).annotate(
            user_notification=F('usernotification'),
        )
