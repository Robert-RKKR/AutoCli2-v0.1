# Django - choices model import:
from django.db.models import IntegerChoices

# Choices class:
class ResponseTypeChoices(IntegerChoices):

    # Choices values:
    EMPTY = 0, 'Empty'
    LIST = 1, 'List'
    DICT = 2, 'Dict'
    STRING = 3, 'String'
