# Django - models import:
from django.db import models

# Django - translation model import:
from django.utils.translation import gettext_lazy as _

# AutoCli2 - base model import:
from .base_message import BaseMessageModel


# Change model class:
class ChangeLog(BaseMessageModel):

    class Meta:
        
        # Model name values:
        verbose_name = _('Change')
        verbose_name_plural = _('Changes')

        # Default ordering:
        ordering = ['-pk']

    # Change details:
    after = models.JSONField(
        verbose_name=_('JSON object representation'),
        help_text=_('JSON object representation after changes was made, and saved to database.'),
        null=True,
        blank=True,
    )
