# Django - user model import:
from django.contrib.auth.models import User

# Rest framework - serializer import:
from rest_framework.serializers import HyperlinkedIdentityField

# AutoCli2 - base serializer import:
from autocli2.base.api.base_serializer import BaseSerializer


# Main serializer class:
class AdministratorSerializer(BaseSerializer):

    # Object URL definition:
    url = HyperlinkedIdentityField(
        view_name='api-management:administrator-detail',
        read_only=False
    )

    class Meta:

        model = User
        fields = [
            # Base values:
            'pk',
            'url',
            # Base administrator values:
            'username',
            'email',
        ]
        extra_kwargs = {'password': {'write_only': True}}
