# Django import:
from django.db import models

# Base model import:
from .base_model import BaseModel

# Validators Import:
from ..validators.base_validator import DescriptionValueValidator
from ..validators.base_validator import NameValueValidator


# Base models class:
class IdentificationModel(BaseModel):

    class Meta:

        # Abstract class value:
        abstract = True

        # Default ordering:
        ordering = ['name']

    # Model validators:
    name_validator = NameValueValidator()
    description_validator = DescriptionValueValidator()

    # Identification values:
    name = models.CharField(
        verbose_name='Name',
        help_text='Object name.',
        max_length=64,
        unique=True,
        validators=[name_validator],
        error_messages={
            'null': 'Name field is mandatory.',
            'blank': 'Name field is mandatory.',
            'unique': 'Object with this name already exists.',
            'invalid': 'Enter the correct name value. It must contain 3 to 64 digits, letters or special characters -, _ or spaces.',
        },
    )
    slug = models.CharField(
        verbose_name='Slug',
        help_text='Object name representation (Slug).',
        max_length=64,
        unique=True,
    )
    description = models.CharField(
        verbose_name='Description',
        help_text='Object description.',
        max_length=256,
        default='Object default description.',
        validators=[description_validator],
        error_messages={
            'invalid': 'Enter the correct description value. It must contain 8 to 256 digits, letters and special characters -, _, . or spaces.',
        },
        null=True,
        blank=True,
    )
    ico = models.IntegerField(
        verbose_name='Object ico',
        help_text='Object graphical representation.',
        default=1,
    )

    # Object representation:
    def __repr__(self) -> str:
        return f'{self.pk}: {self.name}'

    def __str__(self) -> str:
        return  f'{self.pk}: {self.name}'

    # Natural key representation:
    def natural_key(self):
        return str(self.name)
