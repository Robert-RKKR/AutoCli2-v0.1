# Rest framework - serializer import:
from rest_framework.serializers import HyperlinkedIdentityField

# AutoCli2 - base serializer import:
from autocli2.base.api.base_serializer import BaseSerializer

# AutoCli2 - inventory model import:
from inventory.models.region import Region


# Main serializer class:
class RegionSerializer(BaseSerializer):

    # Object URL definition:
    url = HyperlinkedIdentityField(
        view_name='api-inventory:region-detail',
        read_only=False
    )

    class Meta:

        model = Region
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
            'code',
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
