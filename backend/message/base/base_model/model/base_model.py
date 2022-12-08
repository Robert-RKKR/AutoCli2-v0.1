# Django Import:
from django.db import models

# Managers Import:
from ..managers.base_manager import BaseManager

# Notification constants:
SEVERITY = (
    (0, '---'),
    (1, 'CRITICAL'),
    (2, 'ERROR'),
    (3, 'WARNING'),
    (4, 'INFO'),
    (5, 'DEBUG'),
)
TYPE = (
    (0, '---'),
    (1, 'Create'),
    (2, 'Update'),
    (3, 'Delete')
)


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
    
    # Model data time information:
    timestamp = models.DateTimeField(
        verbose_name='Timestamp',
        help_text='Time of the change creation.',
        auto_now_add=True,
    )

    # Type and severity:
    type = models.IntegerField(
        verbose_name='Type of action',
        help_text='The type of action that was performed on a given model.',
        choices=TYPE,
        default=0,
    )
    severity = models.IntegerField(
        verbose_name='Notification severity',
        help_text='Severity level of notification message.',
        choices=SEVERITY,
        default=0,
    )

    # Task ID information:
    task_id = models.CharField(
        verbose_name='Task ID',
        help_text='ID of the associated task.',
        max_length=64,
        null=True,
        blank=True,
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
        verbose_name='Object ID',
        help_text='Correlated object ID representation.',
        null=True,
        blank=True,
    )
