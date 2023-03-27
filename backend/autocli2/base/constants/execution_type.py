# AutoCli2 - base integer model import:
from autocli2.base.constants.base_integer_choices import BaseIntegerChoices


# Choices classes:
class ShhExecutionTypeChoices(BaseIntegerChoices):

    # Choices values:
    COMMAND = 1, 'SSH command'
    TEMPLATE = 2, 'SSH command template'


class HttpExecutionTypeChoices(BaseIntegerChoices):

    # Choices values:
    GET = 1, 'GET'
    POST = 2, 'POST'
    PUT = 3, 'PUT'
    DELETE = 4, 'DELETE'
