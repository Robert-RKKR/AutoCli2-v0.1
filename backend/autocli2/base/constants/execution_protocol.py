from django.db.models import IntegerChoices

# Choices class:
class ExecutionProtocolChoices(IntegerChoices):

    # Choices values:
    SSH = 1, 'SSH'
    HTTP = 2, 'HTTP(S)'
    DISCOVERY = 3, 'Discovery'
