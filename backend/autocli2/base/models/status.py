# Django import:
from django.db import models

# Base model import:
from .base_model import BaseModel


# Status models class:
class StatusModel(BaseModel):

    class Meta:
        
        # Model name values:
        verbose_name = 'StatusModel'
        verbose_name_plural = 'StatusModels'
        
        # Abstract class value:
        abstract = True

    # Deleted information:
    is_deleted = models.BooleanField(
        verbose_name='Deleted',
        help_text=f'Is {Meta.verbose_name} deleted (Deleted {Meta.verbose_name} '\
        'is reserved for backward compatibility).',
        default=False,
    )

    # Model status values:
    is_root = models.BooleanField(
        verbose_name='Root',
        help_text=f'Is {Meta.verbose_name} root (Root {Meta.verbose_name} '\
        'cannot be deleted or modify).',
        default=False,
    )
    is_active = models.BooleanField(
        verbose_name='Active',
        help_text=f'Is {Meta.verbose_name} active (Inactive {Meta.verbose_name} '\
        'has limited functionality).',
        default=True,
    )

    # Model Save override:
    def save(self, *args, **kwargs):
        
        # Check if object root value is true:
        if self.is_root is True:
            pass
            # raise ValidationError('Root object cannot be changed or deleted.')
        else:
            super(StatusModel, self).save(*args, **kwargs)

    # Model Save override:
    def delete(self, *args, **kwargs):
        
        # Check if object root value is true:
        if self.is_root is True:
            pass
            # raise ValidationError('Root object cannot be changed or deleted.')
        else:
            super(StatusModel, self).delete(*args, **kwargs)

    # Model Save override:
    def update(self, *args, **kwargs):
        
        # Check if object root value is true:
        if self.is_root is True:
            pass
            # raise ValidationError('Root object cannot be changed or deleted.')
        else:
            super(StatusModel, self).update(*args, **kwargs)
