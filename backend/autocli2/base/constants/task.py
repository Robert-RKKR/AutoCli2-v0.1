# Django - choices model import:
from django.db.models import IntegerChoices

# Choices class:
class TaskChoices(IntegerChoices):

    # Choices values:
    FIRST = 1, 'Collect host/s data'
    SECOND = 2, 'Check host/s status'
