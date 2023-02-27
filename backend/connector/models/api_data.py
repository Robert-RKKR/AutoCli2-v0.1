# Django import:
from django.db import models

# Base models import:
from autocli2.base.models.identification import IdentificationModel
from autocli2.base.models.data_time import DataTimeModel
from autocli2.base.models.status import StatusModel


# Data time models class:
class ApiData(StatusModel, DataTimeModel, IdentificationModel):

    class Meta:
        
        # Model name values:
        verbose_name = 'API data'
        verbose_name_plural = 'API data'

        # Abstract class value:
        abstract = True

    # API token information:
    http_token_heder_key = models.CharField(
        verbose_name='HTTP(S) token heder key',
        help_text='When authenticating an HTTP(S) connection using an API ''\
        token, the token header key value defines the HTTP(S) request header '\
        'key. In the example "Authorisation=APIToken {{key}}", the token '\
        'header key value is Authorisation.',
        max_length=128,
        null=True,
        blank=True,
    )

    http_token_heder_value = models.CharField(
        verbose_name='HTTP(S) token heder value',
        help_text='When authenticating an HTTP(S) connection using an API '\
        'token, the token header value defines the HTTP(S) request header '\
        'key. In the example "Authorisation=APIToken {{key}}", the '\
        'token header value is APIToken.',
        max_length=128,
        null=True,
        blank=True,
    )

    # Pagination information:
    http_pagination = models.BooleanField(
        verbose_name='HTTP(S) pagination',
        help_text='When the pagination value is active, the API request will '\
        'be repeated to collect all objects from all paginated pages.',
        default=True,
    )

    http_next_page_code_path = models.JSONField(
        verbose_name='HTTP(S) next page code path',
        help_text='The next page path value is used by the connection template '\
        'when the API request returns a response, that is divided into many pages '\
        '(paginated response). In this case next page path value is used to '\
        'retrieve the pagination code required to prepare the next API request '\
        'for other pages (The value will only be used if the pagination field is '\
        'enabled).',
        null=True,
        blank=True,
    )

    http_next_page_link_path = models.JSONField(
        verbose_name='HTTP(S) next page link path',
        help_text='The next page path value is used by the connection template '\
        'when the API request returns a response that is divided into many pages '\
        '(paginated response). In this case, the next page path value is used to '\
        'retrieve the pagination URL link used in the next API request for other '\
        'pages (The value will only be used if the pagination field is enabled).',
        null=True,
        blank=True,
    )

    http_pagination_param_key = models.CharField(
        verbose_name='HTTP(S) pagination param key',
        help_text='Information collected based on the next page code path value '\
        'is added to the URL with a specific code. This code should be provided '\
        'as a pagination param key value. For example, the value "cursor" will '\
        'be added to the URL in the form "?cursor={{next page code}}" '\
        '(The value will only be used if the pagination field is enabled).',
        max_length=128,
        null=True,
        blank=True,
    )

    # Data path:
    http_data_path = models.JSONField(
        verbose_name='HTTP(S) data path',
        help_text='The data path value is used to collect useful data included '\
        'in the HTTP(S) response.',
        null=True,
        blank=True,
    )

    # API related default fields:
    http_default_header = models.JSONField(
        verbose_name='HTTP(S) default heder',
        help_text='Xxx.',
        null=True,
        blank=True,
    )

    http_default_params = models.JSONField(
        verbose_name='HTTP(S) default parameters',
        help_text='Xxx.',
        null=True,
        blank=True,
    )
