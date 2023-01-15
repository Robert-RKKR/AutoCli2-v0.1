# Django import:
from django.db import models

# Base model import:
from message.base.base_model.models.base_model import BaseModel

# Manager class import:
from message.notification.managers.notification import NotificationManager

# Validators import:
from message.base.base_model.validators.base_validators import NameValueValidator


# Notification models:
class Notification(BaseModel):

    class Meta:
        
        # Model name values:
        verbose_name = 'Notification'
        verbose_name_plural = 'Notifications'

        # Default ordering:
        ordering = ['-pk']

    # Validators:
    name_validator = NameValueValidator()

    # Model objects manager:
    objects = NotificationManager()

    # Notification main data:
    application = models.CharField(
        verbose_name='Application',
        help_text='Name of the application which triggered the notification.',
        max_length=64,
        validators=[name_validator],
        error_messages={
            'null': 'Notification message field is mandatory.',
            'blank': 'Notification message field is mandatory.',
            'invalid': 'Enter a valid Notification name. '\
                'It must contain 4 to 256 digits, letters and special characters -, _, . or spaces.',
        },
    )
    message = models.CharField(
        verbose_name='Message',
        help_text='Notification message.',
        max_length=256,
        error_messages={
            'null': 'Notification message field is mandatory.',
            'blank': 'Notification message field is mandatory.',
            'invalid': 'Enter a valid Notification message. It must contain 1 to 256 digits.',
        },
    )

    # Model representation:
    def __str__(self) -> str:
        return f'{self.pk} - {self.message}'
