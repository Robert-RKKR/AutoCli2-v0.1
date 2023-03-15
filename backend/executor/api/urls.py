# Django - models import:
from django.urls import path

# AutoCli2 - base route import:
from autocli2.base.api.base_default_router import BaseDefaultRouter

# AutoCli2 - celery related view import:
from executor.api.task_views.celery import CeleryRegisteredTasks
from executor.api.task_views.celery import get_celery_scheduled_tasks
from executor.api.task_views.celery import get_celery_reserved_tasks
from executor.api.task_views.celery import get_celery_revoked_tasks
from executor.api.task_views.celery import get_celery_report
from executor.api.task_views.celery import get_celery_stats

# AutoCli2 - task related view import:
from executor.api.task_views.tasks import get_task_status

# Register default router:
router = BaseDefaultRouter()





# AutoCli2 - base route import:
from autocli2.base.api.base_default_router import BaseDefaultRouter

# AutoCli2 - root view import:
from executor.api.view_sets.root import TaskRootView

# Register router:
router = BaseDefaultRouter()

# App name registration:
app_name = 'api-task'

# Root api view route registration:
router.APIRootView = TaskRootView

# Standard view route registration:
router.register(r'celery_registered_tasks', CeleryRegisteredTasks, basename='celery_registered_tasks')

# Add urlpatterns:
urlpatterns = router.urls

# URLs registration:
# urlpatterns = [
#     # Register task related view:
#     path('task_status/<str:task_id>', get_task_status, name='task_status'),

#     # Register celery related view:
#     path('celery_registered_tasks', get_celery_registered_tasks, name='celery_registered_tasks'),
#     path('celery_scheduled_tasks', get_celery_scheduled_tasks, name='celery_scheduled_tasks'),
#     path('celery_reserved_tasks', get_celery_reserved_tasks, name='celery_reserved_tasks'),
#     path('celery_revoked_tasks', get_celery_revoked_tasks, name='celery_revoked_tasks'),
#     path('celery_report', get_celery_report, name='celery_report'),
#     path('celery_stats', get_celery_stats, name='celery_stats'),
# ]

# Celery documentation:
# https://docs.celeryq.dev/en/stable/reference/celery.app.control.html
