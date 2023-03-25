# Django - models import:
from django.db import models

# AutoCli2 - base model import:
from autocli2.base.models.identification import IdentificationModel

# AutoCli2 - inventory model import:
from inventory.models.credentials import Credential
from inventory.models.platform import Platform
from inventory.models.site import Site

# AutoCli2 - constance import:
from autocli2.base.constants.execution_protocol import ExecutionProtocolChoices


# Host model class:
class Host(IdentificationModel):

    class Meta:
        
        # Model name values:
        verbose_name = 'Host'
        verbose_name_plural = 'Hosts'

    # Relations with other classes:
    site = models.ForeignKey(
        Site,
        verbose_name='Site',
        help_text='Site associated with current host.',
        on_delete=models.PROTECT,
        null=True,
        blank=True,
    )
    platform = models.ForeignKey(
        Platform,
        verbose_name='Platform',
        help_text='Platform associated with current host.',
        on_delete=models.PROTECT,
        default=1,
    )
    credential = models.ForeignKey(
        Credential,
        verbose_name='Credentials',
        help_text='Credentials associated with current host.',
        on_delete=models.PROTECT,
        default=1,
    )

    # Base host information:
    hostname = models.CharField(
        verbose_name='Hostname',
        help_text='Valid IP address or domain name used to establish '\
            'the SSH / HTTP(S) connections.',
        max_length=128,
        unique=True,
    )
    data_collection_protocol = models.IntegerField(
        verbose_name='Data collection protocol',
        help_text='The network protocol that will be used to execute '\
            'connection template (SSH / HTTP(S)).',
        choices=ExecutionProtocolChoices.choices,
        default=1,
    )
    ssh_port = models.IntegerField(
        verbose_name='SSH port',
        help_text='The TCP port that will be used during the SSH sessions.',
        default=22
    )
    http_port = models.IntegerField(
        verbose_name='HTTP/S port',
        help_text='The TCP port that will be used during the HTTP(S) sessions.',
        default=443
    )

    # Default settings:
    certificate_check = models.BooleanField(
        verbose_name='Certificate check',
        help_text='If enabled, attempts to validate host certificate. '\
            'If disabled, ignores certificate validation process.',
        default=True,
    )
