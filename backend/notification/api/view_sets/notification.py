# AutoCli2 - base pagination import:
from autocli2.base.api.base_pagination import BaseSmallPaginator

# AutoCli2 - base view set import:
from autocli2.base.api.base_model_viewset import BaseRoModelViewSet

# AutoCli2 - serializer import:
from notification.api.serializers.notification import NotificationFullSerializer

# AutoCli2 - notification filter import:
from notification.filters.notification import NotificationFilter

# AutoCli2 - notification model import:
from notification.models.notification import Notification


# ViewSet model classes:
class NotificationView(BaseRoModelViewSet):
    """
    A ViewSet for viewing and editing object/s.
    """

    # Log changes:
    log_changes = True
    # Basic API view parameters:
    queryset = Notification.objects.all().order_by('pk')
    pagination_class = BaseSmallPaginator
    # Serializer classes:
    serializer_class = NotificationFullSerializer
    # Django rest framework filters:
    filterset_class = NotificationFilter
    ordering_fields = '__all__'
    search_fields = '__all__'
