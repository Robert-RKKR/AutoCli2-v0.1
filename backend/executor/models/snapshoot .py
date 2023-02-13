# Django import:
from django.db import models

# Base models import:
from autocli2.base.models.administrator import AdministratorModel
from autocli2.base.models.data_time import DataTimeModel


# Snapshoot model class:
class Snapshoot(DataTimeModel, AdministratorModel):

    class Meta:
        
        # Model name values:
        verbose_name = 'Snapshoot'
        verbose_name_plural = 'Snapshoots'
