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

# Connections template model constants:
EXECUTION_PROTOCOLS = (
    (1, 'SSH'),
    (2, 'HTTP')
)


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
    data_collection_protocol = models.IntegerField(
        verbose_name='Data collection protocol',
        help_text='The network protocol that will be used to execute '\
        'connection template (SSH / HTTP(S)).',
        choices=EXECUTION_PROTOCOLS,
        default=1,
    )
    ssh_port = models.IntegerField(
        verbose_name='SSH port',
        help_text='Xxx.',
        default=22
    )
    http_port = models.IntegerField(
        verbose_name='HTTP/S port',
        help_text='Xxx.',
        default=443
    )

    # Default settings:
    certificate_check = models.BooleanField(
        verbose_name='Certificate check',
        help_text='If enabled, attempts to validate host certificate. '\
        'If disabled, ignores certificate validation process.',
        default=False,
    )
