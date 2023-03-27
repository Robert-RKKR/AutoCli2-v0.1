# AutoCli2 - base integer model import:
from autocli2.base.constants.base_integer_choices import BaseIntegerChoices


# Choices class:
class NotificationTypeChoices(BaseIntegerChoices):

    # Choices values:
    USER = 1, 'User notification'
    BACKLOG = 2, 'Backend log'
