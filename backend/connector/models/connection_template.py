# Django - models import:
from django.db import models

# Django - translation model import:
from django.utils.translation import gettext_lazy as _

# AutoCli2 - connection template manager import:
from connector.managers.connection_template import ConnectionTemplateManager

# AutoCli2 - base model import:
from autocli2.base.models.identification import IdentificationModel

# AutoCli2 - inventory model import:
from inventory.models.platform import Platform

# AutoCli2 - connection template validator import:
from connector.validators.connection_template_validators import regex_validator

# AutoCli2 - constance import:
from autocli2.base.constants.execution_protocol import ExecutionProtocolChoices
from autocli2.base.constants.execution_type import HttpExecutionTypeChoices
from autocli2.base.constants.execution_type import ShhExecutionTypeChoices
from autocli2.base.constants.response_type import ResponseTypeChoices


# Connection template model class:
class ConnectionTemplate(IdentificationModel):

    class Meta:
        
        # Model name values:
        verbose_name = _('Connection template')
        verbose_name_plural = _('Connection templates')

    # Model objects manager:
    objects = ConnectionTemplateManager()

    # Relations with other classes:
    platforms = models.ManyToManyField(
        Platform,
        verbose_name=_('Platform'),
        help_text=_('One or more platform(s) can be added to the connection '\
            'template. To associate the template with the appropriate '\
            'platform(s). Template execution will only be available to '\
            'hosts belonging to the specified platform.'),
    )

    # Execution type:
    execution_protocol = models.IntegerField(
        verbose_name=_('Execution protocol'),
        help_text=_('The network protocol that will be used to execute '\
            'connection template (SSH / HTTP(S)).'),
        choices=ExecutionProtocolChoices.choices,
        default=1,
    )

    # SSH execution type fields:
    ssh_type = models.IntegerField(
        verbose_name=_('SSH execution type'),
        help_text=_('Type of SSH connection template (Command / template).'),
        choices=ShhExecutionTypeChoices.choices,
        default=1,
    )
    ssh_command = models.CharField(
        verbose_name=_('CLI command'),
        help_text=_('The CLI command that will be executed on the remote host.'),
        max_length=128,
        null=True,
        blank=True,
    )
    ssh_template = models.TextField(
        verbose_name=_('Template'),
        help_text=_('SSh template will be used to create CLI command(s), '\
            'which will be executed in the remote host to change configuration.'),
        null=True,
        blank=True,
    )
    ssh_special_template = models.BooleanField(
        verbose_name=_('Special template'),
        help_text=_('SSH special template.'),
        default=False,
    )
    ssh_vrf_template = models.BooleanField(
        verbose_name=_('VRF template'),
        help_text=_('VRF cli command template.'),
        default=False,
    )

    # HTTP execution type fields:
    http_method = models.IntegerField(
        verbose_name=_('HTTP(S) request method'),
        help_text=_('Type of HTTP request method (GET, POST, PUT, DELETE).'),
        choices=HttpExecutionTypeChoices.choices,
        default=1,
    )
    http_url = models.CharField(
        verbose_name=_('HTTP(S) URL'),
        help_text=_('HTTP(S) URL field used to generate API request.'),
        max_length=128,
        null=True,
        blank=True,
    )
    http_params = models.JSONField(
        verbose_name=_('HTTP(S) parameters'),
        help_text=_('HTTP(S) parameters field used to generate API request.'),
        null=True,
        blank=True,
    )
    http_body = models.JSONField(
        verbose_name=_('HTTP(S) body'),
        help_text=_('HTTP(S) body field used to generate API request.'),
        null=True,
        blank=True,
    )
    http_response_type = models.IntegerField(
        verbose_name=_('HTTP(s) type of response'),
        help_text=_('Type of HTTP(S) response. If the host sends a response '\
            'of a different type than specified, the response will be '\
            'treated as invalid.'),
        choices=ResponseTypeChoices.choices,
        default=0,
    )

    # Output validation expressions:
    regex_expression = models.TextField(
        verbose_name=_('Regex expression'),
        help_text=_('Regex expression used to validate the output '\
            'after the execution of the template.'),
        validators=[regex_validator],
        null=True,
        blank=True,
    )
