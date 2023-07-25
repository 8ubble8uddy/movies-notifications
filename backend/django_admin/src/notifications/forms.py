from django import forms

from notifications.models import Notification


class NotificationForm(forms.ModelForm):
    """Форма модели уведолмения для добавления дополнительного поля."""

    all_users = forms.BooleanField(
        required=False,
        label='Все пользователи',
        help_text='Отправить уведомление всем пользователям',
    )

    class Meta:
        """Метаданные."""

        model = Notification
        fields = '__all__'
