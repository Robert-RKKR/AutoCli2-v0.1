# Django - models import:
from django.db import models

# AutoCli2 - base model import:
from autocli2.base.models.identification import IdentificationModel

# AutoCli2 - constance import:
from autocli2.base.constants.severity import SeverityChoices


# Global setting model class:
class GlobalSetting(IdentificationModel):

    class Meta:
        
        # Model name values:
        verbose_name = 'Global setting'
        verbose_name_plural = 'Global settings'

    # Current global settings:
    is_current = models.BooleanField(
        verbose_name='Current global settings',
        help_text='Active settings template used by the AutoCli 2 application',
        default=True,
    )

    # Global settings:
    notification_level = models.IntegerField(
        verbose_name='Notification severity level',
        help_text='The level of severity of the performed action.',
        choices=SeverityChoices.choices,
        default=4,
    )
    logger_level = models.IntegerField(
        verbose_name='Logger severity level',
        help_text='The level of severity of the performed action.',
        choices=SeverityChoices.choices,
        default=1,
    )

    # Connection settings:
    default_user = models.CharField(
        verbose_name='Default username',
        help_text='Default username used to connect to hosts.',
        max_length=128,
        default='admin',
    )
    default_password = models.CharField(
        verbose_name='Default password',
        help_text='Default password used to connect to hosts.',
        max_length=128,
        default='!Cisco@12345',
    )
    http_timeout = models.IntegerField(
        verbose_name='HTTP session timeout',
        help_text='The HTTP(S) timeout refers to the time that an AutoCli '\
            '2 application waits for a response to an HTTP(S) request '\
            'before closing the connection.',
        default=10,
    )
    ssh_timeout = models.IntegerField(
        verbose_name='SSH session timeout',
        help_text='The SSH timeout refers to the time that an AutoCli '\
            '2 application waits for a response to an SSH request before '\
            'closing the connection.',
        default=10,
    )
