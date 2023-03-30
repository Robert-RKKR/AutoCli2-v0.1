# AutoCli2 - base integer model import:
from autocli2.base.constants.base_integer_choices import BaseIntegerChoices

# Django - translation model import:
from django.utils.translation import gettext_lazy as _


# Choices class:
class ActionTypeChoices(BaseIntegerChoices):

    # Choices values:
    EMPTY = 0, _('Empty')
    CREATE = 1, _('Create')
    UPDATE = 2, _('Update')
    DELETE = 3, _('Delete')
