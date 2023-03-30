# AutoCli2 - base integer model import:
from autocli2.base.constants.base_integer_choices import BaseIntegerChoices

# Django - translation model import:
from django.utils.translation import gettext_lazy as _


# Choices class:
class NotificationTypeChoices(BaseIntegerChoices):

    # Choices values:
    USER = 1, _('User notification')
    BACKLOG = 2, _('Backend log')
