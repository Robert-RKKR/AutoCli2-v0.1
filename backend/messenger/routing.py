# Django import:
from django.urls import path

# Application import:
from .consumers import NotificationConsumer

ws_urlpatterns = [
    path('ws/notification/', NotificationConsumer.as_asgi()),
]