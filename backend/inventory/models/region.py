# Django - models import:
from django.db import models

# Django - translation model import:
from django.utils.translation import gettext_lazy as _

# AutoCli2 - base model import:
from autocli2.base.models.identification import IdentificationModel
from autocli2.base.models.tag import Tag

# AutoCli2 - validator Import:
from inventory.validators.inventory_validator import CodeValueValidator


# Region model class:
class Region(IdentificationModel, Tag):

    class Meta:
        
        # Model name values:
        verbose_name = _('Region')
        verbose_name_plural = _('Regions')

    # Model validators:
    code_validator = CodeValueValidator()

    # Region details:
    code = models.CharField(
        verbose_name=_('Region code'),
        help_text=_('Region code (Must contain 2 to 8 letters).'),
        max_length=8,
        validators=[code_validator],
        null=True,
        blank=True,
    )
