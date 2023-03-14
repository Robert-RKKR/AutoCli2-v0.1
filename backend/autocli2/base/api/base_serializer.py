# Rest framework - serializers import:
from rest_framework import serializers


# Base serializer class:
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
