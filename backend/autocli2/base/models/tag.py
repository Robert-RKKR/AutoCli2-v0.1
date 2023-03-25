# Django - models import:
from django.db import models

# AutoCli2 - base models import:
from autocli2.base.models.base_model import BaseModel

# AutoCli2 - inventory model import:
from inventory.models.tag import Tag


# Tag model class:
class Tag(BaseModel):

    class Meta:
        
        # Model name values:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'

        # Abstract class value:
        abstract = True

    # Relations with other classes:
    tag = models.ForeignKey(
        Tag,
        verbose_name='Tag',
        help_text='Related tag.',
        on_delete=models.PROTECT,
        null=True,
        blank=True,
    )
