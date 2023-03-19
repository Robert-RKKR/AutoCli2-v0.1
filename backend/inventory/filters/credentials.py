# AutoCli2 - base filter import:
from autocli2.base.filters.base_filter import BaseFilter

# AutoCli2 - inventory model import:
from inventory.models.credentials import Credential


# Filters:
class CredentialFilter(BaseFilter):

    class Meta:

        model = Credential
        fields = {
            'is_active': ['exact'],
            'is_root': ['exact'],
            'created': ['exact', 'icontains', 'lt', 'gt'],
            'updated': ['exact', 'icontains', 'lt', 'gt'],
            'name': ['exact', 'icontains'],
            'description': ['exact', 'icontains'],
            'is_global': ['exact'],
            'username': ['exact', 'icontains']
        }
