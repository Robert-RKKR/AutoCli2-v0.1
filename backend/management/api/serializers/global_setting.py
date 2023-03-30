# Rest framework - serializer import:
from rest_framework.serializers import HyperlinkedIdentityField

# AutoCli2 - base serializer import:
from autocli2.base.api.base_serializer import BaseSerializer

# AutoCli2 - management model import:
from management.models.global_setting import GlobalSetting

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
    # Status related values:
    'is_current',
    # Settings related values:
    'notification_level',
    'logger_level',
    'default_user',
    'default_password',
    'http_timeout',
    'ssh_timeout',
]
read_only_fields = [
    # Base values:
    'pk',
]


# Main serializer class:
class GlobalSettingSerializer(BaseSerializer):

    # Object URL definition:
    url = HyperlinkedIdentityField(
        view_name='api-management:global-setting-detail',
        read_only=False
    )

    class Meta:

        model = GlobalSetting
        fields = fields
        read_only_fields = read_only_fields
