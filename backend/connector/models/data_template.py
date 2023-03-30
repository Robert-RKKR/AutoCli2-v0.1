# Django - model import:
from django.db import models

# Django - translation model import:
from django.utils.translation import gettext_lazy as _

# AutoCli2 - base model import:
from autocli2.base.models.base_model import BaseModel

# AutoCli2 - connector model import:
from connector.models.data_group_template import DataGroupTemplate
from connector.models.model_template import ModelTemplate


# Data template models class:
class DataTemplate(BaseModel):

    class Meta:
        
        # Model name values:
        verbose_name = _('Data template')
        verbose_name_plural = _('Data templates')

    # Relations with other classes:
    data_group_template = models.ForeignKey(
        DataGroupTemplate,
        verbose_name=_('Data group template'),
        help_text=_('Data group template.'),
        on_delete=models.PROTECT,
        null=True,
        blank=True,
    )
    model_template = models.ForeignKey(
        ModelTemplate,
        verbose_name=_('Model template'),
        help_text=_('Model template.'),
        on_delete=models.PROTECT,
        null=True,
        blank=True,
    )

    # Data path:
    path = models.JSONField(
        verbose_name=_('Path'),
        help_text=_('Xxx.'),
        null=True,
        blank=True,
    )
