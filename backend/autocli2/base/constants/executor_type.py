# AutoCli2 - base integer model import:
from autocli2.base.constants.base_integer_choices import BaseIntegerChoices

# Django - translation model import:
from django.utils.translation import gettext_lazy as _


# Choices class:
class ExecutorTypeChoices(BaseIntegerChoices):

    # Choices values:
    TASK = 1, _('Task')
    TEMPLATE = 2, _('Template/s')

