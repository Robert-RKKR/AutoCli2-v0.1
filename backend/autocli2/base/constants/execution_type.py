# Django - choices model import:
from django.db.models import IntegerChoices

# Choices class:
class ShhExecutionTypeChoices(IntegerChoices):

    # Choices values:
    COMMAND = 1, 'SSH command'
    TEMPLATE = 2, 'SSH command template'


class HttpExecutionTypeChoices(IntegerChoices):

    # Choices values:
    GET = 1, 'GET'
    POST = 2, 'POST'
    PUT = 3, 'PUT'
    DELETE = 4, 'DELETE'
