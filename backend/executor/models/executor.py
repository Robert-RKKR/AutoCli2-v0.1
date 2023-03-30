# Django - models import:
from django.db import models

# Django - translation model import:
from django.utils.translation import gettext_lazy as _

# AutoCli2 - base models import:
from autocli2.base.models.identification import IdentificationModel
from autocli2.base.models.administrator import AdministratorModel

# AutoCli2 - connector model import:
from connector.models.connection_template import ConnectionTemplate

# AutoCli2 - inventory model import:
from inventory.models.credentials import Credential
from inventory.models.host import Host

# AutoCli2 - constance's import:
from autocli2.base.constants.executor_type import ExecutorTypeChoices
from autocli2.base.constants.task import TaskChoices


# Executor model class:
class Executor(IdentificationModel, AdministratorModel):

    class Meta:
        
        # Model name values:
        verbose_name = _('Executor')
        verbose_name_plural = _('Executors')

    # Relations with other classes:
    hosts = models.ManyToManyField(
        Host,
        verbose_name=_('Hosts'),
        help_text=_('Related hosts objects on witch execution will be '\
            'executed (Provides information such as host IP or domain '
            'name, platform, and credentials used to connect to the host).'),
        blank=True,
    )
    connection_templates = models.ManyToManyField(
        ConnectionTemplate,
        verbose_name=_('Connection templates'),
        help_text=_('Related connection template object based on witch '\
            'execution will be executed (Provides information about SSH / '\
            'HTTP(S) command or URL executed on host).'),
        blank=True,
    )

    # Executor type:
    executor_type = models.IntegerField(
        verbose_name=_('Executor type'),
        help_text=_('Execution type (HTTP(S) or SSH).'),
        choices=ExecutorTypeChoices.choices,
        default=1,
    )

    # Task fields:
    task = models.IntegerField(
        verbose_name=_('Task'),
        help_text=_('Task that will be executed.'),
        choices=TaskChoices.choices,
        default=0,
    )
    task_arguments = models.JSONField(
        verbose_name=_('Task arguments'),
        help_text=_('Task arguments used to run task.'),
        null=True,
        blank=True,
    )
