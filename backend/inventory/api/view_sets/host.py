# AutoCli2 - base pagination import:
from autocli2.base.api.base_pagination import BaseSmallPaginator

# AutoCli2 - base view set import:
from autocli2.base.api.base_model_viewset import BaseRwModelViewSet

# AutoCli2 - serializer import:
from inventory.api.serializers.host import HostSimpleSerializer
from inventory.api.serializers.host import HostSerializer

# AutoCli2 - inventory model import:
from inventory.models.host import Host

# AutoCli2 - inventory filter import:
from inventory.filters.host import HostFilter

# Ordering and search values:
ordering_fields = [
    'id', 'name', 'description', 'ico', 'created', 'updated',
     'is_root', 'is_active']
search_fields = [
    'id', 'name', 'description', 'created', 'updated']





# ViewSet model classes:
class HostView(BaseRwModelViewSet):
    """
    A ViewSet for viewing and editing object/s.
    """
    # Basic API view parameters:
    queryset = Host.objects.all()
    pagination_class = BaseSmallPaginator
    # Serializer classes:
    serializer_class = HostSerializer
    single_serializer_class = HostSimpleSerializer
    # Django rest framework filters:
    filterset_class = HostFilter
    ordering_fields = ordering_fields
    search_fields = search_fields


class HostSimpleView(BaseRwModelViewSet):
    """
    A simple ViewSet for viewing and editing object/s.
    """
    # Execute API view from Swagger schema:
    exclude_from_schema = True
    swagger_schema = None
    # Basic API view parameters:
    queryset = Host.objects.all()
    pagination_class = BaseSmallPaginator
    # Serializer classes:
    serializer_class = HostSimpleSerializer
    # Django rest framework filters:
    filterset_class = HostFilter
    ordering_fields = ordering_fields
    search_fields = search_fields
