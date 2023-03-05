# Django import:
from django.db import models

# Base models import:
from autocli2.base.models.identification import IdentificationModel
from autocli2.base.models.administrator import AdministratorModel
from autocli2.base.models.data_time import DataTimeModel
from autocli2.base.models.status import StatusModel

# Relations models import:
from connector.models.connection_template import ConnectionTemplate
from inventory.models.credentials import Credential
from inventory.models.host import Host

# Base message model constants:
EXECUTION_PROTOCOL = (
    (1, 'SSH'),
    (2, 'HTTP')
)
EXECUTOR_TYPE = (
    (1, 'Task'),
    (2, 'Template/s')
)
EXECUTOR_STATUS = (
    (1, 'Initiation'),
    (2, 'Execution'),
    (3, 'Executed')
)
TASK_ID = (
    (1, 'Task one'),
    (2, 'Task Two')
)


# Executor model class:
class Executor(StatusModel, DataTimeModel, IdentificationModel, AdministratorModel):

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
        choices=EXECUTOR_TYPE,
        default=1,
    )

    # Task fields:
    task = models.IntegerField(
        verbose_name='Task',
        help_text='Xxx.',
        choices=TASK_ID,
        default=0,
    )
    task_arguments = models.JSONField(
        verbose_name='Task arguments',
        help_text='Xxx.',
        null=True,
        blank=True,
    )

    # Status fields:
    status = models.IntegerField(
        verbose_name='Status',
        help_text='Xxx.',
        choices=EXECUTOR_STATUS,
        default=0,
    )
    output = models.JSONField(
        verbose_name='Output',
        help_text='Xxx.',
        null=True,
        blank=True,
    )
    results = models.BooleanField(
        verbose_name='Results',
        help_text='Xxx.',
        default=False,
    )
