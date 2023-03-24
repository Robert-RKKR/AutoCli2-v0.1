from django.db.models import IntegerChoices

# Choices class:
class NotificationTypeChoices(IntegerChoices):

    # Choices values:
    USER = 1, 'User notification'
    BACKLOG = 2, 'Backend log'
