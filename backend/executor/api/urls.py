# Django import:
from django.urls import path

# Base default route import:
from autocli2.base.api.base_default_router import BaseDefaultRouter

# View import:
from .view.task_status import get_task_status

# Register router:
router = BaseDefaultRouter()

# URLs registration:
urlpatterns = [
    path('task_status/<str:task_id>', get_task_status, name='task_status'),
]
