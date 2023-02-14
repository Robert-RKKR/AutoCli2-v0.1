# Rest framework import:
from rest_framework import serializers


# Base serializer:
class BaseSerializer(serializers.HyperlinkedModelSerializer):

    base_fields = [
        'pk',
        'url',
        'is_root',
        'created',
        'updated',
        'is_active',
    ]
    base_read_only_fields = [
        'pk',
        'url',
        'is_root',
        'created',
        'updated',
    ]
