# Django import:
from django.apps import AppConfig


# App class:
class ManagementConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'management'

    def ready(self):
        import management.signals
