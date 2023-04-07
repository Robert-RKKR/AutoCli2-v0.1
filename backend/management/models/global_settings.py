# Django - models import:
from django.db import models

# Django - translation model import:
from django.utils.translation import gettext_lazy as _

# AutoCli2 - base model import:
from autocli2.base.models.identification import IdentificationModel

# AutoCli2 - constance import:
from autocli2.base.constants.severity import SeverityChoices

# Standard constance:
INVALID_SSH_RESPONSES = [
    '% Invalid input detected',
    'syntax error, expecting',
    'Error: Unrecognized command',
    '%Error',
    'command not found',
    'Syntax Error: unexpected argument',
    '% Unrecognized command found at',
    'invalid input detected',
    'cdp is not enabled',
    'incomplete command',
    'no spanning tree instance exists',
    'lldp is not enabled',
    'snmp agent not enabled',
]


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

    # HTTP(S)
    http_timeout = models.IntegerField(
        verbose_name=_('HTTP session timeout'),
        help_text=_('The HTTP(S) timeout refers to the time that an AutoCli '\
            '2 application waits for a response to an HTTP(S) request '\
            'before closing the connection.'),
        default=10,
    )

    # SSH
    ssh_timeout = models.IntegerField(
        verbose_name=_('SSH session timeout'),
        help_text=_('The SSH timeout refers to the time that an AutoCli '\
            '2 application waits for a response to an SSH request before '\
            'closing the connection.'),
        default=10,
    )
    ssh_repeat = models.IntegerField(
        verbose_name=_('SSH repeat connection'),
        help_text=_('The SSH repeat connection refers to the number of repeats '\
            'that the application will make in case the previous one fails.'),
        default=2,
    )
    ssh_invalid_responses = models.JSONField(
        verbose_name=_('SSH invalid responses'),
        help_text=_('List of strings that contain invalid host responses. '\
            'For example, the Cisco IOS system returns output such as '\
            '"invalid input detected" in the case of an unsupported command, '\
            'or "cdp is not enabled" in the case of an disabled function, in '\
            'this example CDP.'),
        default=INVALID_SSH_RESPONSES,
    )
