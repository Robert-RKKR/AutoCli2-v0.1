# AutoCli2 - base pagination import:
from autocli2.base.api.base_pagination import BaseSmallPaginator

# AutoCli2 - base view set import:
from autocli2.base.api.base_model_viewset import BaseRwModelViewSet

# AutoCli2 - serializer import:
from inventory.api.serializers.region import RegionSerializer

# AutoCli2 - inventory model import:
from inventory.models.region import Region

# AutoCli2 - inventory filter import:
from inventory.filters.region import RegionFilter


# ViewSet model classes:
class RegionView(BaseRwModelViewSet):
    """
    A ViewSet for viewing and editing object/s.
    """

    # Log changes:
    log_changes = True
    # Basic API view parameters:
    queryset = Region.objects.all().order_by('pk')
    pagination_class = BaseSmallPaginator
    # Serializer classes:
    serializer_class = RegionSerializer
    # Django rest framework filters:
    filterset_class = RegionFilter
    ordering_fields = '__all__'
    search_fields = '__all__'
