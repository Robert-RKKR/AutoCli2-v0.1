# Django - models import:
from django.db import models

# Django - translation model import:
from django.utils.translation import gettext_lazy as _

# AutoCli2 - constance import:
from autocli2.base.constants.color import ColorChoices

# AutoCli2 - base models import:
from autocli2.base.models.identification import IdentificationModel


# Site model class:
class Tag(IdentificationModel):

    class Meta:
        
        # Model name values:
        verbose_name = _('Tag')
        verbose_name_plural = _('Tags')

    # Tag color:
    color = models.CharField(
        verbose_name=_('Color'),
        help_text=_('Tag related color.'),
        max_length=6,
        choices=ColorChoices.choices,
        default=ColorChoices.BLUE,
    )
