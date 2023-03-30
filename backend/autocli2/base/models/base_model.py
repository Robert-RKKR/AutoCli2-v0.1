# Django - models import:
from django.db import models

# Django - translation model import:
from django.utils.translation import gettext_lazy as _

# AutoCli2 - base models import:
from autocli2.base.managers.base_manager import BaseManager


# Base models class:
class BaseModel(models.Model):

    class Meta:
        
        # Model name values:
        verbose_name = _('Base model')
        verbose_name_plural = _('Base models')

        # Abstract class value:
        abstract = True

    # Model objects manager:
    objects = BaseManager()

    # Model status values:
    is_deleted = models.BooleanField(
        verbose_name=_('Deleted'),
        help_text=_(f'Is {Meta.verbose_name} object deleted.'),
        default=False,
    )
    is_root = models.BooleanField(
        verbose_name=_('Root'),
        help_text=_(f'Is {Meta.verbose_name} root (Root {Meta.verbose_name} '\
        'cannot be deleted or modify).'),
        default=False,
    )
    is_active = models.BooleanField(
        verbose_name=_('Active'),
        help_text=_(f'Is {Meta.verbose_name} active (Inactive {Meta.verbose_name} '\
        'has limited functionality).'),
        default=True,
    )

    # Model data time information:
    created = models.DateTimeField(
        verbose_name=_('Created'),
        help_text=_(f'{Meta.verbose_name} create date.'),
        auto_now_add=True,
    )
    updated = models.DateTimeField(
        verbose_name=_('Updated'),
        help_text=_(f'{Meta.verbose_name} last update date.'),
        auto_now=True,
    )

    # object representation:
    def __repr__(self) -> str:
        return f'PK: {self.pk}'

    def __str__(self) -> str:
        return  f'PK: {self.pk}'

    # Natural key representation:
    def natural_key(self):
        return f'PK: {self.pk}'
