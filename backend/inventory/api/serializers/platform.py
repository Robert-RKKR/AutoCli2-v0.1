# Rest framework - serializer import:
from rest_framework.serializers import HyperlinkedIdentityField

# AutoCli2 - base serializer import:
from autocli2.base.api.base_serializer import BaseSerializer

# AutoCli2 - inventory model import:
from inventory.models.platform import Platform


# Main serializer class:
class PlatformSerializer(BaseSerializer):

    # Object URL definition:
    url = HyperlinkedIdentityField(
        view_name='api-inventory:platform-detail',
        read_only=False
    )

    class Meta:

        model = Platform
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
            # Supported protocols values:
            'is_http_supported',
            'is_ssh_supported',
            # HTTP(S) related values:
            'http_token_heder_key',
            'http_token_heder_value',
            'http_pagination',
            'http_next_page_code_path',
            'http_next_page_link_path',
            'http_pagination_param_key',
            'http_data_path',
            'http_default_header',
            'http_default_params',
            # SSH related values:
            'ssh_platform_type'
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
