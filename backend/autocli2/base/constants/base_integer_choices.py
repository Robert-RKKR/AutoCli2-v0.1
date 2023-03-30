# AutoCli2 - base integer model import:
from autocli2.base.constants.base_integer_choices import BaseIntegerChoices

# Django - translation model import:
from django.utils.translation import gettext_lazy as _


# Choices class:
class BaseIntegerChoices(BaseIntegerChoices):

    @classmethod
    def value_from_int(cls, int_to_search):
        for choice in cls.choices:
            if choice[0] == int_to_search:
                return choice[1]
