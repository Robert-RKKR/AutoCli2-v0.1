# Django import:
from django.db import models

# Base models import:
from autocli2.base.models.identification import IdentificationModel
from autocli2.base.models.data_time import DataTimeModel
from autocli2.base.models.status import StatusModel

# Relations models import:
from .connection_ssh_template import ConnectionSshTemplate
from .connection_group import ConnectionGroup

# Other application relations model import:
from inventory.models.platform import Platform

# Connectiont template model constants:
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


# Connectiont template model clas:
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

    platforms = models.ManyToManyField(
        Platform,
        verbose_name='Platform',
        help_text='One or more platform(s) can be added to the connection '\
        'template. To associate the template with the appropriate platform(s). '\
        'Template execution will only be available to hosts belonging to '\
        'the specified platform.',
    )

    connection_ssh_template = models.ForeignKey(
        ConnectionSshTemplate,
        verbose_name='SSH template',
        help_text='SSH template.',
        on_delete=models.PROTECT
    )

    # Execution type:
    execution_protocol = models.IntegerField(
        verbose_name='Execution protocol',
        help_text='Network protocol used to execute the connection template '\
        '(SSH / HTTP).',
        choices=EXECUTION_PROTOCOL,
        default=1,
    )

    # SSH execution type fields:
    ssh_type = models.IntegerField(
        verbose_name='SSH execution type',
        help_text='Type of SSH execution (Command / template).',
        choices=SSH_EXECUTION_TYPE,
        default=1,
    )

    ssh_command = models.CharField(
        verbose_name='Xxx',
        help_text='Xxx.',
        max_length=128,
        null=True,
        blank=True,
    )

    ssh_fsm = models.TextField(
        verbose_name='Xxx',
        help_text='Xxx.',
    )

    # HTTP execution type fields:
    http_method = models.IntegerField(
        verbose_name='HTTP method',
        help_text='Xx (HTTP request methods).',
        choices=HTTP_EXECUTION_METHOD,
        default=1,
    )

    http_url = models.CharField(
        verbose_name='Xxx',
        help_text='Xxx.',
        max_length=128,
        null=True,
        blank=True,
    )

    http_header = models.JSONField(
        verbose_name='HTTP heder',
        help_text='Xxx.',
        null=True,
        blank=True,
    )

    http_params = models.JSONField(
        verbose_name='HTTP parameters',
        help_text='Xxx.',
        null=True,
        blank=True,
    )

    http_body = models.JSONField(
        verbose_name='HTTP body',
        help_text='Xxx.',
        null=True,
        blank=True,
    )

    http_pagination = models.BooleanField(
        verbose_name='Xxx',
        help_text='Xxx.',
        default=False,
    )

    http_pagination_path = models.JSONField(
        verbose_name='HTTP body',
        help_text='Xxx.',
        null=True,
        blank=True,
    )
