# Django - models import:
from django.db import models

# Django - translation model import:
from django.utils.translation import gettext_lazy as _

# AutoCli2 - base models import:
from autocli2.base.models.base_model import BaseModel

# AutoCli2 - inventory model import:
from inventory.models.tag import Tag


# Tag model class:
class Tag(BaseModel):

    class Meta:
        
        # Model name values:
        verbose_name = _('Tag')
        verbose_name_plural = _('Tags')

        # Abstract class value:
        abstract = True

    # Relations with other classes:
    tag = models.ManyToManyField(
        Tag,
        verbose_name=_('Tag'),
        help_text=_('Related tag.'),
    )
