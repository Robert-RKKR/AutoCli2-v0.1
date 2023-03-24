# Django - choices model import:
from django.db.models import IntegerChoices

# Choices class:
class ShhExecutionTypeChoices(IntegerChoices):

    # Choices values:
    COMMAND = 1, 'SSH command'
    TEMPLATE = 2, 'SSH command template'


class HttpExecutionTypeChoices(IntegerChoices):

    # Choices values:
    GET = 1, 'Get HTTP(S) method'
    POST = 2, 'Post HTTP(S) method'
    PUT = 3, 'Put HTTP(S) method'
    DELETE = 4, 'Delete HTTP(S) method'
