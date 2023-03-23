# Django - models import:
from django.db import models

# AutoCli2 - base models import:
from autocli2.base.models.base_model import BaseModel

# AutoCli2 - constance import:
from autocli2.base.constants.color import COLOR_BLUE
from autocli2.base.constants.color import COLORS


# Tag model class:
class Tag(BaseModel):

    class Meta:
        
        # Model name values:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'

    # Related color:
    color = models.CharField(
        verbose_name='Color',
        help_text='Tag related color.',
        max_length=6,
        default=COLOR_BLUE,
        choices=COLORS,
    )