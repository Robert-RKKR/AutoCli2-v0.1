from django.db.models import TextChoices

# Choices class:
class ExecutionProtocolChoices(TextChoices):

    # Empty value:
    __empty__ = 'Empty'

    # Choices values:
    HTTP = 'HTTP', 'HTTP(S)'
    SSH = 'SSH', 'SSH'
    DISCOVERY = 'DS', 'Discovery'
