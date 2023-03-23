# Django - model import:
from django.db import models

# AutoCli2 - base model import:
from autocli2.base.models.identification import IdentificationModel


# Model group template models class:
class ModelGroupTemplate(IdentificationModel):

    class Meta:
        
        # Model name values:
        verbose_name = 'Model group template'
        verbose_name_plural = 'Model group templates'
