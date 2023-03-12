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

    # Check if object can be deleted:
    def can_be_deleted(self):
        # Return True if the object can be deleted, False otherwise:
        if self.is_root is True:
            return False
        else:
            return True

    # Model save method override:
    def save(self, *args, **kwargs):
        if self.pk is not None:
            # Check if object root value is true:
            if not self.can_be_deleted():
                return False
                # raise ValidationError(f"{self._meta.object_name} object can't be "\
                #     "changed because its root object")
        # Save object if allowed:
        super(StatusModel, self).save(*args, **kwargs)
        return True

    # Model delete method override:
    def delete(self, *args, **kwargs):
        # Check if object root value is true:
        if self.can_be_deleted():
            super(StatusModel, self).delete(*args, **kwargs)
            return True
        else:
            return False
            # raise ValidationError(f"{self._meta.object_name} object can't be "\
            #     "deleted because its root object")
