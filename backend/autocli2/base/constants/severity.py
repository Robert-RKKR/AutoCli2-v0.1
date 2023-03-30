# AutoCli2 - base integer model import:
from autocli2.base.constants.base_integer_choices import BaseIntegerChoices

# Django - translation model import:
from django.utils.translation import gettext_lazy as _


# Choices class:
class SeverityChoices(BaseIntegerChoices):

    # Choices values:
    CRITICAL = 1, _('Critical')
    ERROR = 2, _('Error')
    WARNING = 3, _('Warning')
    INFO = 4, _('Info')
    DEBUG = 5, _('Debug')
