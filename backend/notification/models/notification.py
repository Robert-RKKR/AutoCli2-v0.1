# Django - models import:
from django.db import models

# Django - translation model import:
from django.utils.translation import gettext_lazy as _

# AutoCli2 - base model import:
from .base_message import BaseMessageModel

# AutoCli2 - constance import:
from autocli2.base.constants.notification_type import NotificationTypeChoices
from autocli2.base.constants.severity import SeverityChoices


# Notification model class:
class Notification(BaseMessageModel):

    class Meta:
        
        # Model name values:
        verbose_name = _('Notification')
        verbose_name_plural = _('Notifications')

        # Default ordering:
        ordering = ['-pk']

    # Notification severity:
    severity = models.IntegerField(
        verbose_name=_('Severity level'),
        help_text=_('The level of severity of the performed action.'),
        choices=SeverityChoices.choices,
        default=0,
    )

    # Type of notification:
    notification_type = models.IntegerField(
        verbose_name=_('Notification type'),
        help_text=_('Type of notification (User / backlog).'),
        choices=NotificationTypeChoices.choices,
        default=1,
    )

    # Task ID information:
    task_id = models.CharField(
        verbose_name=_('Task ID'),
        help_text=_('ID of the associated task.'),
        max_length=64,
        null=True,
        blank=True,
    )

    # Notification main data:
    application = models.CharField(
        verbose_name=_('Application'),
        help_text=_('Name of the application which triggered the notification.'),
        max_length=64
    )
    message = models.CharField(
        verbose_name=_('Message'),
        help_text=_('Notification message.'),
        max_length=1024,
        error_messages={
            'invalid': _('Enter a valid Notification message. It must contain 1 to 1024 digits.'),
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
