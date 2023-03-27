# Django - integer model import:
from django.db.models import IntegerChoices


# Choices class:
class BaseIntegerChoices(IntegerChoices):

    @property
    def value_from_int(cls, int_to_search):
        for choice in cls.choices:
            if choice[0] == int_to_search:
                return choice[1]
