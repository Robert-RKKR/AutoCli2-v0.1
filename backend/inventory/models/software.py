# Django import:
from django.db import models

# Base models import:
from autocli2.base.models.identification import IdentificationModel
from autocli2.base.models.data_time import DataTimeModel
from autocli2.base.models.status import StatusModel

# Relations models import:
from .platform import Platform


# Software model class:
class Software(StatusModel, DataTimeModel, IdentificationModel):

    class Meta:
        
        # Model name values:
        verbose_name = 'Software'
        verbose_name_plural = 'Softwares'

    # Relations with other classes:
    platform = models.ForeignKey(
        Platform,
        verbose_name='Platform',
        help_text='Platform.',
        on_delete=models.PROTECT,
        null=True,
        blank=True,
    )
