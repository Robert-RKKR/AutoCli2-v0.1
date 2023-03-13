# Django - url import:
from django.urls import path

# AutoCli2 - notification consumers import:
from notification.consumers import NotificationConsumer

ws_urlpatterns = [
    path('ws/notification/', NotificationConsumer.as_asgi()),
]