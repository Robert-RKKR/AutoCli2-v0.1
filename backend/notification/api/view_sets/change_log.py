# AutoCli2 - base pagination import:
from autocli2.base.api.base_pagination import BaseSmallPaginator

# AutoCli2 - base view set import:
from autocli2.base.api.base_model_viewset import BaseRoModelViewSet

# AutoCli2 - serializer import:
from notification.api.serializers.change_log import ChangeLogFullSerializer

# AutoCli2 - notification filter import:
from notification.filters.change_log import ChangeLogFilter

# AutoCli2 - notification model import:
from notification.models.change_log import ChangeLog


# ViewSet model classes:
class ChangeLogView(BaseRoModelViewSet):
    """
    A ViewSet for viewing and editing object/s.
    """

    # Log changes:
    log_changes = True
    # Basic API view parameters:
    queryset = ChangeLog.objects.all().order_by('pk')
    pagination_class = BaseSmallPaginator
    # Serializer classes:
    serializer_class = ChangeLogFullSerializer
    # Django rest framework filters:
    filterset_class = ChangeLogFilter
    ordering_fields = '__all__'
    search_fields = '__all__'
