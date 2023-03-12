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

# Base models import:
from autocli2.base.models.identification import IdentificationModel
from autocli2.base.models.administrator import AdministratorModel
from autocli2.base.models.data_time import DataTimeModel
from autocli2.base.models.status import StatusModel


from rest_framework.response import Response
from rest_framework import status

class DestroyModelMixin:
    """
    Destroy a model instance.
    """
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        response = self.perform_destroy(instance)
        if response:
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)

    def perform_destroy(self, instance):
        response = instance.delete()
        print('====> ', response)
        return response


class ModelViewSet(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   DestroyModelMixin,
                   mixins.ListModelMixin,
                   viewsets.GenericViewSet):

    pass

# Base ModelViewSet model:
class BaseModelViewSet(ModelViewSet):
    """
    Base ModelViewSet model.
    """

    # Initiate empty QuerySet:
    queryset = None

    # Authentication and permissions:
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [DjangoModelPermissions]

    # Django rest framework filters:
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    base_search_fields = ['id']
    base_ordering_fields = ['id']

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

    # Overwrite create method to add many serializer functionality:
    def create(self, *args, **kwargs):
        self.serializer_class = self.get_own_serializer_class(many=False)
        return viewsets.ModelViewSet.create(self, *args, **kwargs)

    # Overwrite update method to add many serializer functionality:
    def update(self, *args, **kwargs):
        self.serializer_class = self.get_own_serializer_class(many=False)
        return viewsets.ModelViewSet.update(self, *args, **kwargs)

    # Overwrite list method to add many serializer functionality:
    def list(self, *args, **kwargs):
        self.serializer_class = self.get_own_serializer_class(many=True)
        # Collect default search and ordering fields:
        self._receive_base_search_ordering_lists()
        return viewsets.ModelViewSet.list(self, *args, **kwargs)

    # Overwrite retrieve method to add many serializer functionality:
    def retrieve(self, *args, **kwargs):
        self.serializer_class = self.get_own_serializer_class(many=True)
        # Collect default search and ordering fields:
        self._receive_base_search_ordering_lists()
        return viewsets.ModelViewSet.retrieve(self, *args, **kwargs)

    def _receive_base_search_ordering_lists(self):
        class_representation = self.queryset.model
        if issubclass(class_representation, IdentificationModel):
            self.base_ordering_fields + ['name', 'slug', 'description', 'ico']
            self.base_search_fields + ['name', 'slug', 'description']
        elif issubclass(class_representation, AdministratorModel):
            self.base_ordering_fields + ['administrator']
            self.base_search_fields + ['administrator']
        elif issubclass(class_representation, DataTimeModel):
            self.base_ordering_fields + ['created', 'updated']
            self.base_search_fields + ['created', 'updated']
        elif issubclass(class_representation, StatusModel):
            self.base_ordering_fields + ['is_root', 'is_active']


# Read only Base ModelViewSet model:
# class BaseRoModelViewSet(
#     viewsets.GenericViewSet,
#     mixins.RetrieveModelMixin,
#     mixins.DestroyModelMixin,
#     mixins.ListModelMixin):
#     """
#     Base Read only ModelViewSet model.
#     """
#     # Authentication and permissions:
#     authentication_classes = [SessionAuthentication, TokenAuthentication]
#     permission_classes = [DjangoModelPermissions]

#     # Django rest framework filters:
#     filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
#     base_search_fields = ['id']
#     base_ordering_fields = ['id', 'created', 'updated', 'active', 'root']
