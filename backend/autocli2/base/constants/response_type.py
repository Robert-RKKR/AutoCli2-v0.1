# AutoCli2 - base integer model import:
from autocli2.base.constants.base.base_choices import BaseIntegerChoices

# Django - translation model import:
from django.utils.translation import gettext_lazy as _


# Choices class:
class ResponseTypeChoices(BaseIntegerChoices):

    # Choices values:
    EMPTY = 0, _('Empty')
    LIST = 1, _('List')
    DICT = 2, _('Dict')
    STRING = 3, _('String')
