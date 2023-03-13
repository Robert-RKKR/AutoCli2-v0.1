# Django - models import:
from django.db import models

# AutoCli2 - base model import:
from .base_message import BaseMessageModel

# Notification model constants:
SEVERITY = (
    (1, 'CRITICAL'),
    (2, 'ERROR'),
    (3, 'WARNING'),
    (4, 'INFO'),
    (5, 'DEBUG'),
)
NOTIFICATION_TYPE = (
    (1, 'User notification'),
    (2, 'Backend log')
)


# Notification model class:
class Notification(BaseMessageModel):

    class Meta:
        
        # Model name values:
        verbose_name = 'Notification'
        verbose_name_plural = 'Notifications'

        # Default ordering:
        ordering = ['-pk']

    # Notification severity:
    severity = models.IntegerField(
        verbose_name='Severity level',
        help_text='The level of severity of the performed action.',
        choices=SEVERITY,
        default=0,
    )

    # Type of notification:
    notification_type = models.IntegerField(
        verbose_name='Notification type',
        help_text='Type of notification (User / backlog).',
        choices=NOTIFICATION_TYPE,
        default=1,
    )

    # Task ID information:
    task_id = models.CharField(
        verbose_name='Task ID',
        help_text='ID of the associated task.',
        max_length=64,
        null=True,
        blank=True,
    )

    # Notification main data:
    application = models.CharField(
        verbose_name='Application',
        help_text='Name of the application which triggered the notification.',
        max_length=64
    )
    message = models.CharField(
        verbose_name='Message',
        help_text='Notification message.',
        max_length=512,
        error_messages={
            'null': 'Notification message field is mandatory.',
            'blank': 'Notification message field is mandatory.',
            'invalid': 'Enter a valid Notification message. It must contain 1 to 512 digits.',
        },
    )

    # Object representation:
    def __repr__(self) -> str:
        return f'{self.pk}: {self.message}'

    def __str__(self) -> str:
        return  f'{self.pk}: {self.message}'

    # Natural key representation:
    def natural_key(self):
        return str(self.message)
