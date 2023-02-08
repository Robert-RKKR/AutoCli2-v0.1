# Django import:
from django.db import models

# Base models import:
from autocli2.base.models.identification import IdentificationModel
from autocli2.base.models.data_time import DataTimeModel
from autocli2.base.models.status import StatusModel

# Relations models import:
from .region import Region


# Site model class:
class Site(StatusModel, DataTimeModel, IdentificationModel):

    class Meta:
        
        # Model name values:
        verbose_name = 'Site'
        verbose_name_plural = 'Sites'

    # Relations with other classes:
    region = models.ForeignKey(
        Region,
        verbose_name='Region',
        help_text='Region.',
        on_delete=models.PROTECT,
        null=True,
        blank=True,
    )

    # Base site information:
    gps_coordinates = models.CharField(
        verbose_name='GPS coordinates',
        help_text='Xxx.',
        max_length=128,
        null=True,
        blank=True,
    )

    physical_address = models.CharField(
        verbose_name='Physical address',
        help_text='Xxx.',
        max_length=128,
        null=True,
        blank=True,
    )
