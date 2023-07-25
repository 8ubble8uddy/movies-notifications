import uuid

from django.db import models


class UUIDMixin(models.Model):
    """Абстрактная модель для генерации первичных ключей."""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        """Метаданные."""

        abstract = True


class TimeStampedMixin(models.Model):
    """Абстрактная модель для отметки времени."""

    created_at = models.DateTimeField(auto_now=True)

    class Meta:
        """Метаданные."""

        abstract = True
