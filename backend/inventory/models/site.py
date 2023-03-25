# Django - models import:
from django.db import models

# AutoCli2 - base model import:
from autocli2.base.models.identification import IdentificationModel
from autocli2.base.models.tag import Tag

# AutoCli2 - inventory model import:
from inventory.models.region import Region

# AutoCli2 - validator Import:
from inventory.validators.inventory_validator import CodeValueValidator


# Site model class:
class Site(IdentificationModel, Tag):

    class Meta:
        
        # Model name values:
        verbose_name = 'Site'
        verbose_name_plural = 'Sites'

    # Model validators:
    code_validator = CodeValueValidator()


    # Relations with other classes:
    region = models.ForeignKey(
        Region,
        verbose_name='Region',
        help_text='Region associated with current site.',
        on_delete=models.PROTECT,
        null=True,
        blank=True,
    )

    # Site details:
    code = models.CharField(
        verbose_name='Site code',
        help_text='Site code (Must contain 2 to 8 letters).',
        max_length=8,
        validators=[code_validator],
        null=True,
        blank=True,
    )

    # Base site information:
    gps_coordinates = models.CharField(
        verbose_name='GPS coordinates',
        help_text='GPS coordinates.',
        max_length=128,
        null=True,
        blank=True,
    )

    physical_address = models.CharField(
        verbose_name='Physical address',
        help_text='Physical address.',
        max_length=128,
        null=True,
        blank=True,
    )
