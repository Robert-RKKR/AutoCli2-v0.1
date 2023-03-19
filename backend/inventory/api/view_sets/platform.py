# AutoCli2 - base pagination import:
from autocli2.base.api.base_pagination import BaseSmallPaginator

# AutoCli2 - base view set import:
from autocli2.base.api.base_model_viewset import BaseRwModelViewSet

# AutoCli2 - serializer import:
from inventory.api.serializers.platform import PlatformSimpleSerializer
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

    # Basic API view parameters:
    queryset = Platform.objects.all()
    pagination_class = BaseSmallPaginator
    # Serializer classes:
    serializer_class = PlatformSerializer
    single_serializer_class = PlatformSimpleSerializer
    # Django rest framework filters:
    filterset_class = PlatformFilter
    ordering_fields = '__all__'
    search_fields = '__all__'


class PlatformSimpleView(BaseRwModelViewSet):
    """
    A simple ViewSet for viewing and editing object/s.
    """

    # Execute API view from Swagger schema:
    exclude_from_schema = True
    swagger_schema = None
    # Basic API view parameters:
    queryset = Platform.objects.all()
    pagination_class = BaseSmallPaginator
    # Serializer classes:
    serializer_class = PlatformSimpleSerializer
    # Django rest framework filters:
    filterset_class = PlatformFilter
    ordering_fields = '__all__'
    search_fields = '__all__'
