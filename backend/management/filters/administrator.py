# AutoCli2 - base filter import:
from autocli2.base.filters.base_filter import BaseFilter

# AutoCli2 - management model import:
from management.models.administrator import Administrator


# Filters:
class AdministratorFilter(BaseFilter):

    class Meta:

        model = Administrator
        fields = {
            'username': ['exact', 'icontains'],
            'first_name': ['exact', 'icontains'],
            'last_name': ['exact', 'icontains'],
            'email': ['exact', 'icontains'],
            'is_staff': ['exact'],
            'is_active': ['exact'],
            'is_superuser': ['exact'],
            'date_joined': ['exact', 'icontains', 'lt', 'gt']
        }
