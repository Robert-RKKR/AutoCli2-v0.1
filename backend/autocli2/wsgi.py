# Python - library import:
import os

# Django - wsgi import:
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'autocli2.settings')
application = get_wsgi_application()
