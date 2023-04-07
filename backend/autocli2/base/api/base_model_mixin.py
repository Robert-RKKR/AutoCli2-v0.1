# Python - copy import:
import copy

# Django - admin import:
from django.contrib import admin

# Django - exceptions import:
from django.core.exceptions import ValidationError
from django.db.models import ProtectedError

# Rest framework - mixins import:
from rest_framework.mixins import RetrieveModelMixin
from rest_framework.mixins import DestroyModelMixin
from rest_framework.mixins import CreateModelMixin
from rest_framework.mixins import ListModelMixin

# Rest framework - other imports:
from rest_framework.response import Response
from rest_framework import status

# Rest framework - exceptions import:
from rest_framework.exceptions import APIException

# AutoCli2 - constance import:
from autocli2.base.constants.action_type import ActionTypeChoices

# AutoCli2 - notification import:
from notification.notification import Notification

# AutoCli2 - log change import:
from notification.log_change import log_change

# AutoCli2 - collect object information import:
from notification.collect_object_data import collect_object_data

# Init API notification:
notification = Notification('API', channel_name='objects_notifications')

# Helper functions:
def is_not_root(instance: object, status_code: int) -> bool:
    """
    Args:
        instance (object):
            The instance on which the notification will be created.
        status_code (int):
            The HTTP Status Code.

    Raises:
        APIException:
            If the instance is a root object,
            an error message will be raised.

    Returns:
        bool: 
            If instance is root function wil raise exception,
            if instance is not root function will return True.
    """
    
    try: # Try to collect is root object attribute:
        is_root = instance.is_root
    except: # If object doesn't have is root attribute, return True:
        return True
    else: # If root object attribute is True return API error:
        if is_root: # Prepare Root error message:
            message = f"{instance._meta.object_name} object can't "\
                "be changed, because it's a root object"
            # Prepare error response:
            exception = {
                'RootProtectedError': {
                    'type': 'RootProtectedError',
                    'message': message}}
            # Raise API error:
            raise APIException(exception, status_code)
        else:
            # If root object attribute is False, return True:
            return True
        
def create_notification(
    instance: object,
    action: ActionTypeChoices,
    user: admin,
    serializer = False) -> None:
    """
    Args:
        instance (object):
            The instance on which the notification will be created.
        action (ActionTypeChoices):
            Notification action (Create, Update, Delete).
        user (admin):
            Django user who make action.
    """

    # Create a new change notification:
    log_change(instance, user, action)
    # Collect instance representation:
    try: # Try to collect name value like instance representation:
        instance_representation = instance.name
    except: # If instance doesn't have name value:
        try: # Try to collect PK / ID value like instance representation:
            instance_representation = instance.pk
        except: # Return non like instance representation:
            return None
    # Create a new message:
    if action == ActionTypeChoices.DELETE:
        message = f'{instance_representation} object has been deleted.'
    elif action == ActionTypeChoices.CREATE:
        message = f'A new object {instance_representation} has been created.'
    elif action == ActionTypeChoices.UPDATE:
        message = f'{instance_representation} object has been updated.'
    try: # Try to collect url:
        url = serializer.data['url']
    except: # If url not available return None:
        url = None
    # Send notification:
    notification.info(message, instance, action, url=url)


# Base mixins classes:
class BaseDestroyModelMixin(DestroyModelMixin):
    """
    Destroy a model instance.
    """

    def destroy(self, request, *args, **kwargs):
        # Collect instance object:
        instance = self.get_object()
        # Copy instance:
        copy_instance = copy.copy(instance)
        # Check if instance is root object:
        if is_not_root(instance, 403):
            try: # Try to delete provided object:
                self.perform_destroy(instance)
            except ProtectedError as exception:
                object_list = []
                # Iterate thru all related objects:
                for row in exception.protected_objects:
                    related_object_data = collect_object_data(row)
                    # Add collected object data into list:
                    object_list.append(related_object_data)
                # Prepare error response:
                error_response = {
                    'ProtectedError': {
                        'type': 'ProtectedError',
                        'message': str(exception.args),
                        'related_objects': object_list}}
                # Raise API error:
                raise APIException(error_response, 409)
            else:
                # Create change notifications:
                create_notification(
                    copy_instance, ActionTypeChoices.DELETE, request.user)
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
        # Create change notifications:
        create_notification(
            instance, ActionTypeChoices.CREATE, request.user, serializer)
        # Prepare headers:
        headers = self.get_success_headers(serializer.data)
        # prepare response:
        response = {
            'page_results': serializer.data}
        # Return HTTP response 201, object was created:
        return Response(
            response, status=status.HTTP_201_CREATED, headers=headers)


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
        # Check if instance is root object:
        if is_not_root(instance, 403):
            # Collect serializer:
            serializer = self.get_serializer(
                instance, data=request.data, partial=partial)
            # Validate serializer:
            serializer.is_valid(raise_exception=True)
            try: # Try to update object:
                serializer.save()
            except ValidationError as exception:
                # Collect error data:
                error_response = {
                    'ValidationError': {
                        'type': 'ValidationError',
                        'message': exception.message}}
                # Raise API error:
                raise APIException(error_response, 403)
            else:
                # Create change notifications:
                create_notification(
                    instance, ActionTypeChoices.UPDATE, request.user, serializer)
                # getattr update action:
                if getattr(instance, '_prefetched_objects_cache', None):
                    # If 'prefetch_related' has been applied to a queryset, 
                    # we need to forcibly invalidate the prefetch cache
                    # on the instance.
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
