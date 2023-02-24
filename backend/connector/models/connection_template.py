# Django import:
from django.db import models

# Base models import:
from autocli2.base.models.identification import IdentificationModel
from autocli2.base.models.data_time import DataTimeModel
from autocli2.base.models.status import StatusModel

# Relations models import:
from .connection_group import ConnectionGroup

# Other application relations model import:
from inventory.models.software import Software

# Connections template model constants:
EXECUTION_PROTOCOL = (
    (1, 'SSH'),
    (2, 'HTTP')
)
SSH_EXECUTION_TYPE = (
    (1, 'Command'),
    (2, 'template')
)
HTTP_EXECUTION_METHOD = (
    (1, 'GET'),
    (2, 'POST'),
    (3, 'PUT'),
    (4, 'DELETE'),
)


# Connection template model class:
class ConnectionTemplate(StatusModel, DataTimeModel, IdentificationModel):

    class Meta:
        
        # Model name values:
        verbose_name = 'Connection template'
        verbose_name_plural = 'Connection templates'

    # Relations with other classes:
    connection_template_groups = models.ManyToManyField(
        ConnectionGroup,
        verbose_name='Connection template group',
        help_text='Connection template can be added to one or '\
        'more connection template group(s). For the purpose of '\
        'arranging templates in order.',
    )

    softwares = models.ManyToManyField(
        Software,
        verbose_name='Software',
        help_text='One or more software(s) can be added to the connection '\
        'template. To associate the template with the appropriate software(s). '\
        'Template execution will only be available to hosts belonging to '\
        'the specified software.',
    )

    # Execution type:
    execution_protocol = models.IntegerField(
        verbose_name='Execution protocol',
        help_text='The network protocol that will be used to execute '\
        'connection template (SSH / HTTP(S)).',
        choices=EXECUTION_PROTOCOL,
        default=1,
    )

    # SSH execution type fields:
    ssh_type = models.IntegerField(
        verbose_name='SSH execution type',
        help_text='Type of SSH connection template (Command / template).',
        choices=SSH_EXECUTION_TYPE,
        default=1,
    )

    ssh_command = models.CharField(
        verbose_name='CLI command',
        help_text='The CLI command that will be executed on the remote host.',
        max_length=128,
        null=True,
        blank=True,
    )

    ssh_template = models.TextField(
        verbose_name='Template',
        help_text='SSh template will be used to create CLI command(s), '\
        'which will be executed in the remote host to change configuration.',
        null=True,
        blank=True,
    )

    # HTTP execution type fields:
    http_method = models.IntegerField(
        verbose_name='HTTP(S) request method',
        help_text='Type of HTTP request method (GET, POST, PUT, DELETE).',
        choices=HTTP_EXECUTION_METHOD,
        default=1,
    )

    http_url = models.CharField(
        verbose_name='HTTP(S) URL',
        help_text='HTTP(S) URL field used to generate API request.',
        max_length=128,
        null=True,
        blank=True,
    )

    http_header = models.JSONField(
        verbose_name='HTTP(S) heder',
        help_text='HTTP(S) heder field used to generate API request.',
        null=True,
        blank=True,
    )

    http_params = models.JSONField(
        verbose_name='HTTP(S) parameters',
        help_text='HTTP(S) parameters field used to generate API request.',
        null=True,
        blank=True,
    )

    http_body = models.JSONField(
        verbose_name='HTTP(S) body',
        help_text='HTTP(S) body field used to generate API request.',
        null=True,
        blank=True,
    )

    # Output validation expressions:
    sfm_expression = models.TextField(
        verbose_name='SFM expression',
        help_text='FSM expression used to validate the output '\
        'after the execution of the template.',
        null=True,
        blank=True,
    )

    regex_expression = models.TextField(
        verbose_name='Regex expression',
        help_text='Regex expression used to validate the output '\
        'after the execution of the template.',
        null=True,
        blank=True,
    )
