# Django Import:
from django.db import models

# Base model import:
from autocli2.base.models.administrator import AdministratorModel
from autocli2.base.models.base_model import BaseModel

# Base message model constants:
ACTION_TYPE = (
    (0, '---'),
    (1, 'Create'),
    (2, 'Update'),
    (3, 'Delete')
)


# Base models class:
class BaseMessageModel(AdministratorModel):

    class Meta:

        # Abstract class value:
        abstract = True
    
    # Model data time information:
    timestamp = models.DateTimeField(
        verbose_name='Timestamp',
        help_text='Time of the change creation.',
        auto_now_add=True,
    )

    # Type:
    action_type = models.IntegerField(
        verbose_name='Type of action',
        help_text='The type of action that was performed on the object.',
        choices=ACTION_TYPE,
        default=0,
    )

    # Information about correlated object:
    app_name = models.CharField(
        verbose_name='Object application name',
        help_text='Name of the object application.',
        max_length=64,
        null=True,
        blank=True,
    )
    model_name = models.CharField(
        verbose_name='Object model name',
        help_text='Name of the object model.',
        max_length=64,
        null=True,
        blank=True,
    )
    object_id = models.IntegerField(
        verbose_name='Object PK',
        help_text='Correlated object PK representation.',
        null=True,
        blank=True,
    )
    object_representation = models.CharField(
        verbose_name='Object representation',
        help_text='Object representation.',
        max_length=128,
        null=True,
        blank=True,
    )

    # Object representation:
    def __repr__(self) -> str:
        return f'{self.pk}: {self.model_name}'

    def __str__(self) -> str:
        return  f'{self.pk}: {self.model_name}'

    # Natural key representation:
    def natural_key(self):
        return str(self.model_name)
