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
        # Prepare data to return:
        data = {
            'page_error': {
                'code': 'server_error',
                'message': 'Internal server error.',
                'error': {}
            }
        }
        # Collect instance object:
        instance = self.get_object()
        try: # Try to delete provided object:
            response = self.perform_destroy(instance)
        except ProtectedError as exception:
            object_list = []
            # Iterate thru all related objects:
            for row in exception.protected_objects:
                try: # Try to collect object representation:
                    object_representation = row.name
                except:
                    object_representation = 'Empty'
                try: # Try to collect object related data:
                    application_name = row.__class__._meta.app_label
                    model_name = row.__class__.__name__
                    object_id = row.pk
                except:
                    application_name = None
                    model_name = None
                    object_id = None
                finally:
                    related_object_data = {
                        'application_name': application_name,
                        'model_name': model_name,
                        'object_representation': object_representation,
                        'object_id': object_id}
                    # Add collected object data into list:
                    object_list.append(related_object_data)
            # Collect error data:
            data['page_error']['error']['type'] = 'ProtectedError'
            data['page_error']['error']['message'] = str(exception.args)
            data['page_error']['error']['related_objects'] = object_list
            # Return JSON error response:
            return Response(data, status=status.HTTP_403_FORBIDDEN)
        except ValidationError as exception:
            # Collect error data:
            data['page_error']['error']['type'] = 'ValidationError'
            data['page_error']['error']['message'] = str(exception)
            # Return JSON error response:
            return Response(data, status=status.HTTP_403_FORBIDDEN)
        else:
            # Return 204 HTTP response if object was deleted:
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
