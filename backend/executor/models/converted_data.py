# Django - models import:
from django.db import models

# AutoCli2 - base models import:
from autocli2.base.models.data_time import DataTimeModel

# AutoCli2 - connector model import:
from connector.models.data_template import DataTemplate

# AutoCli2 - executor model import:
from executor.models.execution import Execution
from executor.models.snapshot  import Snapshot


# Converted data model class:
class ConvertedData(DataTimeModel):

    class Meta:
        
        # Model name values:
        verbose_name = 'Converted data'
        verbose_name_plural = 'Converted data'

    # Relations with other classes:
    snapshot = models.ForeignKey(
        Snapshot,
        verbose_name='Snapshot',
        help_text='Xxx.',
        on_delete=models.PROTECT,
        null=True,
        blank=True,
    )
    execution = models.ForeignKey(
        Execution,
        verbose_name='Execution',
        help_text='Xxx.',
        on_delete=models.PROTECT,
    )
    data_template = models.ForeignKey(
        DataTemplate,
        verbose_name='Data template',
        help_text='Xxx.',
        on_delete=models.PROTECT,
    )

    # Collected data:
    value = models.CharField(
        verbose_name='Value',
        help_text='Xxx.',
        max_length=128,
        null=True,
        blank=True,
    )
    json_value = models.JSONField(
        verbose_name='JSON value',
        help_text='Xxx.',
        null=True,
        blank=True,
    )
