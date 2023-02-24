# Django import:
from django.db import models

# Base models import:
from autocli2.base.models.identification import IdentificationModel
from autocli2.base.models.data_time import DataTimeModel
from autocli2.base.models.status import StatusModel

# Relations models import:
from .credentials import Credential
from .software import Software
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
    
    software = models.ForeignKey(
        Software,
        verbose_name='Software',
        help_text='Software.',
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
    )

    # Default settings:
    certificate_check = models.BooleanField(
        verbose_name='Certificate check',
        help_text='If enabled, attempts to validate host certificate. '\
        'If disabled, ignores certificate validation process.',
        default=False,
    )
