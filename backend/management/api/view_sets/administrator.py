# AutoCli2 - base pagination import:
from autocli2.base.api.base_pagination import BaseSmallPaginator

# AutoCli2 - base view set import:
from autocli2.base.api.base_model_viewset import BaseRwModelViewSet

# AutoCli2 - serializer import:
from management.api.serializers.administrator import AdministratorSerializer

# AutoCli2 - management model import:
from management.models.administrator import Administrator

# AutoCli2 - inventory filter import:
from management.filters.administrator import AdministratorFilter


# ViewSet model classes:
class AdministratorView(BaseRwModelViewSet):
    """
    A ViewSet for viewing and editing object/s.
    """

    # Log changes:
    log_changes = True
    # Basic API view parameters:
    queryset = Administrator.objects.all().order_by('pk')
    pagination_class = BaseSmallPaginator
    # Serializer classes:
    serializer_class = AdministratorSerializer
    # Django rest framework filters:
    filterset_class = AdministratorFilter
    ordering_fields = '__all__'
    search_fields = '__all__'
