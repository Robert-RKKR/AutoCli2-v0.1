# Rest framework - mixins import:
from rest_framework.mixins import RetrieveModelMixin
from rest_framework.mixins import DestroyModelMixin
from rest_framework.mixins import UpdateModelMixin
from rest_framework.mixins import CreateModelMixin
from rest_framework.mixins import ListModelMixin

# Rest framework - other imports:
from rest_framework.response import Response
from rest_framework import status

# Rest framework - exceptions import:
from rest_framework.exceptions import APIException

# Django - exceptions import:
from django.core.exceptions import ValidationError
from django.db.models import ProtectedError

# AutoCli2 - log change import:
from notification.log_change import log_change

# AutoCli2 - constance import:
from autocli2.base.constants.action_type import ActionTypeChoices as ActionType

# Custom error page:
error_response = {
    'page_results': False,
    'page_error': {
        'code': 'server_error',
        'message': 'Internal server error.',
        'errors': None
    }
}

# Hellper function:
def is_root_action(instance, status_code) -> bool:
    try: # Try to collect is root object attibute:
        is_root = instance.is_root
    except:
        # If object doesn't have is root attibute, return True:
        return True
    else:
        # If root object attibute is True return API error:
        if is_root:
            raise APIException(f"{instance._meta.object_name} object can't "\
                "be changed because it's a root object", status_code)
        else:
            # If root object attibute is False, return True:
            return True


# Base mixins classes:
class BaseDestroyModelMixin(DestroyModelMixin):
    """
    Destroy a model instance.
    """

    def destroy(self, request, *args, **kwargs):
        # Collect instance object:
        instance = self.get_object()
        # Check if instanse is root object:
        if is_root_action(instance, 400):
            try: # Try to delete provided object:
                self.perform_destroy(instance)
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
                error_response['page_error']['error']['type'] = 'ProtectedError'
                error_response['page_error']['error']['message'] = str(exception.args)
                error_response['page_error']['error']['related_objects'] = object_list
                # Return JSON error response:
                return Response(error_response, status=status.HTTP_403_FORBIDDEN)
            else:
                # Create change:
                log_change(instance, request.user, ActionType.DELETE)
                # Return 204 HTTP response if object was deleted:
                return Response(status=status.HTTP_204_NO_CONTENT)     


class BaseCreateModelMixin(CreateModelMixin):
    """
    Create a model instance.
    """

    def create(self, request, *args, **kwargs):
        # Collect serializer:
        serializer = self.get_serializer(data=request.data)
        # Validate serializer:
        serializer.is_valid(raise_exception=True)
        # Save serializer:
        instance = serializer.save()
        # Create change:
        log_change(instance, request.user, ActionType.CREATE)
        # Prepare headers:
        headers = self.get_success_headers(serializer.data)
        response = {
            'page_results': serializer.data}
        # Return HTTP response 201, object was created:
        return Response(response, status=status.HTTP_201_CREATED, headers=headers)


class BaseRetrieveModelMixin(RetrieveModelMixin):
    """
    Retrieve a model instance.
    """
    
    def retrieve(self, request, *args, **kwargs):
        # Collect instance:
        instance = self.get_object()
        # Collect serializer:
        serializer = self.get_serializer(instance)
        # Prepare response:
        response = {
            'page_results': serializer.data}
        # Return HTTP response 200.
        return Response(response, status=status.HTTP_200_OK)


class BaseUpdateModelMixin:
    """
    Update a model instance.
    """
    
    def update(self, request, *args, **kwargs):
        # Update method:
        partial = kwargs.pop('partial', False)
        # Collect instance:
        instance = self.get_object()
        # Check if instanse is root object:
        if is_root_action(instance, 400):
            # Collect serializer:
            serializer = self.get_serializer(
                instance, data=request.data, partial=partial)
            # Validate serializer:
            serializer.is_valid(raise_exception=True)
            try: # Try to update object:
                serializer.save()
            except ValidationError as exception:
                # Collect error data:
                error_response['page_error']['error']['type'] = 'ValidationError'
                error_response['page_error']['error']['message'] = exception.message
                # Return JSON error response:
                return Response(error_response, status=status.HTTP_403_FORBIDDEN)
            else:
                # Create change:
                log_change(instance, request.user, ActionType.UPDATE)
                # getattr update action:
                if getattr(instance, '_prefetched_objects_cache', None):
                    # If 'prefetch_related' has been applied to a queryset, we need to
                    # forcibly invalidate the prefetch cache on the instance.
                    instance._prefetched_objects_cache = {}
                # Prepare response:
                response = {
                    'page_results': serializer.data}
                # Return HTTP response 200, object was updated:
                return Response(response, status=status.HTTP_200_OK)

class BaseListModelMixin(ListModelMixin):
    """
    List a queryset.
    """

    pass
