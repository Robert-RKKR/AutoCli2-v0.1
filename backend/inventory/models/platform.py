# Django - models import:
from django.db import models

# Django - translation model import:
from django.utils.translation import gettext_lazy as _

# AutoCli2 - base model import:
from autocli2.base.models.identification import IdentificationModel
from autocli2.base.models.tag import Tag

# AutoCli2 - constance import:
from autocli2.base.constants.platform_type import PlatformTypeChoices


# Platform model class:
class Platform(IdentificationModel, Tag):

    class Meta:
        
        # Model name values:
        verbose_name = _('Platform')
        verbose_name_plural = _('Platforms')

    # HTTP / SSH - support:
    is_http_supported = models.BooleanField(
        verbose_name=_('Is HTTP(S) supported'),
        help_text=_('Is HTTP(S) protocol supported by platform.'),
        default=False,
    )
    is_ssh_supported = models.BooleanField(
        verbose_name=_('Is SSH supported'),
        help_text=_('Is SSH protocol supported by platform.'),
        default=False,
    )

    # HTTP - HTTP(S) token information:
    http_token_heder_key = models.CharField(
        verbose_name=_('API token heder key'),
        help_text=_('When authenticating an HTTP(S) connection using an API '\
            'token, the token key value is defined in the HTTP(S) request '\
            'header . In the example "Authorization=API_Token {{key}}", the '\
            'token header key value is Authorization.'),
        max_length=128,
        null=True,
        blank=True,
    )
    http_token_heder_value = models.CharField(
        verbose_name=_('API token heder value'),
        help_text=_('When authenticating an HTTP(S) connection using an API '\
            'token, the token value is defined in the HTTP(S) request header '\
            '. In the example "Authorization=API_Token {{key}}", the '\
            'token header value is API_Token.'),
        max_length=128,
        null=True,
        blank=True,
    )

    # HTTP - pagination information:
    http_pagination = models.BooleanField(
        verbose_name=_('HTTP(S) pagination'),
        help_text=_('When the pagination value is active, the HTTP(S) request '\
            'will be repeated to collect all objects from all paginated pages.'),
        default=False,
    )
    http_next_page_code_path = models.JSONField(
        verbose_name=_('HTTP(S) next page code path'),
        help_text=_('The next page path value is used by the connection template '\
            'when the HTTP(S) request returns a response, that is divided into '\
            'many pages (paginated response). In this case next page path value '\
            'is used to retrieve the pagination code required to prepare the next '\
            'HTTP(S) request for other pages (The value will only be used if '\
            'the pagination field is enabled).'),
        null=True,
        blank=True,
    )
    http_next_page_link_path = models.JSONField(
        verbose_name=_('HTTP(S) next page link path'),
        help_text=_('The next page path value is used by the connection template '\
            'when the HTTP(S) request returns a response that is divided into many '\
            'pages (paginated response). In this case, the next page path value '\
            'is used to retrieve the pagination URL link used in the next HTTP(S) '\
            'request for other pages (The value will only be used if the '\
            'pagination field is enabled).'),
        null=True,
        blank=True,
    )
    http_pagination_param_key = models.CharField(
        verbose_name=_('HTTP(S) pagination param key'),
        help_text=_('Information collected based on the next page code path value '\
            'is added to the URL with a specific code. This code should be provided '\
            'as a pagination param key value. For example, the value "cursor" will '\
            'be added to the URL in the form "?cursor={{next page code}}" '\
            '(The value will only be used if the pagination field is enabled).'),
        max_length=128,
        null=True,
        blank=True,
    )

    # HTTP - data path:
    http_data_path = models.JSONField(
        verbose_name=_('HTTP(S) data path'),
        help_text=_('The data path value is used to collect useful data included '\
            'in the HTTP(S) response.'),
        null=True,
        blank=True,
    )

    # HTTP - API related default fields:
    http_default_header = models.JSONField(
        verbose_name=_('HTTP(S) default heder'),
        help_text=_('Default heder used during HTTP(S) requests.'),
        null=True,
        blank=True,
    )
    http_default_params = models.JSONField(
        verbose_name=_('HTTP(S) default parameters'),
        help_text=_('Default parameters used during HTTP(S) requests.'),
        null=True,
        blank=True,
    )

    # SSH - invalid responses:
    ssh_invalid_responses = models.JSONField(
        verbose_name=_('SSH invalid responses'),
        help_text=_('List of strings that contain invalid host responses. '\
            'For example, the Cisco IOS system returns output such as '\
            '"invalid input detected" in the case of an unsupported command, '\
            'or "cdp is not enabled" in the case of an disabled function, in '\
            'this example CDP.'),
        null=True,
        blank=True,
    )

    # SSH - Netmiko settings:
    ssh_platform_type = models.CharField(
        verbose_name=_('Netmiko platform type'),
        help_text=_('Netmiko platform type (SSH only).'),
        max_length=32,
        choices=PlatformTypeChoices.choices,
        default=PlatformTypeChoices.GENERIC,
    )
