# AutoCli2 - base integer model import:
from autocli2.base.constants.base_integer_choices import BaseIntegerChoices


# Choices class:
class ResponseTypeChoices(BaseIntegerChoices):

    # Choices values:
    EMPTY = 0, 'Empty'
    LIST = 1, 'List'
    DICT = 2, 'Dict'
    STRING = 3, 'String'
