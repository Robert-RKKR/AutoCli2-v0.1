# Django import:
from django.db import models

# Base models import:
from autocli2.base.models.identification import IdentificationModel
from autocli2.base.models.administrator import AdministratorModel
from autocli2.base.models.data_time import DataTimeModel
from autocli2.base.models.status import StatusModel


# Credential model class:
class Credential(StatusModel, DataTimeModel, IdentificationModel, AdministratorModel):

    class Meta:
        
        # Model name values:
        verbose_name = 'Credential'
        verbose_name_plural = 'Credentials'

    # Global credential settings:
    is_global = models.BooleanField(
        verbose_name='Xxxx',
        help_text='Xxx.',
        default=False,
    )

    # Credential information:
    username = models.CharField(
        verbose_name='Username',
        help_text='Xxx.',
        max_length=128,
        null=True,
        blank=True,
    )

    password = models.CharField(
        verbose_name='Password',
        help_text='Xxx.',
        max_length=128,
        null=True,
        blank=True,
    )

    token = models.CharField(
        verbose_name='Token',
        help_text='Xxx.',
        max_length=128,
        null=True,
        blank=True,
    )
