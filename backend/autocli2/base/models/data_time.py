# Django import:
from django.db import models

# Base model import:
from .base_model import BaseModel


# Data time models class:
class DataTimeModel(BaseModel):

    class Meta:
        
        # Model name values:
        verbose_name = 'DataTimeModel'
        verbose_name_plural = 'DataTimeModels'

        # Abstract class value:
        abstract = True

    # Model data time information:
    created = models.DateTimeField(
        verbose_name='Created',
        help_text=f'{Meta.verbose_name} create date.',
        auto_now_add=True,
    )
    updated = models.DateTimeField(
        verbose_name='Updated',
        help_text=f'{Meta.verbose_name} last update date.',
        auto_now=True,
    )
