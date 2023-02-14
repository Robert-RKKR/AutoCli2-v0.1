# Rest framework import:
from rest_framework.serializers import HyperlinkedIdentityField

# Base serializer import:
from autocli2.base.api.base_serializer import BaseSerializer

# Model import:
from ...models.host import Host

# Other serializer import:



# Main serializer class:
class HostSerializer(BaseSerializer):

    # Object URL definition:
    url = HyperlinkedIdentityField(
        view_name='api-inventory:host-detail',
        read_only=False,
    )

    class Meta:

        model = Host
        fields = BaseSerializer.base_fields + [
            'name',
            'description',
            'hostname',
        ]
        read_only_fields = BaseSerializer.base_read_only_fields



# Simple serializer class:
class HostSimpleSerializer(BaseSerializer):

    # Object URL definition:
    url = HyperlinkedIdentityField(
        view_name='api-inventory:host-detail',
        read_only=False,
    )
    # Object relation definition:

    class Meta:

        model = Host
        fields = BaseSerializer.base_fields + [
            'name',
            'description',
            'hostname',
        ]
        read_only_fields = BaseSerializer.base_read_only_fields
