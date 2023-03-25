# Django - models import:
from django.db import models

# AutoCli2 - executor model import:
from management.models.administrator import Administrator

# AutoCli2 - base models import:
from autocli2.base.models.base_model import BaseModel


# Administrator models class:
class AdministratorModel(BaseModel):

    class Meta:
        
        # Model name values:
        verbose_name = 'AdministratorModel'
        verbose_name_plural = 'AdministratorModels'
        
        # Abstract class value:
        abstract = True

    # Administrator information:
    administrator = models.ForeignKey(
        Administrator,
        verbose_name='Administrator',
        help_text=f'Administrator responsible for provided {Meta.verbose_name}.',
        on_delete=models.PROTECT,
        null=True,
        blank=True,
    )
