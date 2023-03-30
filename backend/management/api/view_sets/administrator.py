# Django - serializers import:
from django.core.serializers import serialize

# Rest framework - other imports:
from rest_framework.response import Response
from rest_framework import status

# Rest framework - exceptions import:
from rest_framework.exceptions import APIException

# AutoCli2 - base pagination import:
from autocli2.base.api.base_pagination import BaseSmallPaginator

# AutoCli2 - base view set import:
from autocli2.base.api.base_model_viewset import BaseRwModelViewSet

# AutoCli2 - serializer import:
from management.api.serializers.administrator import AdministratorSerializer

# AutoCli2 - management model import:
from management.models.administrator import Administrator

# AutoCli2 - inventory filter import:
from management.filters.administrator import AdministratorFilter

# AutoCli2 - constance import:
from autocli2.base.constants.action_type import ActionTypeChoices

# AutoCli2 - log change import:
from notification.log_change import log_change


# Administrator custom view set class:
class AdministratorViewSet(BaseRwModelViewSet):

    # Overwrite create method to add many serializer functionality:
    def create(self, *args, **kwargs):
        # Collect request:
        request = args[0]
        # Collect password value:
        password = request.data.get('password', False)
        email = request.data.get('email', '')
        username = request.data.get('username', False)
        other_data = {
            'first_name': request.data.get('first_name', False),
            'last_name': request.data.get('last_name', False),
            'api_token': request.data.get('api_token', False)}
        # Check if password was provided:
        if password:
            try: # Try to create superuser:
                instance = Administrator.objects.create_superuser(
                    username, email, password)
            except:
                # Raise API error:
                raise APIException('Server error.', 500)
            else:
                # Create change:
                log_change(instance, request.user, ActionTypeChoices.CREATE)
                # Return HTTP response 201, object was created:
                object_representation = serialize('json', [instance], use_natural_foreign_keys=True,)
                response = {
                    'page_results': object_representation}
                return Response(
                    response, status=status.HTTP_201_CREATED)
        else:
            # Raise API error if password wasn't provided:
            raise APIException('The password has not been provided.', 409)


# ViewSet model classes:
class AdministratorView(AdministratorViewSet):
    """
    A ViewSet for viewing and editing object/s.
    """

    # Log changes:
    log_changes = True
    # Basic API view parameters:
    queryset = Administrator.objects.all().order_by('pk')
    pagination_class = BaseSmallPaginator
    # Serializer classes:
    serializer_class = AdministratorSerializer
    # Django rest framework filters:
    filterset_class = AdministratorFilter
    ordering_fields = '__all__'
    search_fields = '__all__'
