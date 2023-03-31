# Django - models import:
from django.db import models

# Django - user model import:
from django.contrib.auth.models import User

# Django - translation model import:
from django.utils.translation import gettext_lazy as _

# AutoCli2 - base models import:
from autocli2.base.models.base_model import BaseModel


# Administrator models class:
class AdministratorModel(BaseModel):

    class Meta:
        
        # Model name values:
        verbose_name = _('AdministratorModel')
        verbose_name_plural = _('AdministratorModels')
        
        # Abstract class value:
        abstract = True

    # Administrator information:
    administrator = models.ForeignKey(
        User,
        verbose_name=_('Administrator'),
        help_text=_(f'Administrator responsible for provided {Meta.verbose_name}.'),
        on_delete=models.PROTECT,
        null=True,
        blank=True,
    )
