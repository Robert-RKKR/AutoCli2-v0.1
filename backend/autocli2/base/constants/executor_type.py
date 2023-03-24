# Django - choices model import:
from django.db.models import IntegerChoices

# Choices class:
class ExecutorTypeChoices(IntegerChoices):

    # Choices values:
    TASK = 1, 'Task'
    TEMPLATE = 2, 'Template/s'

