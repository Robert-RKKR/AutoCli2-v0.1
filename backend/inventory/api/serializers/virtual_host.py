# Rest framework - serializer import:
from rest_framework.serializers import HyperlinkedIdentityField
from rest_framework.serializers import PrimaryKeyRelatedField

# AutoCli2 - base serializer import:
from autocli2.base.api.base_serializer import BaseSerializer

# AutoCli2 - inventory serializers import:
from inventory.api.serializers.host import CredentialSerializer

# AutoCli2 - inventory model import:
from inventory.models.virtual_host import VirtualHost
from inventory.models.host import Host

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
    'host',
    # Object related values:
    'virtual_host_name',
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


# Main serializer class:
class HostSerializer(BaseSerializer):

    # Object URL definition:
    url = HyperlinkedIdentityField(
        view_name='api-inventory:virtual-host-detail',
        read_only=False,
        help_text='URL to provided object.',
    )

    # Object relation definition:
    host = PrimaryKeyRelatedField(
        queryset=Host.objects.all(),
        required=False,
        allow_null=True,
        help_text=VirtualHost.site.field.help_text,
    )

    class Meta:

        model = VirtualHost
        fields = fields
        read_only_fields = read_only_fields


# Full serializer class:
class HostFullSerializer(BaseSerializer):

    # Object URL definition:
    url = HyperlinkedIdentityField(
        view_name='api-inventory:virtual-host-detail',
        read_only=False
    )
    
    # Object relation definition:
    host = HostSerializer(
        many=False,
        read_only=True,
    )

    class Meta:

        model = VirtualHost
        fields = fields
        read_only_fields = read_only_fields
