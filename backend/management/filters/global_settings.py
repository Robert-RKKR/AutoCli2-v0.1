# AutoCli2 - base filter import:
from autocli2.base.filters.base_filter import BaseFilter

# AutoCli2 - management model import:
from management.models.global_settings import GlobalSettings


# Filters:
class GlobalSettingsFilter(BaseFilter):

    class Meta:

        model = GlobalSettings
        fields = {
            'is_active': ['exact'],
            'is_root': ['exact'],
            'created': ['exact', 'icontains', 'lt', 'gt'],
            'updated': ['exact', 'icontains', 'lt', 'gt'],
            'name': ['exact', 'icontains'],
            'description': ['exact', 'icontains']
        }
