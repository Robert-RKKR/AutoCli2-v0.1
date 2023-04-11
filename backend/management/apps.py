# Django - models import:
from django.apps import AppConfig


# App class:
class ManagementConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'management'
