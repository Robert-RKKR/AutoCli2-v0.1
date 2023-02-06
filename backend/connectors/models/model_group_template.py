# Django Import:
from django.db import models

# Base model import:
from autocli2.base.models.identification import IdentificationModel
from autocli2.base.models.data_time import DataTimeModel
from autocli2.base.models.status import StatusModel


# Base models class:
class ModelGroupTemplate(StatusModel, DataTimeModel, IdentificationModel):

    class Meta:
        
        # Model name values:
        verbose_name = 'Model group template'
        verbose_name_plural = 'Model group templates'
