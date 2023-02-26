# Django import:
from django.db import models

# Base models import:
from autocli2.base.models.identification import IdentificationModel
from autocli2.base.models.data_time import DataTimeModel
from autocli2.base.models.status import StatusModel

# Relations models import:
from .api_setting import ApiSetting


# Platform model class:
class Platform(StatusModel, DataTimeModel, IdentificationModel):

    class Meta:
        
        # Model name values:
        verbose_name = 'Platform'
        verbose_name_plural = 'Platforms'

    # Relations with other classes:
    api_setting = models.ForeignKey(
        ApiSetting,
        verbose_name='API setting',
        help_text='API setting.',
        on_delete=models.PROTECT,
        null=True,
        blank=True,
    )