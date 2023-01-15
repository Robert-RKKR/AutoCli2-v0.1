# Document description:
__author__ = 'Robert Tadeusz Kucharski'
__version__ = '1.0'

# Django import:
from django.db.models import Model

# Channels import:
from channels.layers import get_channel_layer

# Channels registration:
channel_layer = get_channel_layer()

# Async import:
from asgiref.sync import async_to_sync

# Notification model import:
from message.notification.models.notification import Notification as NotificationModel

class Notification:
    """
    Notification class.

    Methods:
    --------
    send_notification:
        Send notifications through the channel and
        save them to database.
    send_channel_notification:
        Send notifications only through the channel.
    send_database_notification:
        Save notifications to the database only.
    """

    def __init__(self, application: str = '--NoName--') -> None:
        """
        Notification application activity.
        """

        # Verify if the application variable is a valid sting:
        if isinstance(application, str):
            if len(application) <= 64:
                self.__application = application
            else:
                raise ValueError('The provided application variable is to long (Allowed max 64 signs).')
        else:
            raise TypeError('The provided application variable must be string.')

        # Log data:
        self.log_data = None

    @property
    def application(self):
        return self.__application

    def __repr__(self) -> str:
        "Notification class representation"
        return f'Notification({self.__application})'

    def channel_notification(self,
        notification_message: str,
        correlated_object: Model = None,
        notification_type: int = 0,
        severity_level: int = 0,
        channel_name: str = 'notification'):
        """
        Create a new channel only notification based on the following data:

        Parameters:
        -----------------
        notification_message: string
            Notification message string value.
        notification_type: integer
            Type of notification.
        correlated_object: Django model class object
            Correlated object.
        channel_name: string
            Notification channel name.
        severity_level: integer
            Notification severity level.
        """

        # Verify provided data:
        self._verification(
            notification_message,
            notification_type,
            severity_level,
            correlated_object,
            channel_name)

        # Check if object was provided:
        if correlated_object:
            async_to_sync(channel_layer.group_send)(channel_name, {
                'type': 'send_collect',
                'message': notification_message,
                'app_name': correlated_object.__class__._meta.app_label,
                'model_name': correlated_object.__class__.__name__,
                'object_id': correlated_object.pk,
                'notification_type': notification_type,
                'application': self.__application,
                'link': 'None'})
        else: # If object was not provided:
            async_to_sync(channel_layer.group_send)(channel_name, {
                'type': 'send_collect',
                'message': notification_message,
                'application': self.__application,
            })

    def database_notification(self,
        notification_message: str,
        correlated_object: Model = None,
        notification_type: int = 0,
        severity_level: int = 0):
        """
        Create a new database only notification based on the following data:

        Parameters:
        -----------------
        notification_message: string
            Notification message string value.
        notification_type: integer
            Type of notification.
        correlated_object: Django model class object
            Correlated object.
        severity_level: integer
            Notification severity level.
        """

        # Verify provided data:
        self._verification(
            notification_message,
            notification_type,
            severity_level,
            correlated_object)

        # Check if object was provided:
        if correlated_object:
            # Collect app and model name based on object information:
            app_name = correlated_object.__class__._meta.app_label
            model_name = correlated_object.__class__.__name__
            # Collect object ID:
            object_id = correlated_object.id
        else: # If object was not provided:
            app_name = None
            model_name = None
            object_id = None
        
        # Try to create notification:
        try:
            notification = NotificationModel.objects.create(
                app_name=app_name,
                model_name=model_name,
                object_id=object_id,
                type=notification_type,
                severity=severity_level,
                application=self.__application,
                message=notification_message)
        except:
            return False
        else:
            return notification

    def send(self,
        notification_message: str,
        correlated_object: Model = None,
        notification_type: int = 0,
        severity_level: int = 0,
        channel_name: str = 'notification'):
        """
        Create a new channel and database notification based on the following data:

        Parameters:
        -----------------
        notification_message: string
            Notification message string value.
        notification_type: integer
            Type of notification.
        correlated_object: Django model class object
            Correlated object.
        channel_name: string
            Notification channel name.
        severity_level: integer
            Notification severity level.
        """

        self.channel_notification(
            notification_message,
            correlated_object,
            notification_type,
            severity_level,
            channel_name)
        return self.database_notification(
            notification_message,
            correlated_object,
            notification_type,
            severity_level)

    def _verification(self, notification_message,
            notification_type,
            severity_level,
            correlated_object,
            channel_name='None'):
        """
        Provided data verification.
        """

        # Verify if the task_id variable is a valid sting:
        if isinstance(notification_message, str):
            if len(notification_message) > 256:
                raise ValueError('The provided message variable is to long (Allowed max 256 signs).')
        else:
            raise TypeError('The provided message variable must be string. '\
            f'Provided: "{notification_message}"')

        # Verify if the type variable is a valid sting:     
        if not isinstance(notification_type, int):
            raise TypeError('The provided type variable must be integer. '\
            f' Provided: "{notification_type}"')

        # Verify if the severity level variable is a valid sting:     
        if not isinstance(severity_level, int):
            raise TypeError('The provided severity level variable must be integer. '\
            f' Provided: "{severity_level}"')

        # Verify if the type variable is a valid sting:      
        if not isinstance(channel_name, str):
            raise TypeError('The provided notification variable must be string. '\
            f' Provided: "{channel_name}"')

        # Verify if provided object is valid:
        if not isinstance(correlated_object, Model):
            if correlated_object is not None:
                raise TypeError('Provided object id not a valid Django object. '\
                f' Provided: "{correlated_object}"')
