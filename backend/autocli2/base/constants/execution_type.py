# AutoCli2 - base integer model import:
from autocli2.base.constants.base.base_choices import BaseIntegerChoices

# Django - translation model import:
from django.utils.translation import gettext_lazy as _


# Choices classes:
class SshExecutionTypeChoices(BaseIntegerChoices):

    # Choices values:
    COMMAND = 1, _('SSH command')
    TEMPLATE = 2, _('SSH command template')


class HttpExecutionTypeChoices(BaseIntegerChoices):

    # Choices values:
    GET = 1, _('GET')
    POST = 2, _('POST')
    PUT = 3, _('PUT')
    DELETE = 4, _('DELETE')
