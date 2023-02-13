# Python import:
import os

# Django import:
from django.core.asgi import get_asgi_application

# Channels import:
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack

# Application import:
from notification.routing import ws_urlpatterns

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'autocli2.settings')
application = ProtocolTypeRouter({
    'http': get_asgi_application(),
    'websocket': AuthMiddlewareStack(URLRouter(ws_urlpatterns)),
})
