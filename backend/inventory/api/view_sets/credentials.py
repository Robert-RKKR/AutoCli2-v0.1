# AutoCli2 - base pagination import:
from autocli2.base.api.base_pagination import BaseSmallPaginator

# AutoCli2 - base view set import:
from autocli2.base.api.base_model_viewset import BaseRwModelViewSet
from autocli2.base.api.base_model_viewset import BaseRoModelViewSet

# AutoCli2 - serializer import:
from inventory.api.serializers.credentials import CredentialFullSerializer
from inventory.api.serializers.credentials import CredentialSerializer

# AutoCli2 - inventory model import:
from inventory.models.credentials import Credential

# AutoCli2 - inventory filter import:
from inventory.filters.credentials import CredentialFilter

# AutoCli2 - base model mixin import:
from autocli2.base.api.base_model_mixin import BaseCreateModelMixin


class CredentialView(BaseRwModelViewSet):
    """
    A ViewSet for viewing and editing object/s.
    """

    # Log changes:
    log_changes = True
    # Basic API view parameters:
    queryset = Credential.objects.all().order_by('pk')
    pagination_class = BaseSmallPaginator
    # Serializer classes:
    serializer_class = CredentialSerializer
    # Django rest framework filters:
    filterset_class = CredentialFilter
    ordering_fields = '__all__'
    search_fields = '__all__'

    # Overwrite create method to add many serializer functionality:
    def create(self, request, *args, **kwargs):
        # Add administrator value to request data:
        request.data['administrator'] = request.user.pk
        # Continue execution of create function:
        return BaseCreateModelMixin.create(self, request, *args, **kwargs)


# ViewSet model classes:
class CredentialFullView(BaseRoModelViewSet):
    """
    A full ViewSet for viewing and editing object/s.
    """

    # Log changes:
    log_changes = True
    # Execute API view from Swagger schema:
    exclude_from_schema = True
    swagger_schema = None
    # Basic API view parameters:
    queryset = Credential.objects.all().order_by('pk')
    pagination_class = BaseSmallPaginator
    # Serializer classes:
    serializer_class = CredentialFullSerializer
    single_serializer_class = CredentialSerializer
    # Django rest framework filters:
    filterset_class = CredentialFilter
    ordering_fields = '__all__'
    search_fields = '__all__'
