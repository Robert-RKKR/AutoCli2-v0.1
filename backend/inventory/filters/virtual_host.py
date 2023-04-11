# AutoCli2 - base filter import:
from autocli2.base.filters.base_filter import BaseFilter

# AutoCli2 - inventory model import:
from inventory.models.virtual_host import VirtualHost


# Filters:
class VirtualHostFilter(BaseFilter):

    class Meta:

        model = VirtualHost
        fields = {
            'is_active': ['exact'],
            'is_root': ['exact'],
            'created': ['exact', 'icontains', 'lt', 'gt'],
            'updated': ['exact', 'icontains', 'lt', 'gt'],
            'name': ['exact', 'icontains'],
            'description': ['exact', 'icontains'],
            'host': ['exact'],
            'virtual_host_name': ['exact', 'icontains'],
        }
