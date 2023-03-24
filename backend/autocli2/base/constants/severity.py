from django.db.models import IntegerChoices

# Choices class:
class SeverityChoices(IntegerChoices):

    # Choices values:
    USER = 1, 'User notification'
    BACKLOG = 2, 'Backend log'
