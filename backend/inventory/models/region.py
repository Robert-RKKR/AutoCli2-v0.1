# Django - models import:
from django.db import models

# AutoCli2 - base models import:
from autocli2.base.models.identification import IdentificationModel
from autocli2.base.models.data_time import DataTimeModel
from autocli2.base.models.status import StatusModel

# AutoCli2 - validator Import:
from inventory.validators.inventory_validator import CodeValueValidator


# Region model class:
class Region(StatusModel, DataTimeModel, IdentificationModel):

    class Meta:
        
        # Model name values:
        verbose_name = 'Region'
        verbose_name_plural = 'Regions'

    # Model validators:
    code_validator = CodeValueValidator()

    # Region details:
    code = models.CharField(
        verbose_name='Region code',
        help_text='Region code (Must contain 2 to 8 letters).',
        max_length=8,
        validators=[code_validator],
        null=True,
        blank=True,
    )
