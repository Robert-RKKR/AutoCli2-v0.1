# Django - models import:
from django.db import models

# Django - translation model import:
from django.utils.translation import gettext_lazy as _

# AutoCli2 - base model import:
from autocli2.base.models.identification import IdentificationModel
from autocli2.base.models.tag import Tag


# Platform model class:
class Platform(IdentificationModel, Tag):

    class Meta:
        
        # Model name values:
        verbose_name = _('Platform')
        verbose_name_plural = _('Platforms')

    # API token information:
    api_token_heder_key = models.CharField(
        verbose_name=_('API token heder key'),
        help_text=_('When authenticating an API connection using an API ''\
        token, the token header key value defines the API request header '\
        'key. In the example "Authorization=APIToken {{key}}", the token '\
        'header key value is Authorization.'),
        max_length=128,
        null=True,
        blank=True,
    )

    api_token_heder_value = models.CharField(
        verbose_name=_('API token heder value'),
        help_text=_('When authenticating an API connection using an API '\
        'token, the token header value defines the API request header '\
        'key. In the example "Authorization=APIToken {{key}}", the '\
        'token header value is APIToken.'),
        max_length=128,
        null=True,
        blank=True,
    )

    # Pagination information:
    api_pagination = models.BooleanField(
        verbose_name=_('API pagination'),
        help_text=_('When the pagination value is active, the API request will '\
        'be repeated to collect all objects from all paginated pages.'),
        default=False,
    )

    api_next_page_code_path = models.JSONField(
        verbose_name=_('API next page code path'),
        help_text=_('The next page path value is used by the connection template '\
        'when the API request returns a response, that is divided into many pages '\
        '(paginated response). In this case next page path value is used to '\
        'retrieve the pagination code required to prepare the next API request '\
        'for other pages (The value will only be used if the pagination field is '\
        'enabled).'),
        null=True,
        blank=True,
    )

    api_next_page_link_path = models.JSONField(
        verbose_name=_('API next page link path'),
        help_text=_('The next page path value is used by the connection template '\
        'when the API request returns a response that is divided into many pages '\
        '(paginated response). In this case, the next page path value is used to '\
        'retrieve the pagination URL link used in the next API request for other '\
        'pages (The value will only be used if the pagination field is enabled).'),
        null=True,
        blank=True,
    )

    api_pagination_param_key = models.CharField(
        verbose_name=_('API pagination param key'),
        help_text=_('Information collected based on the next page code path value '\
        'is added to the URL with a specific code. This code should be provided '\
        'as a pagination param key value. For example, the value "cursor" will '\
        'be added to the URL in the form "?cursor={{next page code}}" '\
        '(The value will only be used if the pagination field is enabled).'),
        max_length=128,
        null=True,
        blank=True,
    )

    # Data path:
    api_data_path = models.JSONField(
        verbose_name=_('API data path'),
        help_text=_('The data path value is used to collect useful data included '\
        'in the API response.'),
        null=True,
        blank=True,
    )

    # API related default fields:
    api_default_header = models.JSONField(
        verbose_name=_('API default heder'),
        help_text=_('Default heder used during HTTP(S) requests.'),
        null=True,
        blank=True,
    )

    api_default_params = models.JSONField(
        verbose_name=_('API default parameters'),
        help_text=_('Default parameters used during HTTP(S) requests.'),
        null=True,
        blank=True,
    )
