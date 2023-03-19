# AutoCli2 - base filter import:
from autocli2.base.filters.base_filter import BaseFilter

# AutoCli2 - inventory model import:
from inventory.models.region import Region


# Filters:
class RegionFilter(BaseFilter):

    class Meta:

        model = Region
        fields = {
            'is_active': ['exact'],
            'is_root': ['exact'],
            'created': ['exact', 'icontains', 'lt', 'gt'],
            'updated': ['exact', 'icontains', 'lt', 'gt'],
            'name': ['exact', 'icontains'],
            'description': ['exact', 'icontains'],
            'code': ['exact', 'icontains']
        }
