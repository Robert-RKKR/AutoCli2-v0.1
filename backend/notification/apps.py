# Django - application import:
from django.apps import AppConfig


# App class:
class NotificationConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'notification'

    # def ready(self):
    #     import notification.signals
