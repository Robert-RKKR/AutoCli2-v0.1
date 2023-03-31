# Django - user model import:
from django.contrib.auth.models import User

# AutoCli2 - base pagination import:
from autocli2.base.api.base_pagination import BaseSmallPaginator

# AutoCli2 - base view set import:
from autocli2.base.api.base_model_viewset import BaseRwModelViewSet

# AutoCli2 - serializer import:
from management.api.serializers.administrator import AdministratorSerializer


# ViewSet model classes:
class AdministratorView(BaseRwModelViewSet):
    """
    A ViewSet for viewing and editing object/s.
    """

    # Log changes:
    log_changes = True
    # Basic API view parameters:
    queryset = User.objects.all().order_by('pk')
    pagination_class = BaseSmallPaginator
    # Serializer classes:
    serializer_class = AdministratorSerializer
    # Django rest framework filters:
    ordering_fields = '__all__'
    search_fields = '__all__'
