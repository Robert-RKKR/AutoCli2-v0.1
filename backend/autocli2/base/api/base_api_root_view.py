# Rest framework - import:
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.views import APIView


# Base API root view:
class APIRootView(APIView):
    """
    This is the root of AutoCLI REST API.
    """
    _ignore_model_permissions = True
    exclude_from_schema = True
    swagger_schema = None

    def get_view_name(self):
        return "API Root"

    def get(self, request, format=None):

        return Response({
            'task': reverse('api-task:api-root', request=request, format=format),
            'inventory': reverse('api-inventory:api-root', request=request, format=format),
        })
