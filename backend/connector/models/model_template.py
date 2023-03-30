# Django - model import:
from django.db import models

# Django - translation model import:
from django.utils.translation import gettext_lazy as _

# AutoCli2 - base model import:
from autocli2.base.models.identification import IdentificationModel

# AutoCli2 - connector model import:
from connector.models.model_group_template import ModelGroupTemplate


# Model template models class:
class ModelTemplate(IdentificationModel):

    class Meta:
        
        # Model name values:
        verbose_name = _('Model template')
        verbose_name_plural = _('Model templates')

    # Relations with other classes:
    model_group_template = models.ForeignKey(
        ModelGroupTemplate,
        verbose_name=_('Model group template'),
        help_text=_('Model group template.'),
        on_delete=models.PROTECT,
        null=True,
        blank=True,
    )
