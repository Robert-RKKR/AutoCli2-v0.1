# AutoCli2 - base pagination import:
from autocli2.base.api.base_pagination import BaseSmallPaginator

# AutoCli2 - base view set import:
from autocli2.base.api.base_modelviewset import BaseModelViewSet

# AutoCli2 - serializer import:
from inventory.api.serializers.host import HostSimpleSerializer
from inventory.api.serializers.host import HostSerializer

# Model import:
from inventory.models.host import Host


# ViewSet model classes:
class HostView(BaseModelViewSet):
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
    # filterset_class = DeviceFilter
    search_fields = BaseModelViewSet.base_search_fields + [
        'hostname',
    ]
    ordering_fields = BaseModelViewSet.base_ordering_fields + [
        'hostname',
    ]


class HostSimpleView(BaseModelViewSet):
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
    # filterset_class = DeviceFilter
    search_fields = BaseModelViewSet.base_search_fields + [
        'hostname',
    ]
    ordering_fields = BaseModelViewSet.base_ordering_fields + [
        'hostname',
    ]
