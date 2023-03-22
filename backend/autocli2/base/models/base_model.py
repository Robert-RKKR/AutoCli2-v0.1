# Django - models import:
from django.db import models

# AutoCli2 - base models import:
from autocli2.base.managers.base_manager import BaseManager


# Base models class:
class BaseModel(models.Model):

    class Meta:
        
        # Model name values:
        verbose_name = 'Base model'
        verbose_name_plural = 'Base models'

        # Abstract class value:
        abstract = True

    # Model objects manager:
    objects = BaseManager()

    # Delete status:
    is_deleted = models.BooleanField(
        verbose_name='Deleted',
        help_text=f'Is {Meta.verbose_name} object deleted.',
        default=False,
    )

    # object representation:
    def __repr__(self) -> str:
        return f'PK: {self.pk}'

    def __str__(self) -> str:
        return  f'PK: {self.pk}'

    # Natural key representation:
    def natural_key(self):
        return f'PK: {self.pk}'
