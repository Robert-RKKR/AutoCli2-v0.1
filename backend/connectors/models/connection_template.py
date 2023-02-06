# Django Import:
from django.db import models

# Base model import:
from autocli2.base.models.identification import IdentificationModel
from autocli2.base.models.data_time import DataTimeModel
from autocli2.base.models.status import StatusModel

# Base message model constants:
EXECUTION_TYPE = (
    (1, 'SSH'),
    (2, 'HTTPS')
)
SSH_EXECUTION_TYPE = (
    (1, 'Command'),
    (2, 'template')
)
HTTPS_EXECUTION_METHOD = (
    (1, 'Get'),
    (2, 'Post'),
    (3, 'Put'),
    (4, 'Delete'),
)


# Base models class:
class ConnectionTemplate(StatusModel, DataTimeModel, IdentificationModel):

    class Meta:
        
        # Model name values:
        verbose_name = 'Connection template'
        verbose_name_plural = 'Connection templates'

    # Relations with other classes:
    # connection_template_group = models.ForeignKey(
    #     ConnectionTemplateGroup,
    #     verbose_name='Connection template group',
    #     help_text='Connection template group.',
    #     on_delete=models.PROTECT,
    #     null=True,
    #     blank=True,
    # )

    # platform = models.ForeignKey(
    #     Platform,
    #     verbose_name='Platform',
    #     help_text='Platform.',
    #     on_delete=models.PROTECT,
    #     null=True,
    #     blank=True,
    # )

    # template = models.ForeignKey(
    #     Template,
    #     verbose_name='SSH template',
    #     help_text='SSH template.',
    #     on_delete=models.PROTECT,
    #     null=True,
    #     blank=True,
    # )

    # Execution type:
    execution_method = models.IntegerField(
        verbose_name='Execution method',
        help_text='Method of template execution (SSH / HTTPS).',
        choices=EXECUTION_TYPE,
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

    # HTTPS execution type fields:
    https_method = models.IntegerField(
        verbose_name='HTTPS method',
        help_text='Xx (HTTPS request methods).',
        choices=HTTPS_EXECUTION_METHOD,
        default=1,
    )

    https_url = models.CharField(
        verbose_name='Xxx',
        help_text='Xxx.',
        max_length=128,
        null=True,
        blank=True,
    )

    https_header = models.JSONField(
        verbose_name='HTTPS heder',
        help_text='Xxx.',
        null=True,
        blank=True,
    )

    https_params = models.JSONField(
        verbose_name='HTTPS parameters',
        help_text='Xxx.',
        null=True,
        blank=True,
    )

    https_body = models.JSONField(
        verbose_name='HTTPS body',
        help_text='Xxx.',
        null=True,
        blank=True,
    )

    https_pagination = models.BooleanField(
        verbose_name='Xxx',
        help_text='Xxx.',
        default=False,
    )

    https_pagination_path = models.JSONField(
        verbose_name='HTTPS body',
        help_text='Xxx.',
        null=True,
        blank=True,
    )

    # Check certificate:
    certificate = models.BooleanField(
        verbose_name='Xxx',
        help_text='Xxx.',
        default=False,
    )
