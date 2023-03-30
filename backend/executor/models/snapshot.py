# Django - models import:
from django.db import models

# Django - translation model import:
from django.utils.translation import gettext_lazy as _

# AutoCli2 - base models import:
from autocli2.base.models.identification import IdentificationModel
from autocli2.base.models.administrator import AdministratorModel


# Snapshot model class:
class Snapshot(IdentificationModel, AdministratorModel):

    class Meta:
        
        # Model name values:
        verbose_name = _('Snapshot')
        verbose_name_plural = _('Snapshots')
