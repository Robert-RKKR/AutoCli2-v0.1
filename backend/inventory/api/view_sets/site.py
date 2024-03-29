# AutoCli2 - base pagination import:
from autocli2.base.api.base_pagination import BaseSmallPaginator

# AutoCli2 - base view set import:
from autocli2.base.api.base_model_viewset import BaseRwModelViewSet
from autocli2.base.api.base_model_viewset import BaseRoModelViewSet

# AutoCli2 - serializer import:
from inventory.api.serializers.site import SiteFullSerializer
from inventory.api.serializers.site import SiteSerializer

# AutoCli2 - inventory model import:
from inventory.models.site import Site

# AutoCli2 - inventory filter import:
from inventory.filters.site import SiteFilter


class SiteView(BaseRwModelViewSet):
    """
    A ViewSet for viewing and editing object/s.
    """

    # Log changes:
    log_changes = True
    # Basic API view parameters:
    queryset = Site.objects.all().order_by('pk')
    pagination_class = BaseSmallPaginator
    # Serializer classes:
    serializer_class = SiteSerializer
    # Django rest framework filters:
    filterset_class = SiteFilter
    ordering_fields = '__all__'
    search_fields = '__all__'


# ViewSet model classes:
class SiteFullView(BaseRoModelViewSet):
    """
    A full ViewSet for viewing and editing object/s.
    """

    # Execute API view from Swagger schema:
    exclude_from_schema = True
    swagger_schema = None
    # Basic API view parameters:
    queryset = Site.objects.all().order_by('pk')
    pagination_class = BaseSmallPaginator
    # Serializer classes:
    serializer_class = SiteFullSerializer
    # Django rest framework filters:
    filterset_class = SiteFilter
    ordering_fields = '__all__'
    search_fields = '__all__'
