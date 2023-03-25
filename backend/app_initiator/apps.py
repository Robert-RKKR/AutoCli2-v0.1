# Django - application import:
from django.apps import AppConfig


# App class:
class AppInitiatorConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app_initiator'

    def ready(self):
        # Import signals:
        import app_initiator.signals