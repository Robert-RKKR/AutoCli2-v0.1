# Rest framework - serializer import:
from rest_framework.serializers import HyperlinkedIdentityField

# AutoCli2 - base serializer import:
from autocli2.base.api.base_serializer import BaseSerializer

# AutoCli2 - inventory model import:
from inventory.models.platform import Platform

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
    # Object related values:
    'api_token_heder_key',
    'api_token_heder_value',
    'api_pagination',
    'api_next_page_code_path',
    'api_next_page_link_path',
    'api_pagination_param_key',
    'api_data_path',
    'api_default_header',
    'api_default_params',
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
class PlatformSerializer(BaseSerializer):

    # Object URL definition:
    url = HyperlinkedIdentityField(
        view_name='api-inventory:platform-detail',
        read_only=False
    )

    class Meta:

        model = Platform
        fields = fields
        read_only_fields = read_only_fields


# Simple serializer class:
class PlatformSimpleSerializer(BaseSerializer):

    # Object URL definition:
    url = HyperlinkedIdentityField(
        view_name='api-inventory:platform-detail',
        read_only=False
    )
    # Object relation definition:

    class Meta:

        model = Platform
        fields = fields
        read_only_fields = read_only_fields
