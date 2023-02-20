# Django import:
from django.db import models

# Base models import:
from autocli2.base.models.identification import IdentificationModel
from autocli2.base.models.data_time import DataTimeModel
from autocli2.base.models.status import StatusModel


# Data time models class:
class ApiData(StatusModel, DataTimeModel, IdentificationModel):

    class Meta:
        
        # Model name values:
        verbose_name = 'API data'
        verbose_name_plural = 'API data'

        # Abstract class value:
        abstract = True

    # API token information:
    http_token_heder_key = models.CharField(
        verbose_name='Xxx',
        help_text='Xxx.',
        max_length=128,
        null=True,
        blank=True,
    )

    http_token_heder_value = models.CharField(
        verbose_name='Xxx',
        help_text='Xxx.',
        max_length=128,
        null=True,
        blank=True,
    )

    # Pagination information:
    http_pagination = models.BooleanField(
        verbose_name='HTTP(S) pagination',
        help_text='If this option is active, the API request is repeated '\
        'to collect all objects from all paginated pages.',
        default=True,
    )

    http_pagination_path = models.JSONField(
        verbose_name='HTTP(S) pagination path',
        help_text='The pagination path value is used to retrieve information '\
        'about the next pagination page from APi requests (Required only if '\
        'the HTTP(S) pagination field is enabled).',
        null=True,
        blank=True,
    )

    http_next_page_path = models.JSONField(
        verbose_name='HTTP(S) next page path',
        help_text='Xxx',
        null=True,
        blank=True,
    )

    http_pagination_param_key = models.CharField(
        verbose_name='Xxx',
        help_text='Xxx.',
        max_length=128,
        null=True,
        blank=True,
    )

    # Data path:
    http_data_path = models.JSONField(
        verbose_name='HTTP(S) data path',
        help_text='Xxx',
        null=True,
        blank=True,
    )

    # API related default fields:
    http_default_header = models.JSONField(
        verbose_name='HTTP(S) default heder',
        help_text='Xxx.',
        null=True,
        blank=True,
    )

    http_default_params = models.JSONField(
        verbose_name='HTTP(S) default parameters',
        help_text='Xxx.',
        null=True,
        blank=True,
    )
