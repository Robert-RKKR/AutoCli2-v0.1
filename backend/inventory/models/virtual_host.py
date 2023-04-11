# Django - models import:
from django.db import models

# Django - translation model import:
from django.utils.translation import gettext_lazy as _

# AutoCli2 - base model import:
from autocli2.base.models.identification import IdentificationModel

# AutoCli2 - inventory model import:
from inventory.models.host import Host

# AutoCli2 - host manager import:
from inventory.managers.host import HostManager


# Virtual host model class:
class VirtualHost(IdentificationModel):

    class Meta:
        
        # Model name values:
        verbose_name = _('Virtual host')
        verbose_name_plural = _('Virtual hosts')

    # Model objects manager:
    objects = HostManager()

    # Relations with other classes:
    host = models.ForeignKey(
        Host,
        verbose_name=_('Host'),
        help_text=_('Host associated with current virtual host.'),
        on_delete=models.PROTECT,
        null=True,
        blank=True,
    )

    # Base host information:
    virtual_host_name = models.CharField(
        verbose_name=_('Virtual host name'),
        help_text=_('Virtual host name refers to the name of the '\
            'virtual device in the case of virtual technology '\
            'such as Cisco VRF or FortiNet Vdoom.'),
        max_length=128,
        unique=True,
    )
