# Django - models import:
from django.db import models

# AutoCli2 - base models import:
from autocli2.base.models.identification import IdentificationModel
from autocli2.base.models.administrator import AdministratorModel
from autocli2.base.models.data_time import DataTimeModel
from autocli2.base.models.status import StatusModel

# AutoCli2 - inventory model import:
from inventory.models.credentials import Credential
from inventory.models.host import Host


# Snapshot model class:
class Snapshot(StatusModel, DataTimeModel, IdentificationModel, AdministratorModel):

    class Meta:
        
        # Model name values:
        verbose_name = 'Snapshot'
        verbose_name_plural = 'Snapshots'

    host = models.ForeignKey(
        Host,
        verbose_name='Hosts',
        help_text='Xxx.',
        on_delete=models.PROTECT,
    )