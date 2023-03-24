from django.db.models import IntegerChoices

# Choices class:
class NotificationTypeChoices(IntegerChoices):

    # Choices values:
    CRITICAL = 1, 'Critical'
    ERROR = 2, 'Error'
    WARNING = 3, 'Warning'
    INFO = 4, 'Info'
    DEBUG = 5, 'Debug'
