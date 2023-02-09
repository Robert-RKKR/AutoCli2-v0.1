# Django import:
from django.db import models

# Base models import:
from autocli2.base.models.identification import IdentificationModel
from autocli2.base.models.data_time import DataTimeModel
from autocli2.base.models.status import StatusModel

# Relations models import:
from .credentials import Credential
from .platform import Platform
from .site import Site


# Host model class:
class Host(StatusModel, DataTimeModel, IdentificationModel):

    class Meta:
        
        # Model name values:
        verbose_name = 'Host'
        verbose_name_plural = 'Hosts'

    # Relations with other classes:
    site = models.ForeignKey(
        Site,
        verbose_name='Site',
        help_text='Site.',
        on_delete=models.PROTECT,
        null=True,
        blank=True,
    )
    
    platform = models.ForeignKey(
        Platform,
        verbose_name='Platform',
        help_text='Platform.',
        on_delete=models.PROTECT,
        null=True,
        blank=True,
    )
    
    credential = models.ForeignKey(
        Credential,
        verbose_name='Credentials',
        help_text='Credentials.',
        on_delete=models.PROTECT,
        null=True,
        blank=True,
    )

    # Base host information:
    hostname = models.CharField(
        verbose_name='Hostname',
        help_text='Xxx.',
        max_length=128,
        null=True,
        blank=True,
    )

    # Default settings:
    default_certificate_check = models.BooleanField(
        verbose_name='Default certificate check',
        help_text='If enabled, attempts to validate host certificate. '\
        'If disabled, ignores certificate validation process.',
        default=False,
    )

    default_http_header = models.JSONField(
        verbose_name='Default HTTP heder',
        help_text='Xxx.',
        null=True,
        blank=True,
    )

    default_http_params = models.JSONField(
        verbose_name='Default HTTP parameters',
        help_text='Xxx.',
        null=True,
        blank=True,
    )
