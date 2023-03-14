# Rest framework - mixins import:
from rest_framework.mixins import RetrieveModelMixin
from rest_framework.mixins import DestroyModelMixin
from rest_framework.mixins import UpdateModelMixin
from rest_framework.mixins import CreateModelMixin
from rest_framework.mixins import ListModelMixin

# Rest framework - other imports:
from rest_framework.settings import api_settings
from rest_framework.response import Response
from rest_framework import status

# Django - errors import:
from django.core.exceptions import ValidationError
from django.db.models import ProtectedError


# Base mixins classes:
class BaseDestroyModelMixin(DestroyModelMixin):
    """
    Destroy a model instance.
    """

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        try:
            response = self.perform_destroy(instance)
        except ProtectedError as error:
            error_string = str(error)
            return Response(error_string, status=status.HTTP_403_FORBIDDEN)
        except ValidationError as error:
            error_string = str(error)
            return Response(error_string, status=status.HTTP_403_FORBIDDEN)
        else:
            return Response(status=status.HTTP_204_NO_CONTENT)     


class BaseCreateModelMixin(CreateModelMixin):
    """
    Create a model instance.
    """

    pass


class BaseRetrieveModelMixin(RetrieveModelMixin):
    """
    Retrieve a model instance.
    """

    pass


class BaseUpdateModelMixin(UpdateModelMixin):
    """
    Update a model instance.
    """

    pass


class BaseListModelMixin(ListModelMixin):
    """
    List a queryset.
    """

    pass
