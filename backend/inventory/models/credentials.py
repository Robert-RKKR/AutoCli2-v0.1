# Django - models import:
from django.db import models

# Django - translation model import:
from django.utils.translation import gettext_lazy as _

# AutoCli2 - base models import:
from autocli2.base.models.identification import IdentificationModel
from autocli2.base.models.administrator import AdministratorModel
from autocli2.base.models.tag import Tag


# Credential model class:
class Credential(IdentificationModel, AdministratorModel, Tag):

    class Meta:
        
        # Model name values:
        verbose_name = _('Credential')
        verbose_name_plural = _('Credentials')

    # Global credential settings:
    is_global = models.BooleanField(
        verbose_name=_('Global credentials'),
        help_text=_('Global credentials visible to all administrators.'),
        default=False,
    )

    # Credential information:
    username = models.CharField(
        verbose_name=_('Username'),
        help_text=_('Value of the credential user name.'),
        max_length=128,
        null=True,
        blank=True,
    )
    password = models.CharField(
        verbose_name=_('Password'),
        help_text=_('Value of the credential password (If both Password and '\
            'Token are specified, the Token will be used to authenticate '\
            'HTTP requests).'),
        max_length=128,
        null=True,
        blank=True,
    )
    token = models.CharField(
        verbose_name=_('Token'),
        help_text=_('Value of the credential token (If both Password and Token '\
            'are specified, the Token will be used to authenticate HTTP '\
            'requests).'),
        max_length=128,
        null=True,
        blank=True,
    )
