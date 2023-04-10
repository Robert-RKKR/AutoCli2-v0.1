# Django - models import:
from django.db import models

# Django - translation model import:
from django.utils.translation import gettext_lazy as _

# AutoCli2 - base model import:
from autocli2.base.models.base_model import BaseModel

# AutoCli2 - connector model import:
from connector.models.data_template import DataTemplate

# AutoCli2 - executor model import:
from executor.models.execution import Execution
from executor.models.snapshot  import Snapshot


# Converted data model class:
class ConvertedData(BaseModel):

    class Meta:
        
        # Model name values:
        verbose_name = _('Converted data')
        verbose_name_plural = _('Converted data')

    # Relations with other classes:
    snapshot = models.ForeignKey(
        Snapshot,
        verbose_name=_('Snapshot'),
        help_text=_('Related snapshot object.'),
        on_delete=models.PROTECT,
        null=True,
        blank=True,
    )
    execution = models.ForeignKey(
        Execution,
        verbose_name=_('Execution'),
        help_text=_('Related execution object from which '\
            'collected data was taken.'),
        on_delete=models.PROTECT,
    )
    data_template = models.ForeignKey(
        DataTemplate,
        verbose_name=_('Data template'),
        help_text=_('Related data template object based on '\
            'which collected data was correlated.'),
        on_delete=models.PROTECT,
    )

    # Collected data:
    value = models.CharField(
        verbose_name=_('Value'),
        help_text=_('Value collected from related execution '\
            'object based on Data Template object.'),
        max_length=128,
        null=True,
        blank=True,
    )
    json_value = models.JSONField(
        verbose_name=_('JSON value'),
        help_text=_('JSON value collected from related execution '\
            'object based on Data Template object.'),
        null=True,
        blank=True,
    )
