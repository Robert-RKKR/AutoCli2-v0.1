# Django import:
from django.db import models

# Base models import:
from autocli2.base.models.data_time import DataTimeModel

# Relations models import:
from connector.models.data_template import DataTemplate
from inventory.models.host import Host
from .snapshoot  import Snapshoot
from .execution import Host


# Converted data model class:
class ConvertedData(DataTimeModel):

    class Meta:
        
        # Model name values:
        verbose_name = 'Converted data'
        verbose_name_plural = 'Converted data'

    # Relations with other classes:
    snapshoot = models.ForeignKey(
        Snapshoot,
        verbose_name='Xxx',
        help_text='Xxx.',
        on_delete=models.PROTECT,
    )

    data_template = models.ForeignKey(
        DataTemplate,
        verbose_name='Xxx',
        help_text='Xxx.',
        on_delete=models.PROTECT,
    )

    execution = models.ForeignKey(
        Execution,
        verbose_name='Xxx',
        help_text='Xxx.',
        on_delete=models.PROTECT,
    )

    host = models.ForeignKey(
        Host,
        verbose_name='Xxx',
        help_text='Xxx.',
        on_delete=models.PROTECT,
    )
