# Django - model import:
from django.db import models

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
        verbose_name = 'Data group template'
        verbose_name_plural = 'Data group templates'

    # Relations with other classes:
    model_group_template = models.ForeignKey(
        ModelGroupTemplate,
        verbose_name='Model group template',
        help_text='Model group template.',
        on_delete=models.PROTECT,
        null=True,
        blank=True,
    )
    connection_template  = models.ForeignKey(
        ConnectionTemplate,
        verbose_name='Connection template',
        help_text='Connection template.',
        on_delete=models.PROTECT,
        null=True,
        blank=True,
    )
    platform = models.ManyToManyField(
        Platform,
        verbose_name='Software',
        help_text='One or more software(s) can be added to the connection '\
            'template. To associate the template with the appropriate '\
            'software(s). Template execution will only be available to '\
            'hosts belonging to the specified software.',
    )

    # Data group specific fields:
    keys = models.JSONField(
        verbose_name='Keys',
        help_text='Xxx.',
        null=True,
        blank=True,
    )
    keys_regex = models.CharField(
        verbose_name='Keys REGEX',
        help_text='Xxx.',
        max_length=128,
        null=True,
        blank=True,
    )
