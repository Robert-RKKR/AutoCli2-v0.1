# AutoCli2 - base filter import:
from autocli2.base.filters.base_filter import BaseFilter

# AutoCli2 - notification model import:
from notification.models.notification import Notification


# Filters:
class NotificationFilter(BaseFilter):

    class Meta:

        model = Notification
        fields = {
            'timestamp': ['exact', 'icontains', 'lt', 'gt'],
            'administrator': ['exact'],
            'action_type': ['exact', 'icontains'],
            'app_name': ['exact', 'icontains'],
            'model_name': ['exact', 'icontains'],
            'object_id': ['exact', 'icontains'],
            'object_representation': ['exact', 'icontains'],
            'execution_time': ['exact', 'icontains', 'lt', 'gt'],
            'severity': ['exact'],
            'notification_type': ['exact'],
            'task_id': ['exact', 'icontains'],
            'application': ['exact', 'icontains'],
            'message': ['exact', 'icontains'],
        }
