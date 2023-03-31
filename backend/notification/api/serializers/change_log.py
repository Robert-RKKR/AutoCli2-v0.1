# Rest framework - serializer import:
from rest_framework.serializers import HyperlinkedIdentityField

# AutoCli2 - base serializer import:
from autocli2.base.api.base_serializer import BaseSerializer

# AutoCli2 - notification model import:
from notification.models.change_log import ChangeLog

# AutoCli2 - management serializers import:
from management.api.serializers.administrator import AdministratorSerializer


# Full serializer class:
class ChangeLogFullSerializer(BaseSerializer):

    # Object URL definition:
    url = HyperlinkedIdentityField(
        view_name='api-notification:change-log-detail',
        read_only=False
    )

    # Object relation definition:
    administrator = AdministratorSerializer(
        many=False,
        read_only=True,
    )

    class Meta:

        model = ChangeLog
        fields = [
            # Base object values:
            'pk',
            'url',
            # Base notification values:
            'timestamp',
            'administrator',
            'action_type',
            'app_name',
            'model_name',
            'object_id',
            'object_representation',
            'execution_time',
            # Change log values:
            'after',
        ]
        read_only_fields = [
            # Base object values:
            'pk',
            'url',
            # Base notification values:
            'timestamp',
            'administrator',
            'action_type',
            'app_name',
            'model_name',
            'object_id',
            'object_representation',
            'execution_time',
            # Change log values:
            'after',
        ]
