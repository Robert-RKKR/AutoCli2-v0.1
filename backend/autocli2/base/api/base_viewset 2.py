# Django - models import:
from django.http import JsonResponse

# Rest framework - view import:
from rest_framework.viewsets import ViewSet

# Rest framework - authentication & permissions import:
from rest_framework.authentication import SessionAuthentication
from rest_framework.authentication import TokenAuthentication
from rest_framework import permissions


# Base celery views classes:
class BaseListViewSet(ViewSet):
    """
    Base viewset class.
    """
    
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [permissions.IsAdminUser]

    def collect_data(self):
        raise NotImplementedError

    def list(self, request, format=None):
        """
        Description.
        """

        # Collect data:
        collected_data = self.collect_data()
        # Prepare results:
        result = {
            'page_results': collected_data}
        # Prepare API response:
        return JsonResponse(result, status=200)


class BaseRetrieveViewSet(ViewSet):
    """
    Base viewset class.
    """
    
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [permissions.IsAdminUser]

    def collect_data(self, pk):
        raise NotImplementedError
    
    def retrieve(self, request, pk=None):
        """
        Description.
        """

        # Collect data:
        collected_data = self.collect_data(pk)
        # Prepare results:
        result = {
            'page_results': collected_data}
        # Prepare API response:
        return JsonResponse(result, status=200) 
