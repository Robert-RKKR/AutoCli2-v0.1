# Rest framework - viewsets import:
from rest_framework import viewsets

# Rest framework - authentication & permissions import:
from rest_framework.authentication import SessionAuthentication
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import DjangoModelPermissions

# Rest framework - filters import:
from rest_framework.filters import OrderingFilter
from rest_framework.filters import SearchFilter

# Django filters - rest framework filters import:
from django_filters.rest_framework import DjangoFilterBackend

# AutoCli2 - base model mixin import:
from autocli2.base.api.base_model_mixin import BaseRetrieveModelMixin
from autocli2.base.api.base_model_mixin import BaseDestroyModelMixin
from autocli2.base.api.base_model_mixin import BaseUpdateModelMixin
from autocli2.base.api.base_model_mixin import BaseCreateModelMixin
from autocli2.base.api.base_model_mixin import BaseListModelMixin


# Base ModelViewSet models:
class BaseRwModelViewSet(
    BaseCreateModelMixin,
    BaseRetrieveModelMixin,
    BaseUpdateModelMixin,
    BaseDestroyModelMixin,
    BaseListModelMixin,
    viewsets.GenericViewSet):
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

    # Log changes:
    log_changes = False


# Read only Base ModelViewSet model:
class BaseRoModelViewSet(
    viewsets.GenericViewSet,
    BaseRetrieveModelMixin,
    BaseListModelMixin):
    """
    Base Read only ModelViewSet model.
    """

    # Authentication and permissions:
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [DjangoModelPermissions]

    # Django rest framework filters:
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]


# Read only plus edit Base ModelViewSet model:
class BaseRoPlusModelViewSet(
    viewsets.GenericViewSet,
    BaseRetrieveModelMixin,
    BaseUpdateModelMixin,
    BaseListModelMixin):
    """
    Base Read only ModelViewSet model.
    """

    # Authentication and permissions:
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [DjangoModelPermissions]

    # Django rest framework filters:
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
