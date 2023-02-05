# Django import:
from django.db import models

# Base model import:
from .base_model import BaseModel


# Base models class:
class DataTimeModel(BaseModel):

    class Meta:

        # Abstract class value:
        abstract = True

    # Model data time information:
    created = models.DateTimeField(
        verbose_name='Created',
        help_text='Object create date.',
        auto_now_add=True,
    )
    updated = models.DateTimeField(
        verbose_name='Updated',
        help_text='object last update date.',
        auto_now=True,
    )

    # Object representation:
    def __repr__(self) -> str:
        return f'{self.pk}: {self.created}'

    def __str__(self) -> str:
        return  f'{self.pk}: {self.created}'

    # Natural key representation:
    def natural_key(self):
        return str(self.created)
