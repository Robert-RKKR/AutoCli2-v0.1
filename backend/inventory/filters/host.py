# AutoCli2 - base filter import:
from autocli2.base.filters.base_filter import BaseFilter

# AutoCli2 - inventory model import:
from inventory.models.host import Host


# Filters:
class HostFilter(BaseFilter):

    class Meta:

        model = Host
        fields = {
            'is_active': ['exact'],
            'is_root': ['exact'],
            'created': ['exact', 'icontains', 'lt', 'gt'],
            'updated': ['exact', 'icontains', 'lt', 'gt'],
            'name': ['exact', 'icontains'],
            'description': ['exact', 'icontains'],
            'hostname': ['exact', 'icontains'],
            'data_collection_protocol': ['exact'],
            'ssh_port': ['exact', 'icontains', 'lt', 'gt'],
            'http_port': ['exact', 'icontains', 'lt', 'gt'],
            'certificate_check': ['exact'],
        }
