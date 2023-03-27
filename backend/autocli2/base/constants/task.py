# AutoCli2 - base integer model import:
from autocli2.base.constants.base_integer_choices import BaseIntegerChoices


# Choices class:
class TaskChoices(BaseIntegerChoices):

    # Choices values:
    FIRST = 1, 'Collect host/s data'
    SECOND = 2, 'Check host/s status'
