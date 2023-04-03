# AutoCli2 - base integer model import:
from autocli2.base.constants.base.base_choices import BaseIntegerChoices

# Django - translation model import:
from django.utils.translation import gettext_lazy as _


# Choices class:
class ExecutionProtocolChoices(BaseIntegerChoices):

    # Choices values:
    SSH = 1, _('SSH')
    HTTP = 2, _('HTTP(S)')
    DISCOVERY = 3, _('Discovery')
