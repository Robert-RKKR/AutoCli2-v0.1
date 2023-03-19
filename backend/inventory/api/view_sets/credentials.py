# AutoCli2 - base pagination import:
from autocli2.base.api.base_pagination import BaseSmallPaginator

# AutoCli2 - base view set import:
from autocli2.base.api.base_model_viewset import BaseRwModelViewSet

# AutoCli2 - serializer import:
from inventory.api.serializers.credentials import CredentialSimpleSerializer
from inventory.api.serializers.credentials import CredentialSerializer

# AutoCli2 - inventory model import:
from inventory.models.credentials import Credential

# AutoCli2 - inventory filter import:
from inventory.filters.credentials import CredentialFilter


# ViewSet model classes:
class CredentialView(BaseRwModelViewSet):
    """
    A ViewSet for viewing and editing object/s.
    """

    # Basic API view parameters:
    queryset = Credential.objects.all()
    pagination_class = BaseSmallPaginator
    # Serializer classes:
    serializer_class = CredentialSerializer
    single_serializer_class = CredentialSimpleSerializer
    # Django rest framework filters:
    filterset_class = CredentialFilter
    ordering_fields = '__all__'
    search_fields = '__all__'


class CredentialSimpleView(BaseRwModelViewSet):
    """
    A simple ViewSet for viewing and editing object/s.
    """

    # Execute API view from Swagger schema:
    exclude_from_schema = True
    swagger_schema = None
    # Basic API view parameters:
    queryset = Credential.objects.all()
    pagination_class = BaseSmallPaginator
    # Serializer classes:
    serializer_class = CredentialSimpleSerializer
    # Django rest framework filters:
    filterset_class = CredentialFilter
    ordering_fields = '__all__'
    search_fields = '__all__'
