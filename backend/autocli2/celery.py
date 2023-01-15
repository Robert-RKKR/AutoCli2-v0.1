# Python import:
import os

# Celery import:
from celery import Celery

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'autocli2.settings')
app = Celery('autocli2')

# Celery settings are in settings.py using a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()
# Change default queue name:
app.conf.task_default_queue = 'default'
