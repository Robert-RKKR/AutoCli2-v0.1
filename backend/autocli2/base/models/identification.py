# Django - models import:
from django.db import models

# AutoCli2 - base models import:
from autocli2.base.models.base_model import BaseModel

# AutoCli2 - validators Import:
from autocli2.base.validators.base_validator import DescriptionValueValidator
from autocli2.base.validators.base_validator import NameValueValidator


# Identification models class:
class IdentificationModel(BaseModel):

    class Meta:
        
        # Model name values:
        verbose_name = 'IdentificationModel'
        verbose_name_plural = 'IdentificationModels'

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
        help_text=f'{Meta.verbose_name} name.',
        max_length=64,
        unique=True,
        validators=[name_validator],
        error_messages={
            'null': 'Name field is mandatory.',
            'blank': 'Name field is mandatory.',
            'unique': f'{Meta.verbose_name} with this name already exists.',
            'invalid': 'Enter the correct name value. It must contain 3 to 64 digits, letters or special characters -, _ or spaces.',
        },
    )
    # slug = models.CharField(
    #     verbose_name='Slug',
    #     help_text=f'{Meta.verbose_name} name representation (Slug).',
    #     max_length=64,
    #     unique=True,
    # )
    description = models.CharField(
        verbose_name='Description',
        help_text=f'{Meta.verbose_name} description.',
        max_length=256,
        default=f'{Meta.verbose_name} default description.',
        validators=[description_validator],
        error_messages={
            'invalid': 'Enter the correct description value. It must contain 8 to 256 digits, letters and special characters -, _, . or spaces.',
        },
        null=True,
        blank=True,
    )
    ico = models.IntegerField(
        verbose_name=f'{Meta.verbose_name} ico',
        help_text=f'{Meta.verbose_name} graphical representation.',
        default=1,
    )

    # object representation:
    def __repr__(self) -> str:
        return f'{self.pk}: {self.name}'

    def __str__(self) -> str:
        return  f'{self.pk}: {self.name}'

    # Natural key representation:
    def natural_key(self):
        return str(self.name)
