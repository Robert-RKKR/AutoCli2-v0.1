# Django import:
from django.urls import path

# Base default route import:
from autocli2.base.api.base_default_router import BaseDefaultRouter

# Celery related view import:
from .view.celery import get_celery_registered_tasks
from .view.celery import get_celery_scheduled_tasks
from .view.celery import get_celery_reserved_tasks
from .view.celery import get_celery_revoked_tasks
from .view.celery import get_celery_report
from .view.celery import get_celery_stats

# Task related view import:
from .view.tasks import get_task_status

# Register router:
router = BaseDefaultRouter()

# URLs registration:
urlpatterns = [
    # Register task related view:
    path('task_status/<str:task_id>', get_task_status, name='task_status'),

    # Register celery related view:
    path('celery_registered_tasks', get_celery_registered_tasks, name='celery_registered_tasks'),
    path('celery_scheduled_tasks', get_celery_scheduled_tasks, name='celery_scheduled_tasks'),
    path('celery_reserved_tasks', get_celery_reserved_tasks, name='celery_reserved_tasks'),
    path('celery_revoked_tasks', get_celery_revoked_tasks, name='celery_revoked_tasks'),
    path('celery_report', get_celery_report, name='celery_report'),
    path('celery_stats', get_celery_stats, name='celery_stats'),
]

# Celery documentation:
# https://docs.celeryq.dev/en/stable/reference/celery.app.control.html
