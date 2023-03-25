# Rest framework - serializer import:
from rest_framework.serializers import HyperlinkedIdentityField
from rest_framework.serializers import PrimaryKeyRelatedField

# AutoCli2 - base serializer import:
from autocli2.base.api.base_serializer import BaseSerializer

# AutoCli2 - inventory model import:
from inventory.models.credentials import Credential

# AutoCli2 - management model import:
from management.models.administrator import Administrator

# AutoCli2 - management serializers import:
from management.api.serializers.administrator import AdministratorSerializer

# Fields and read only fields:
fields = [
    # Base values:
    'pk',
    'url',
    # Status related values:
    'is_active',
    'is_root',
    # Data time related values:
    'created',
    'updated',
    # Identification related values:
    'name',
    'slug',
    'description',
    # Object related relations values:
    'administrator',
    # Object related values:
    'is_global',
    'username',
    'password',
    'token',
]
read_only_fields = [
    # Base values:
    'pk',
    'url',
    # Status related values:
    'is_root',
    'created',
    'updated',
    # Identification related values:
    'slug',
]


# Full serializer class:
class CredentialFullSerializer(BaseSerializer):

    # Object URL definition:
    url = HyperlinkedIdentityField(
        view_name='api-inventory:credential-detail',
        read_only=False
    )

    # Object relation definition:
    administrator = AdministratorSerializer(
        many=False,
        read_only=True,
    )

    class Meta:

        model = Credential
        fields = fields
        read_only_fields = read_only_fields


# Main serializer class:
class CredentialSerializer(BaseSerializer):

    # Object URL definition:
    url = HyperlinkedIdentityField(
        view_name='api-inventory:credential-detail',
        read_only=False,
    )

    # Object relation definition:
    administrator = PrimaryKeyRelatedField(
        queryset=Administrator.objects.all(),
        required=False,
        allow_null=True,
        help_text=Credential.administrator.field.help_text,
    )

    class Meta:

        model = Credential
        fields = fields
        read_only_fields = read_only_fields
