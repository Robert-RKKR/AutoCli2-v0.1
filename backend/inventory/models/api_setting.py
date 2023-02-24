# Django import:
from django.db import models

# Base models import:
from autocli2.base.models.identification import IdentificationModel
from autocli2.base.models.data_time import DataTimeModel
from autocli2.base.models.status import StatusModel


# Api setting model class:
class ApiSetting(StatusModel, DataTimeModel, IdentificationModel):

    class Meta:
        
        # Model name values:
        verbose_name = 'Api setting'
        verbose_name_plural = 'Api settings'

    # Default host API settings:
    api_token_key_name = models.CharField(
        verbose_name='API token value',
        help_text='Xxx.',
        max_length=128,
        null=True,
        blank=True,
    )
    
    api_token_key_value = models.CharField(
        verbose_name='API token value name',
        help_text='Xxx',
        max_length=128,
        null=True,
        blank=True,
    )
    
    api_pagination_path = models.JSONField(
        verbose_name='API pagination path',
        help_text='Xxx',
        null=True,
        blank=True,
    )

    api_pagination_key = models.CharField(
        verbose_name='API pagination key',
        help_text='Xxx',
        max_length=128,
        null=True,
        blank=True,
    )

    api_data_path = models.JSONField(
        verbose_name='API data items path',
        help_text='Xxx',
        null=True,
        blank=True,
    )

    # Default settings:
    default_api_header = models.JSONField(
        verbose_name='Default HTTP heder',
        help_text='Xxx.',
        null=True,
        blank=True,
    )

    default_api_params = models.JSONField(
        verbose_name='Default HTTP parameters',
        help_text='Xxx.',
        null=True,
        blank=True,
    )
