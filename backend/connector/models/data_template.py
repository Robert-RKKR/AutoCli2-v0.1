# Django - model import:
from django.db import models

# AutoCli2 - base models import:
from autocli2.base.models.data_time import DataTimeModel
from autocli2.base.models.status import StatusModel

# AutoCli2 - connector model import:
from connector.models.data_group_template import DataGroupTemplate
from connector.models.model_template import ModelTemplate


# Data template models class:
class DataTemplate(StatusModel, DataTimeModel):

    class Meta:
        
        # Model name values:
        verbose_name = 'Data template'
        verbose_name_plural = 'Data templates'

    # Relations with other classes:
    data_group_template = models.ForeignKey(
        DataGroupTemplate,
        verbose_name='Data group template',
        help_text='Data group template.',
        on_delete=models.PROTECT,
        null=True,
        blank=True,
    )

    model_template = models.ForeignKey(
        ModelTemplate,
        verbose_name='Model template',
        help_text='Model template.',
        on_delete=models.PROTECT,
        null=True,
        blank=True,
    )

    # Data path:
    path = models.JSONField(
        verbose_name='Path',
        help_text='Xxx.',
        null=True,
        blank=True,
    )
