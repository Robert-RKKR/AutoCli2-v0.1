# Rest framework - serializer import:
from rest_framework.serializers import HyperlinkedIdentityField
from rest_framework.serializers import PrimaryKeyRelatedField

# AutoCli2 - base serializer import:
from autocli2.base.api.base_serializer import BaseSerializer

# AutoCli2 - inventory serializers import:
from inventory.api.serializers.credentials import CredentialSimpleSerializer
from inventory.api.serializers.platform import PlatformSimpleSerializer
from inventory.api.serializers.site import SiteSimpleSerializer

# AutoCli2 - inventory model import:
from inventory.models.credentials import Credential
from inventory.models.platform import Platform
from inventory.models.site import Site
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
    'site',
    'platform',
    'credential',
    # Object related values:
    'hostname',
    'data_collection_protocol',
    'ssh_port',
    'http_port',
    'certificate_check'
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
        view_name='api-inventory:host-detail',
        read_only=False
    )
    # Object relation definition:
    site = SiteSimpleSerializer(
        many=False,
        read_only=True,
    )
    platform = PlatformSimpleSerializer(
        many=False,
        read_only=True,
    )
    credential = CredentialSimpleSerializer(
        many=False,
        read_only=True,
    )

    class Meta:

        model = Host
        fields = fields
        read_only_fields = read_only_fields


# Simple serializer class:
class HostSimpleSerializer(BaseSerializer):

    # Object URL definition:
    url = HyperlinkedIdentityField(
        view_name='api-inventory:host-detail',
        read_only=False,
        help_text='URL to provided object.',
    )
    # Object relation definition:
    site = PrimaryKeyRelatedField(
        queryset=Site.objects.all(),
        required=False,
        allow_null=True,
        help_text=Host.site.field.help_text,
    )
    platform = PrimaryKeyRelatedField(
        queryset=Platform.objects.all(),
        required=False,
        allow_null=True,
        help_text=Host.platform.field.help_text,
    )
    credential = PrimaryKeyRelatedField(
        queryset=Credential.objects.all(),
        required=False,
        allow_null=True,
        help_text=Host.credential.field.help_text,
    )

    class Meta:

        model = Host
        fields = fields
        read_only_fields = read_only_fields
