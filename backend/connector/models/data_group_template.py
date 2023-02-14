# Django import:
from django.db import models

# Base models import:
from autocli2.base.models.data_time import DataTimeModel
from autocli2.base.models.status import StatusModel

# Relations models import:
from .model_group_template import ModelGroupTemplate
from .connection_template import ConnectionTemplate



# Data group template models class:
class DataGroupTemplate(StatusModel, DataTimeModel):

    class Meta:
        
        # Model name values:
        verbose_name = 'Data group template'
        verbose_name_plural = 'Data group templates'

    # Relations with other classes:
    model_group_template = models.ForeignKey(
        ModelGroupTemplate,
        verbose_name='Model group template',
        help_text='Model group template.',
        on_delete=models.PROTECT,
        null=True,
        blank=True,
    )

    connection_template  = models.ForeignKey(
        ConnectionTemplate,
        verbose_name='Connection template',
        help_text='Connection template.',
        on_delete=models.PROTECT,
        null=True,
        blank=True,
    )

    # platform  = models.ForeignKey(
    #     Platform,
    #     verbose_name='Platform',
    #     help_text='Platform.',
    #     on_delete=models.PROTECT,
    #     null=True,
    #     blank=True,
    # )

    # Data group specific fields:
    keys = models.JSONField(
        verbose_name='Keys',
        help_text='Xxx.',
        null=True,
        blank=True,
    )

    keys_regex = models.CharField(
        verbose_name='Xxx',
        help_text='Xxx.',
        max_length=128,
        null=True,
        blank=True,
    )
