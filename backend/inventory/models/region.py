# Django - models import:
from django.db import models

# AutoCli2 - base models import:
from autocli2.base.models.identification import IdentificationModel
from autocli2.base.models.data_time import DataTimeModel
from autocli2.base.models.status import StatusModel


# Region model class:
class Region(StatusModel, DataTimeModel, IdentificationModel):

    class Meta:
        
        # Model name values:
        verbose_name = 'Region'
        verbose_name_plural = 'Regions'

    # Region details:
    code = models.CharField(
        verbose_name='Region code',
        help_text='Xxx.',
        max_length=32,
        null=True,
        blank=True,
    )
