# Django import:
from django.db import models

# Base models import:
from autocli2.base.models.data_time import DataTimeModel

# Relations models import:
from connector.models.connection_template import ConnectionTemplate
from inventory.models.credentials import Credential
from inventory.models.host import Host
from .executor import Executor


# Execution model class:
class Execution(DataTimeModel):

    class Meta:
        
        # Model name values:
        verbose_name = 'Execution'
        verbose_name_plural = 'Executions'

    # Relations with other classes:
    executor = models.ForeignKey(
        Executor,
        verbose_name='Executor',
        help_text='Xxx.',
        on_delete=models.PROTECT,
    )
    host = models.ForeignKey(
        Host,
        verbose_name='Hosts',
        help_text='Xxx.',
        on_delete=models.PROTECT
    )
    connection_template = models.ForeignKey(
        ConnectionTemplate,
        verbose_name='Connection templates',
        help_text='Xxx.',
        on_delete=models.PROTECT
    )
    credential = models.ForeignKey(
        Credential,
        verbose_name='Credential',
        help_text='Xxx.',
        on_delete=models.PROTECT
    )

    # Related task ID:
    task_id = models.CharField(
        verbose_name='Task ID',
        help_text='ID of the associated task.',
        max_length=64,
        null=True,
        blank=True,
    )

    # 
    result_status = models.BooleanField(
        verbose_name='Result status',
        help_text='A positive result means that the command output was successfully received and processed.',
        default=False,
    )

    # Ssh status values:
    ssh_raw_data_status = models.BooleanField(
        verbose_name='Raw data status',
        help_text='A positive result means that the raw data collection process has been successfully completed.',
        default=False,
    )
    ssh_processed_data_status = models.BooleanField(
        verbose_name='Processed data status',
        help_text='A positive result means that the process of processing the data was completed successfully.',
        default=False,
    )

    # SSH data:
    ssh_raw_data = models.TextField(
        verbose_name='Command raw data',
        help_text='CLI command raw data output.',
        null=True,
        blank=True,
    )
    ssh_processed_data = models.JSONField(
        verbose_name='Command processed data',
        help_text='CLI command FSM process data.',
        null=True,
        blank=True,
    )

    # HTTP status and data:
    https_response_status = models.BooleanField(
        verbose_name='HTTP(S) response status',
        help_text='Xxx.',
        default=False,
    )

    https_response_code = models.IntegerField(
        verbose_name='HTTP(S) response code',
        help_text='Xxx.',
        default=0,
    )

    https_response = models.JSONField(
        verbose_name='HTTP(S) response',
        help_text='Xxx.',
        null=True,
        blank=True,
    )
