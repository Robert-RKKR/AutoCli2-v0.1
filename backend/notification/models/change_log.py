# Django - models import:
from django.db import models

# AutoCli2 - base model import:
from .base_message import BaseMessageModel


# Change model class:
class ChangeLog(BaseMessageModel):

    class Meta:
        
        # Model name values:
        verbose_name = 'Change'
        verbose_name_plural = 'Changes'

        # Default ordering:
        ordering = ['-pk']

    # Change details:
    after = models.JSONField(
        verbose_name='JSON object representation',
        help_text='JSON object representation after changes was made, and saved to database.',
        null=True,
        blank=True,
    )
