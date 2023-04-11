# Django - models import:
from django.db import models

# Django - translation model import:
from django.utils.translation import gettext_lazy as _

# AutoCli2 - base model import:
from autocli2.base.models.identification import IdentificationModel
from autocli2.base.models.tag import Tag

# AutoCli2 - inventory model import:
from inventory.models.credentials import Credential
from inventory.models.platform import Platform
from inventory.models.site import Site

# AutoCli2 - inventory model import:
from inventory.models.credentials import Credential

# AutoCli2 - constance import:
from autocli2.base.constants.execution_protocol import ExecutionProtocolChoices

# AutoCli2 - host manager import:
from inventory.managers.host import HostManager


# Host model class:
class Host(IdentificationModel, Tag):

    class Meta:
        
        # Model name values:
        verbose_name = _('Host')
        verbose_name_plural = _('Hosts')

    # Model objects manager:
    objects = HostManager()

    # Relations with other classes:
    site = models.ForeignKey(
        Site,
        verbose_name=_('Site'),
        help_text=_('Site associated with current host.'),
        on_delete=models.PROTECT,
        null=True,
        blank=True,
    )
    platform = models.ForeignKey(
        Platform,
        verbose_name=_('Platform'),
        help_text=_('Platform associated with current host.'),
        on_delete=models.PROTECT,
        default=1,
    )
    credential = models.ForeignKey(
        Credential,
        verbose_name=_('Credentials'),
        help_text=_('Credentials associated with current host.'),
        on_delete=models.PROTECT,
        default=1,
    )

    # Base host information:
    hostname = models.CharField(
        verbose_name=_('Hostname'),
        help_text=_('Valid IP address or domain name used to establish '\
            'the SSH / HTTP(S) connections.'),
        max_length=128,
        unique=True,
    )
    data_collection_protocol = models.IntegerField(
        verbose_name=_('Data collection protocol'),
        help_text=_('The network protocol that will be used to execute '\
            'connection template (SSH / HTTP(S)).'),
        choices=ExecutionProtocolChoices.choices,
        default=1,
    )
    ssh_port = models.IntegerField(
        verbose_name=_('SSH port'),
        help_text=_('The TCP port that will be used during the SSH sessions.'),
        default=22
    )
    http_port = models.IntegerField(
        verbose_name=_('HTTP/S port'),
        help_text=_('The TCP port that will be used during the HTTP(S) sessions.'),
        default=443
    )

    # Default settings:
    certificate_check = models.BooleanField(
        verbose_name=_('Certificate check'),
        help_text=_('If enabled, attempts to validate host certificate. '\
            'If disabled, ignores certificate validation process.'),
        default=True,
    )

    def get_all_related_templates(self):
        # AutoCli2 - connector import:
        from connector.models.connection_template import ConnectionTemplate
        # Return Connection templates:
        return ConnectionTemplate.objects.filter(
            platforms=self.platform)

    def get_ssh_related_templates(self):
        # AutoCli2 - connector import:
        from connector.models.connection_template import ConnectionTemplate
        # Return Connection templates:
        return ConnectionTemplate.objects.filter(
            platforms=self.platform,
            execution_protocol=ExecutionProtocolChoices.SSH)

    def get_http_related_templates(self):
        # AutoCli2 - connector import:
        from connector.models.connection_template import ConnectionTemplate
        # Return Connection templates:
        return ConnectionTemplate.objects.filter(
            platforms=self.platform,
            execution_protocol=ExecutionProtocolChoices.HTTP)
