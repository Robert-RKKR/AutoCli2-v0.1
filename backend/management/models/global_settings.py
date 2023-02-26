# Django import:
from django.db import models

# Base models import:
from autocli2.base.models.identification import IdentificationModel
from autocli2.base.models.data_time import DataTimeModel

# Notification severity import:
from notification.models.notification import SEVERITY


# Global setting model class:
class GlobalSetting(DataTimeModel, IdentificationModel):

    class Meta:
        
        # Model name values:
        verbose_name = 'Global setting'
        verbose_name_plural = 'Global settings'

    # Current global settings:
    is_current = models.BooleanField(
        verbose_name='Current global settings',
        help_text='Xxx',
        default=True,
    )

    # Global settings:
    notification_level = models.IntegerField(
        verbose_name='Notification severity level',
        help_text='The level of severity of the performed action.',
        choices=SEVERITY,
        default=0,
    )

    logger_level = models.IntegerField(
        verbose_name='Logger severity level',
        help_text='The level of severity of the performed action.',
        choices=SEVERITY,
        default=0,
    )
