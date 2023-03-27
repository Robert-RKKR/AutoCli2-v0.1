# AutoCli2 - base integer model import:
from autocli2.base.constants.base_integer_choices import BaseIntegerChoices


# Choices class:
class ExecutionProtocolChoices(BaseIntegerChoices):

    # Choices values:
    SSH = 1, 'SSH'
    HTTP = 2, 'HTTP(S)'
    DISCOVERY = 3, 'Discovery'
