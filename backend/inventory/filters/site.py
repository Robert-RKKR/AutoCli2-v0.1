# AutoCli2 - base filter import:
from autocli2.base.filters.base_filter import BaseFilter

# AutoCli2 - inventory model import:
from inventory.models.site import Site


# Filters:
class SiteFilter(BaseFilter):

    class Meta:

        model = Site
        fields = {
            'is_active': ['exact'],
            'is_root': ['exact'],
            'created': ['exact', 'icontains', 'lt', 'gt'],
            'updated': ['exact', 'icontains', 'lt', 'gt'],
            'name': ['exact', 'icontains'],
            'description': ['exact', 'icontains'],
            'code': ['exact', 'icontains'],
            'gps_coordinates': ['exact', 'icontains'],
            'physical_address': ['exact', 'icontains']
        }
