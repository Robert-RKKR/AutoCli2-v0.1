# AutoCli2 - base route import:
from autocli2.base.api.base_default_router import BaseDefaultRouter

# AutoCli2 - root view import:
from executor.api.view_sets.root import TaskRootView

# AutoCli2 - celery related view import:
from executor.api.task_views.celery import CeleryRegisteredTasksView
from executor.api.task_views.celery import CeleryScheduledView
from executor.api.task_views.celery import CeleryReservedView
from executor.api.task_views.celery import CeleryRevokedView
from executor.api.task_views.celery import CeleryReportView
from executor.api.task_views.celery import CeleryStatsView

# AutoCli2 - task related view import:
from executor.api.task_views.tasks import TaskStatusView

# Register router:
router = BaseDefaultRouter()

# App name registration:
app_name = 'api-task'

# Root api view route registration:
router.APIRootView = TaskRootView

# Celery view route registration:
router.register(r'celery_registered_tasks', CeleryRegisteredTasksView, basename='celery_registered_tasks')
router.register(r'celery_scheduled', CeleryScheduledView, basename='celery_scheduled')
router.register(r'celery_reserved', CeleryReservedView, basename='celery_reserved')
router.register(r'celery_revoked', CeleryRevokedView, basename='celery_revoked')
router.register(r'celery_report', CeleryReportView, basename='celery_report')
router.register(r'celery_stats', CeleryStatsView, basename='celery_stats')

# Task view route registration:
router.register(r'task_status', TaskStatusView, basename='task_status')

# Add urlpatterns:
urlpatterns = router.urls

# Celery documentation:
# https://docs.celeryq.dev/en/stable/reference/celery.app.control.html
