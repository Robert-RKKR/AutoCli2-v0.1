# Django - models import:
from django.db import models

# Django - user model import:
from django.contrib.auth.models import User

# Django - translation model import:
from django.utils.translation import gettext_lazy as _

# AutoCli2 - constance import:
from autocli2.base.constants.action_type import ActionTypeChoices


# Base message model class:
class BaseMessageModel(models.Model):

    class Meta:

        # Abstract class value:
        abstract = True
    
    # Model data time information:
    timestamp = models.DateTimeField(
        verbose_name=_('Timestamp'),
        help_text=_('Time of the change creation.'),
        auto_now_add=True,
    )

    # Administrator information:
    administrator = models.ForeignKey(
        User,
        verbose_name=_('Administrator'),
        help_text=_(f'Administrator responsible for provided change.'),
        on_delete=models.PROTECT,
        null=True,
        blank=True,
    )

    # Message type:
    action_type = models.IntegerField(
        verbose_name=_('Type of action'),
        help_text=_('The type of action that was performed on the object.'),
        choices=ActionTypeChoices.choices,
        default=0,
    )

    # Information about correlated object:
    app_name = models.CharField(
        verbose_name=_('Object application name'),
        help_text=_('Name of the object application.'),
        max_length=64,
        null=True,
        blank=True,
    )
    model_name = models.CharField(
        verbose_name=_('Object model name'),
        help_text=_('Name of the object model.'),
        max_length=64,
        null=True,
        blank=True,
    )
    object_id = models.IntegerField(
        verbose_name=_('Object PK'),
        help_text=_('Correlated object PK representation.'),
        null=True,
        blank=True,
    )
    object_representation = models.CharField(
        verbose_name=_('Object representation'),
        help_text=_('Object representation.'),
        max_length=128,
        null=True,
        blank=True,
    )
    object_url = models.CharField(
        verbose_name=_('URL'),
        help_text=_('URL to object.'),
        max_length=256,
        null=True,
        blank=True,
    )

    # Execution time:
    execution_time = models.FloatField(
        verbose_name='Execution time',
        help_text='Log execution time.',
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
