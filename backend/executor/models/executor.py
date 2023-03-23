# Django - models import:
from django.db import models

# AutoCli2 - base models import:
from autocli2.base.models.identification import IdentificationModel
from autocli2.base.models.administrator import AdministratorModel

# AutoCli2 - connector model import:
from connector.models.connection_template import ConnectionTemplate

# AutoCli2 - inventory model import:
from inventory.models.credentials import Credential
from inventory.models.host import Host

# AutoCli2 - constance's import:
from autocli2.base.constants.executor_type import EXECUTOR_TYPES
from autocli2.base.constants.task import TASKS


# Executor model class:
class Executor(IdentificationModel, AdministratorModel):

    class Meta:
        
        # Model name values:
        verbose_name = 'Executor'
        verbose_name_plural = 'Executors'

    # Relations with other classes:
    hosts = models.ManyToManyField(
        Host,
        verbose_name='Hosts',
        help_text='Xxx.',
        blank=True,
    )
    connection_templates = models.ManyToManyField(
        ConnectionTemplate,
        verbose_name='Connection templates',
        help_text='Xxx.',
        blank=True,
    )

    # Executor type:
    executor_type = models.IntegerField(
        verbose_name='Executor type',
        help_text='Xxx.',
        choices=EXECUTOR_TYPES,
        default=1,
    )

    # Task fields:
    task = models.IntegerField(
        verbose_name='Task',
        help_text='Xxx.',
        choices=TASKS,
        default=0,
    )
    task_arguments = models.JSONField(
        verbose_name='Task arguments',
        help_text='Xxx.',
        null=True,
        blank=True,
    )
