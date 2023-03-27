# Rest framework - serializer import:
from rest_framework.serializers import HyperlinkedIdentityField

# AutoCli2 - base serializer import:
from autocli2.base.api.base_serializer import BaseSerializer

# AutoCli2 - management model import:
from management.models.administrator import Administrator

# Fields and read only fields:
fields = [
    # Base values:
    'pk',
    'url',
    # Base administrator values:
    'username',
    'first_name',
    'last_name',
    'email',
    # Status related values:
    'is_staff',
    'is_active',
    'is_superuser',
    # Data time related values:
    'date_joined',
    # Custom administrator values:
    'api_token',
]
read_only_fields = [
    # Base values:
    'pk',
]


# Main serializer class:
class AdministratorSerializer(BaseSerializer):

    # Object URL definition:
    url = HyperlinkedIdentityField(
        view_name='api-management:administrator-detail',
        read_only=False
    )

    class Meta:

        model = Administrator
        fields = fields
        read_only_fields = read_only_fields
