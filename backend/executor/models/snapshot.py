# Django - models import:
from django.db import models

# AutoCli2 - base models import:
from autocli2.base.models.identification import IdentificationModel
from autocli2.base.models.administrator import AdministratorModel


# Snapshot model class:
class Snapshot(IdentificationModel, AdministratorModel):

    class Meta:
        
        # Model name values:
        verbose_name = 'Snapshot'
        verbose_name_plural = 'Snapshots'
