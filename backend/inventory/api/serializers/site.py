# Rest framework - serializer import:
from rest_framework.serializers import HyperlinkedIdentityField
from rest_framework.serializers import PrimaryKeyRelatedField

# AutoCli2 - base serializer import:
from autocli2.base.api.base_serializer import BaseSerializer

# AutoCli2 - inventory serializers import:
from inventory.api.serializers.region import RegionSimpleSerializer

# AutoCli2 - inventory model import:
from inventory.models.region import Region
from inventory.models.site import Site

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
    'region',
    # Object related values:
    'code',
    'gps_coordinates',
    'physical_address',
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
class SiteSerializer(BaseSerializer):

    # Object URL definition:
    url = HyperlinkedIdentityField(
        view_name='api-inventory:site-detail',
        read_only=False
    )

    # Object relation definition:
    region = RegionSimpleSerializer(
        many=False,
        read_only=True,
    )

    class Meta:

        model = Site
        fields = fields
        read_only_fields = read_only_fields


# Simple serializer class:
class SiteSimpleSerializer(BaseSerializer):

    # Object URL definition:
    url = HyperlinkedIdentityField(
        view_name='api-inventory:site-detail',
        read_only=False,
    )
    
    # Object relation definition:
    region = PrimaryKeyRelatedField(
        queryset=Region.objects.all(),
        required=False,
        allow_null=True,
        help_text=Site.region.field.help_text,
    )

    class Meta:

        model = Site
        fields = fields
        read_only_fields = read_only_fields
