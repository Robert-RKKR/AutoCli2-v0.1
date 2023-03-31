# Django - models import:
from django.db import models

# Django - translation model import:
from django.utils.translation import gettext_lazy as _

# AutoCli2 - base model import:
from autocli2.base.models.identification import IdentificationModel

# AutoCli2 - constance import:
from autocli2.base.constants.severity import SeverityChoices


# Global setting model class:
class GlobalSettings(IdentificationModel):

    class Meta:
        
        # Model name values:
        verbose_name = _('Global settings')
        verbose_name_plural = _('Global settings')

    # Current global settings:
    is_current = models.BooleanField(
        verbose_name=_('Current global settings'),
        help_text=_('Active settings template used by the AutoCli 2 application'),
        default=True,
    )

    # Global settings:
    notification_level = models.IntegerField(
        verbose_name=_('Notification severity level'),
        help_text=_('The level of severity of the performed action.'),
        choices=SeverityChoices.choices,
        default=4,
    )
    logger_level = models.IntegerField(
        verbose_name=_('Logger severity level'),
        help_text=_('The level of severity of the performed action.'),
        choices=SeverityChoices.choices,
        default=1,
    )

    # Connection settings:
    default_user = models.CharField(
        verbose_name=_('Default username'),
        help_text=_('Default username used to connect to hosts.'),
        max_length=128,
        default='admin',
    )
    default_password = models.CharField(
        verbose_name=_('Default password'),
        help_text=_('Default password used to connect to hosts.'),
        max_length=128,
        default='!Cisco@12345',
    )
    http_timeout = models.IntegerField(
        verbose_name=_('HTTP session timeout'),
        help_text=_('The HTTP(S) timeout refers to the time that an AutoCli '\
            '2 application waits for a response to an HTTP(S) request '\
            'before closing the connection.'),
        default=10,
    )
    ssh_timeout = models.IntegerField(
        verbose_name=_('SSH session timeout'),
        help_text=_('The SSH timeout refers to the time that an AutoCli '\
            '2 application waits for a response to an SSH request before '\
            'closing the connection.'),
        default=10,
    )
