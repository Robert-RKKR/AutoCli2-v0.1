# AutoCli2 - base filter import:
# AutoCli2 - base filter import:
from autocli2.base.filters.base_filter import BaseFilter

# AutoCli2 - notification model import:
from notification.models.change_log import ChangeLog


# Filters:
class ChangeLogFilter(BaseFilter):

    class Meta:

        model = ChangeLog
        fields = {
            'timestamp': ['exact', 'icontains', 'lt', 'gt'],
            'administrator': ['exact'],
            'action_type': ['exact', 'icontains'],
            'app_name': ['exact', 'icontains'],
            'model_name': ['exact', 'icontains'],
            'object_id': ['exact', 'icontains'],
            'object_representation': ['exact', 'icontains'],
            'execution_time': ['exact', 'icontains'],
        }
