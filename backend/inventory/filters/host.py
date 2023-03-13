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
            'name': ['exact', 'icontains'],
            'description': ['exact', 'icontains'],
            'hostname': ['exact', 'icontains'],
            # 'ssh_port': ['exact', 'icontains', 'lt', 'gt'],
            # 'https_port': ['exact', 'icontains', 'lt', 'gt'],
            # 'device_type': ['exact'],
            # 'ssh_status': ['exact'],
            # 'https_status': ['exact'],
            # 'credential': ['exact'],
            # 'token': ['exact'],
            # 'certificate': ['exact'],
        }
