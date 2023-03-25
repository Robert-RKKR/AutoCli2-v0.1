# Django - application import:
from django.apps import AppConfig

# AutoCli2 - init function import:
from app_initiator.init import init_app_db


# App class:
class AppInitiatorConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app_initiator'

    def ready(self):
        # Create initial objects:
        init_app_db()
