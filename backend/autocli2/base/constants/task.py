# AutoCli2 - base integer model import:
from autocli2.base.constants.base.base_choices import BaseIntegerChoices

# Django - translation model import:
from django.utils.translation import gettext_lazy as _


# Choices class:
class TaskChoices(BaseIntegerChoices):

    # Choices values:
    FIRST = 1, _('Collect host/s data')
    SECOND = 2, _('Check host/s status')
