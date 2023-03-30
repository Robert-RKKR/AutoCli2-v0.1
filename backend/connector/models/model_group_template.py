# Django - model import:
from django.db import models

# Django - translation model import:
from django.utils.translation import gettext_lazy as _

# AutoCli2 - base model import:
from autocli2.base.models.identification import IdentificationModel


# Model group template models class:
class ModelGroupTemplate(IdentificationModel):

    class Meta:
        
        # Model name values:
        verbose_name = _('Model group template')
        verbose_name_plural = _('Model group templates')
