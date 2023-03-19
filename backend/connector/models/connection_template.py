# Django - models import:
from django.db import models

# AutoCli2 - connection template manager import:
from connector.managers.connection_template import ConnectionTemplateManager

# AutoCli2 - base models import:
from autocli2.base.models.identification import IdentificationModel
from autocli2.base.models.data_time import DataTimeModel
from autocli2.base.models.status import StatusModel

# AutoCli2 - inventory model import:
from inventory.models.platform import Platform

# AutoCli2 - connection template validator import:
from connector.validators.connection_template_validators import regex_validator

# AutoCli2 - inventory host constant import:
from inventory.models.host import EXECUTION_PROTOCOLS

# Connections template constants:
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
RESPONSE_TYPE = (
    (1, '----'),
    (2, 'List'),
    (3, 'Dict'),
    (4, 'String'),
)


# Connection template model class:
class ConnectionTemplate(StatusModel, DataTimeModel, IdentificationModel):

    class Meta:
        
        # Model name values:
        verbose_name = 'Connection template'
        verbose_name_plural = 'Connection templates'

    # Model objects manager:
    objects = ConnectionTemplateManager()

    # Relations with other classes:
    platforms = models.ManyToManyField(
        Platform,
        verbose_name='Platform',
        help_text='One or more platform(s) can be added to the connection '\
        'template. To associate the template with the appropriate platform(s). '\
        'Template execution will only be available to hosts belonging to '\
        'the specified platform.',
    )

    # Execution type:
    execution_protocol = models.IntegerField(
        verbose_name='Execution protocol',
        help_text='The network protocol that will be used to execute '\
        'connection template (SSH / HTTP(S)).',
        choices=EXECUTION_PROTOCOLS,
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
    ssh_special_template = models.BooleanField(
        verbose_name='Special template',
        help_text='Xxx.',
        default=False,
    )
    ssh_vrf_template = models.BooleanField(
        verbose_name='VRF template',
        help_text='VRF cli command template.',
        default=False,
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
    regex_expression = models.TextField(
        verbose_name='Regex expression',
        help_text='Regex expression used to validate the output '\
        'after the execution of the template.',
        validators=[regex_validator],
        null=True,
        blank=True,
    )
    response_type = models.IntegerField(
        verbose_name='Type of response',
        help_text='Xxx.',
        choices=RESPONSE_TYPE,
        default=1,
    )
