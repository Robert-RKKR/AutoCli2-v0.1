# AutoCli2 - base pagination import:
# AutoCli2 - base pagination import:
from autocli2.base.api.base_pagination import BaseSmallPaginator

# AutoCli2 - base view set import:
from autocli2.base.api.base_model_viewset import BaseRwModelViewSet

# AutoCli2 - serializer import:
from management.api.serializers.global_setting import GlobalSettingSerializer

# AutoCli2 - management model import:
from management.models.global_setting import GlobalSetting

# AutoCli2 - inventory filter import:
from management.filters.global_setting import GlobalSettingFilter


# ViewSet model classes:
class GlobalSettingView(BaseRwModelViewSet):
    """
    A ViewSet for viewing and editing object/s.
    """

    # Log changes:
    log_changes = True
    # Basic API view parameters:
    queryset = GlobalSetting.objects.all().order_by('pk')
    pagination_class = BaseSmallPaginator
    # Serializer classes:
    serializer_class = GlobalSettingSerializer
    # Django rest framework filters:
    filterset_class = GlobalSettingFilter
    ordering_fields = '__all__'
    search_fields = '__all__'
