# Django - application import:
from django.apps import AppConfig


# App class:
class ExecutorConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'executor'
