# Django import:
from django.db import models

# Base models import:
from autocli2.base.models.identification import IdentificationModel
from autocli2.base.models.administrator import AdministratorModel
from autocli2.base.models.data_time import DataTimeModel

# Relations models import:
from inventory.models.credentials import Credential


# Administrator setting model class:
class AdministratorSetting(DataTimeModel, AdministratorModel):

    class Meta:
        
        # Model name values:
        verbose_name = 'Administrator setting'
        verbose_name_plural = 'Administrator settings'

    # Relations with other classes:
    default_ssh_credentials = models.ForeignKey(
        Credential,
        verbose_name='Default SSH credentials',
        help_text='The following credentials will be used '\
        'by default when connecting via SSH.',
        on_delete=models.PROTECT,
    )

    
    default_http_credentials = models.ForeignKey(
        Credential,
        verbose_name='Default HTTP credentials',
        help_text='The following credentials will be used '\
        'by default when connecting via HTTP.',
        on_delete=models.PROTECT,
    )
