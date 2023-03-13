# Rest framework - mixins import:
from rest_framework.mixins import RetrieveModelMixin
from rest_framework.mixins import DestroyModelMixin
from rest_framework.mixins import UpdateModelMixin
from rest_framework.mixins import CreateModelMixin
from rest_framework.mixins import ListModelMixin

# Rest framework - other imports:
from rest_framework.response import Response
from rest_framework import status


# Base mixins classes:
class BaseDestroyModelMixin:
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
        return response


class BaseCreateModelMixin(CreateModelMixin):
    """
    Xxx.
    """

    pass


class BaseRetrieveModelMixin(RetrieveModelMixin):
    """
    Xxx.
    """

    pass


class BaseUpdateModelMixin(UpdateModelMixin):
    """
    Xxx.
    """

    pass


class BaseListModelMixin(ListModelMixin):
    """
    Xxx.
    """

    pass
