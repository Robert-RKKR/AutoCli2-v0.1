# Django Import:
from django.db import models

# Base model import:
from autocli2.base.models.data_time import DataTimeModel
from autocli2.base.models.status import StatusModel


# Base models class:
class ConnectionSshTemplate(StatusModel, DataTimeModel):

    class Meta:
        
        # Model name values:
        verbose_name = 'SSH connection template'
        verbose_name_plural = 'SSH connection templates'

    template = models.TextField(
        verbose_name='Template',
        help_text='Xxx.',
    )

    sfm_expression = models.TextField(
        verbose_name='SFM expression',
        help_text='Xxx.',
    )

    regex_expression = models.TextField(
        verbose_name='Regex expression',
        help_text='Xxx.',
    )
