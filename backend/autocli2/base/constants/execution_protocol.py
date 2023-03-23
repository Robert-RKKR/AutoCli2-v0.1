from django.db.models import TextChoices

# Choices class:
class ExecutionProtocolChoices(TextChoices):

    # Empty value:
    __empty__ = 'Empty'

    # Choices values:
    HTTP = 'http', 'HTTP(S)'
    SSH = 'ssh', 'SSH'
    DISCOVERY = 'dsc', 'Discovery'
