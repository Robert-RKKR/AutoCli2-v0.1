# AutoCli2 - base pagination import:
from autocli2.base.api.base_pagination import BaseSmallPaginator

# AutoCli2 - base view set import:
from autocli2.base.api.base_model_viewset import BaseRwModelViewSet

# AutoCli2 - serializer import:
from inventory.api.serializers.host import HostFullSerializer
from inventory.api.serializers.host import HostSerializer

# AutoCli2 - inventory model import:
from inventory.models.host import Host

# AutoCli2 - inventory filter import:
from inventory.filters.host import HostFilter


# ViewSet model classes:
class HostFullView(BaseRwModelViewSet):
    """
    A full ViewSet for viewing and editing object/s.
    """

    # Log changes:
    log_changes = True
    # Basic API view parameters:
    queryset = Host.objects.all().order_by('pk')
    pagination_class = BaseSmallPaginator
    # Serializer classes:
    serializer_class = HostFullSerializer
    single_serializer_class = HostSerializer
    # Django rest framework filters:
    filterset_class = HostFilter
    ordering_fields = '__all__'
    search_fields = '__all__'


class HostView(BaseRwModelViewSet):
    """
    A ViewSet for viewing and editing object/s.
    """

    # Log changes:
    log_changes = True
    # Execute API view from Swagger schema:
    exclude_from_schema = True
    swagger_schema = None
    # Basic API view parameters:
    queryset = Host.objects.all().order_by('pk')
    pagination_class = BaseSmallPaginator
    # Serializer classes:
    serializer_class = HostSerializer
    # Django rest framework filters:
    filterset_class = HostFilter
    ordering_fields = '__all__'
    search_fields = '__all__'
