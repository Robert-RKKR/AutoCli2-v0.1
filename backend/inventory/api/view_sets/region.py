# AutoCli2 - base pagination import:
from autocli2.base.api.base_pagination import BaseSmallPaginator

# AutoCli2 - base view set import:
from autocli2.base.api.base_model_viewset import BaseRwModelViewSet

# AutoCli2 - serializer import:
from inventory.api.serializers.region import RegionSimpleSerializer
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

    # Basic API view parameters:
    queryset = Region.objects.all().order_by('pk')
    pagination_class = BaseSmallPaginator
    # Serializer classes:
    serializer_class = RegionSerializer
    single_serializer_class = RegionSimpleSerializer
    # Django rest framework filters:
    filterset_class = RegionFilter
    ordering_fields = '__all__'
    search_fields = '__all__'


class RegionSimpleView(BaseRwModelViewSet):
    """
    A simple ViewSet for viewing and editing object/s.
    """

    # Execute API view from Swagger schema:
    exclude_from_schema = True
    swagger_schema = None
    # Basic API view parameters:
    queryset = Region.objects.all().order_by('pk')
    pagination_class = BaseSmallPaginator
    # Serializer classes:
    serializer_class = RegionSimpleSerializer
    # Django rest framework filters:
    filterset_class = RegionFilter
    ordering_fields = '__all__'
    search_fields = '__all__'
