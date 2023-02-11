# Django import:
from django.db import models

# Base model import:
from .base_model import BaseModel


# Status models class:
class StatusModel(BaseModel):

    class Meta:
        
        # Abstract class value:
        abstract = True

    # Deleted information:
    is_deleted = models.BooleanField(
        verbose_name='Deleted',
        help_text='Is object deleted (Deleted object is reserved for backward compatibility).',
        default=False,
    )

    # Model status values:
    is_root = models.BooleanField(
        verbose_name='Root',
        help_text='Is object root (Root object cannot be deleted or modify).',
        default=False,
    )
    is_active = models.BooleanField(
        verbose_name='Active',
        help_text='Is object active (Inactive object has limited functionality).',
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

    # Object representation:
    def __repr__(self) -> str:
        return f'{self.pk}: {self.is_deleted}'

    def __str__(self) -> str:
        return  f'{self.pk}: {self.is_deleted}'

    # Natural key representation:
    def natural_key(self):
        return str(self.is_deleted)