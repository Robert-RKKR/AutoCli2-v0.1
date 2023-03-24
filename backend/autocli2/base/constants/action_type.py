from django.db.models import IntegerChoices

# Choices class:
class ActionTypeChoices(IntegerChoices):

    # Choices values:
    EMPTY = 0, 'Empty'
    CREATE = 1, 'Create'
    UPDATE = 2, 'Update'
    DELETE = 3, 'Delete'
