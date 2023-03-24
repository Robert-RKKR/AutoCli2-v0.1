# Django - models import:
from django.db import models

# AutoCli2 - base model import:
from .base_message import BaseMessageModel

# AutoCli2 - constance import:
from autocli2.base.constants.notification_type import NotificationTypeChoices
from autocli2.base.constants.severity import SeverityChoices


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
        choices=SeverityChoices.choices,
        default=0,
    )

    # Type of notification:
    notification_type = models.IntegerField(
        verbose_name='Notification type',
        help_text='Type of notification (User / backlog).',
        choices=NotificationTypeChoices.choices,
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
        max_length=1024,
        error_messages={
            'null': 'Notification message field is mandatory.',
            'blank': 'Notification message field is mandatory.',
            'invalid': 'Enter a valid Notification message. It must contain 1 to 1024 digits.',
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
