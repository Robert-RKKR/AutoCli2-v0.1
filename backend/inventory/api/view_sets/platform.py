# AutoCli2 - base pagination import:
from autocli2.base.api.base_pagination import BaseSmallPaginator

# AutoCli2 - base view set import:
from autocli2.base.api.base_model_viewset import BaseRwModelViewSet

# AutoCli2 - serializer import:
from inventory.api.serializers.platform import PlatformSerializer

# AutoCli2 - inventory model import:
from inventory.models.platform import Platform

# AutoCli2 - inventory filter import:
from inventory.filters.platform import PlatformFilter


# ViewSet model classes:
class PlatformView(BaseRwModelViewSet):
    """
    A ViewSet for viewing and editing object/s.
    """

    # Log changes:
    log_changes = True
    # Basic API view parameters:
    queryset = Platform.objects.all().order_by('pk')
    pagination_class = BaseSmallPaginator
    # Serializer classes:
    serializer_class = PlatformSerializer
    # Django rest framework filters:
    filterset_class = PlatformFilter
    ordering_fields = '__all__'
    search_fields = '__all__'
