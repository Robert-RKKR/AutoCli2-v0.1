# AutoCli2 - base pagination import:
# AutoCli2 - base pagination import:
from autocli2.base.api.base_pagination import BaseSmallPaginator

# AutoCli2 - base view set import:
from autocli2.base.api.base_model_viewset import BaseRoPlusModelViewSet

# AutoCli2 - serializer import:
from management.api.serializers.global_settings import GlobalSettingsSerializer

# AutoCli2 - management model import:
from management.models.global_settings import GlobalSettings

# AutoCli2 - inventory filter import:
from management.filters.global_settings import GlobalSettingsFilter


# ViewSet model classes:
class GlobalSettingsView(BaseRoPlusModelViewSet):
    """
    A ViewSet for viewing and editing object/s.
    """

    # Log changes:
    log_changes = True
    # Basic API view parameters:
    queryset = GlobalSettings.objects.all().order_by('pk')
    pagination_class = BaseSmallPaginator
    # Serializer classes:
    serializer_class = GlobalSettingsSerializer
    # Django rest framework filters:
    filterset_class = GlobalSettingsFilter
    ordering_fields = '__all__'
    search_fields = '__all__'
