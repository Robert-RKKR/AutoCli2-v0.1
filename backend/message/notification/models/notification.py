# Django import:
from django.db import models

# Base model import:
from message.base.base_model.model.base_model import BaseModel

# Manager class import:
from message.notification.managers.notification import NotificationManager


# Notification models:
class Notification(BaseModel):

    class Meta:
        
        # Model name values:
        verbose_name = 'Notification'
        verbose_name_plural = 'Notifications'

        # Default ordering:
        ordering = ['-pk']

    # Model objects manager:
    objects = NotificationManager()

    # Notification main data:
    application = models.CharField(
        verbose_name='Application',
        help_text='Name of the application which triggered the notification.',
        max_length=64,
    )
    message = models.CharField(
        verbose_name='Message',
        help_text='Notification message.',
        max_length=256,
    )

    # Model representation:
    def __str__(self) -> str:
        return f'{self.pk} - {self.message}'
