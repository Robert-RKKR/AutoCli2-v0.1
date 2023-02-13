# Django import:
from django.db import models

# Base models import:
from autocli2.base.models.identification import IdentificationModel
from autocli2.base.models.data_time import DataTimeModel


# Global setting model class:
class GlobalSetting(DataTimeModel, IdentificationModel):

    class Meta:
        
        # Model name values:
        verbose_name = 'Global setting'
        verbose_name_plural = 'Global settings'
