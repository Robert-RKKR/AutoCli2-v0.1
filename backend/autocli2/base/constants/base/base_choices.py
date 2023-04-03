# Django - integer model import:
from django.db.models import IntegerChoices
from django.db.models import TextChoices

# Django - translation model import:
from django.utils.translation import gettext_lazy as _


# Choices classes:
class BaseIntegerChoices(IntegerChoices):

    @classmethod
    def value_from_int(cls, int_to_search):
        for choice in cls.choices:
            if choice[0] == int_to_search:
                return choice[1]


class BaseTextChoices(TextChoices):

    @classmethod
    def value_from_str(cls, int_to_search):
        for choice in cls.choices:
            if choice[0] == int_to_search:
                return choice[1]
