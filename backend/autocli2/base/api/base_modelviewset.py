# Rest framework import:
from rest_framework import viewsets
from rest_framework import mixins

# Rest framework import:
from rest_framework.authentication import SessionAuthentication
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import DjangoModelPermissions
from rest_framework.filters import OrderingFilter
from rest_framework.filters import SearchFilter

# Django rest framework filters import:
from django_filters.rest_framework import DjangoFilterBackend


# Base ModelViewSet model:
class BaseModelViewSet(viewsets.ModelViewSet):
    """
    Base ModelViewSet model.
    """

    # Authentication and permissions:
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [DjangoModelPermissions]

    # Django rest framework filters:
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    base_search_fields = ['id']
    base_ordering_fields = ['id', 'created', 'updated', 'active', 'root']

    def get_own_serializer_class(self, many=True):

        # Collect class:
        if many:
            return self.serializer_class
        else:
            try:
                # Try to collect single serializer class:
                return self.single_serializer_class
            except:
                # use default serializer class:
                return self.serializer_class

    # overwrite create method to add many serializer functionality:
    def create(self, *args, **kwargs):
        self.serializer_class = self.get_own_serializer_class(many=False)
        return viewsets.ModelViewSet.create(self, *args, **kwargs)

    # overwrite update method to add many serializer functionality:
    def update(self, *args, **kwargs):
        self.serializer_class = self.get_own_serializer_class(many=False)
        return viewsets.ModelViewSet.update(self, *args, **kwargs)

    # overwrite list method to add many serializer functionality:
    def list(self, *args, **kwargs):
        self.serializer_class = self.get_own_serializer_class(many=True)
        return viewsets.ModelViewSet.list(self, *args, **kwargs)

    # overwrite retrieve method to add many serializer functionality:
    def retrieve(self, *args, **kwargs):
        self.serializer_class = self.get_own_serializer_class(many=True)
        return viewsets.ModelViewSet.retrieve(self, *args, **kwargs)


# Read only Base ModelViewSet model:
class BaseRoModelViewSet(
    viewsets.GenericViewSet,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    mixins.ListModelMixin):
    """
    Base Read only ModelViewSet model.
    """
    # Authentication and permissions:
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [DjangoModelPermissions]

    # Django rest framework filters:
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    base_search_fields = ['id']
    base_ordering_fields = ['id', 'created', 'updated', 'active', 'root']
