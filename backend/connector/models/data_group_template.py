# Django - model import:
from django.db import models

# Django - translation model import:
from django.utils.translation import gettext_lazy as _

# AutoCli2 - base model import:
from autocli2.base.models.base_model import BaseModel

# AutoCli2 - connector model import:
from connector.models.model_group_template import ModelGroupTemplate
from connector.models.connection_template import ConnectionTemplate

# AutoCli2 - inventory model import:
from inventory.models.platform import Platform


# Data group template models class:
class DataGroupTemplate(BaseModel):

    class Meta:
        
        # Model name values:
        verbose_name = _('Data group template')
        verbose_name_plural = _('Data group templates')

    # Relations with other classes:
    model_group_template = models.ForeignKey(
        ModelGroupTemplate,
        verbose_name=_('Model group template'),
        help_text=_('Model group template.'),
        on_delete=models.PROTECT,
        null=True,
        blank=True,
    )
    connection_template  = models.ForeignKey(
        ConnectionTemplate,
        verbose_name=_('Connection template'),
        help_text=_('Connection template.'),
        on_delete=models.PROTECT,
        null=True,
        blank=True,
    )
    platform = models.ManyToManyField(
        Platform,
        verbose_name=_('Software'),
        help_text=_('One or more software(s) can be added to the connection '\
            'template. To associate the template with the appropriate '\
            'software(s). Template execution will only be available to '\
            'hosts belonging to the specified software.'),
    )

    # Data group specific fields:
    keys = models.JSONField(
        verbose_name=_('Keys'),
        help_text=_('Xxx.'),
        null=True,
        blank=True,
    )
    keys_regex = models.CharField(
        verbose_name=_('Keys REGEX'),
        help_text=_('Xxx.'),
        max_length=128,
        null=True,
        blank=True,
    )
