# Django Import:
from django.db import models

# Base model import:
from autocli2.base.models.identification import IdentificationModel
from autocli2.base.models.data_time import DataTimeModel
from autocli2.base.models.status import StatusModel

# Relations models import:
from .model_group_template import ModelGroupTemplate


# Base models class:
class ModelTemplate(StatusModel, DataTimeModel, IdentificationModel):

    class Meta:
        
        # Model name values:
        verbose_name = 'Model template'
        verbose_name_plural = 'Model templates'

    # Relations with other classes:
    model_group_template = models.ForeignKey(
        ModelGroupTemplate,
        verbose_name='Model group template',
        help_text='Model group template.',
        on_delete=models.PROTECT,
        null=True,
        blank=True,
    )
