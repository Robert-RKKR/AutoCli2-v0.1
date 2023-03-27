# AutoCli2 - base integer model import:
from autocli2.base.constants.base_integer_choices import BaseIntegerChoices


# Choices class:
class SeverityChoices(BaseIntegerChoices):

    # Choices values:
    CRITICAL = 1, 'Critical'
    ERROR = 2, 'Error'
    WARNING = 3, 'Warning'
    INFO = 4, 'Info'
    DEBUG = 5, 'Debug'
