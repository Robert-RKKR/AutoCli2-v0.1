# Django - models import:
from django.db import models

# AutoCli2 - base model import:
from autocli2.base.models.administrator import AdministratorModel

# AutoCli2 - inventory model import:
from inventory.models.credentials import Credential


# Administrator setting model class:
class AdministratorSetting(AdministratorModel):

    class Meta:
        
        # Model name values:
        verbose_name = 'Administrator setting'
        verbose_name_plural = 'Administrator settings'

    # Relations with other classes:
    default_credentials = models.ForeignKey(
        Credential,
        verbose_name='Default SSH credentials',
        help_text='The following credentials will be used '\
        'by default when connecting via SSH / HTTP.',
        on_delete=models.PROTECT,
    )
