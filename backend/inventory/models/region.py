# Django import:
from django.db import models

# Base models import:
from autocli2.base.models.identification import IdentificationModel
from autocli2.base.models.data_time import DataTimeModel
from autocli2.base.models.status import StatusModel

# Relations models import:
from .connection_ssh_template import ConnectionSshTemplate
from .connection_group import ConnectionGroup


# Region model class:
class Region(StatusModel, DataTimeModel, IdentificationModel):

    class Meta:
        
        # Model name values:
        verbose_name = 'Region'
        verbose_name_plural = 'Regions'
