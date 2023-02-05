# Document description:
__author__ = 'Robert Tadeusz Kucharski'
__version__ = '2.0'

# Django import:
from django.db.models import Model

# Channels import:
from channels.layers import get_channel_layer

# Channels registration:
channel_layer = get_channel_layer()

# Async import:
from asgiref.sync import async_to_sync

# Notification model import:
from messenger.models.notification import Notification as NotificationModel


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

        # Object information:
        self.correlated_object = None
        self.app_name = None
        self.model_name = None
        self.object_id = None
        self.object_representation = None

        # Notification information:
        self.notification_message = None
        self.action_type = None
        self.notification_type = None
        self.severity_level = None
        self.channel_name = None
        self.task_id = None

    @property
    def application(self):
        return self.__application

    def __repr__(self) -> str:
        "Notification class representation"
        return f'Notification({self.__application})'

    def notification(self,
        notification_message: str,
        correlated_object: Model = None,
        action_type: int = 0,
        severity_level: int = 5,
        channel_name: str = 'notification'):
        """
        Create a new channel only notification based on the following data:

        Parameters:
        -----------------
        notification_message: string
            Notification message string value.
        action_type: integer
            Type of action (1-Created, 2-Updated, 3-Deleted).
            Default: 0-None.
        notification_type: integer
            Type of notification (1-User, 2-Log).
            Default: 2-Log.
        correlated_object: Django model class object
            Correlated object.
        severity_level: integer
            Notification severity level (1-5).
            Default: 5-Debug.
        channel_name: string
            Notification channel name.
        """

        # Collect data:
        self.correlated_object = correlated_object
        self.notification_message = notification_message
        self.action_type = action_type
        self.notification_type = 1
        self.severity_level = severity_level
        self.channel_name = channel_name

        # Verify provided data:
        self._verification()
        
        # Collect object information:
        self._collect_object_information()

        # Send channel notification:
        async_to_sync(channel_layer.group_send)(channel_name, {
            'type': 'send_collect',
            'message': self.notification_message,
            'app_name': self.app_name,
            'model_name': self.model_name,
            'object_id': self.object_id,
            'object_representation': self.object_representation,
            'action_type': self.action_type,
            'notification_type': self.notification_type,
            'application': self.application,
            # 'administrator': administrator,
            'link': 'None'})
        
        # Try to save notification in database:
        try:
            notification = NotificationModel.objects.create(
                app_name=self.app_name,
                model_name=self.model_name,
                object_id=self.object_id,
                object_representation=self.object_representation,
                action_type=self.action_type,
                notification_type=self.notification_type,
                severity=self.severity_level,
                application=self.application,
                message=self.notification_message)
        except:
            return False
        else:
            return notification

    def logger(self,
        notification_message: str,
        correlated_object: Model = None,
        action_type: int = 0,
        severity_level: int = 5,
        task_id: str = 'None'):
        """
        Create a new database only notification based on the following data:

        Parameters:
        -----------------
        notification_message: string
            Notification message string value.
        action_type: integer
            Type of action (1-Created, 2-Updated, 3-Deleted).
            Default: 0-None.
        notification_type: integer
            Type of notification (1-User, 2-Log).
            Default: 2-Log.
        correlated_object: Django model class object
            Correlated object.
        severity_level: integer
            Notification severity level (1-5).
            Default: 5-Debug.
        task_id
        """

        # Collect data:
        self.correlated_object = correlated_object
        self.notification_message = notification_message
        self.action_type = action_type
        self.notification_type = 2
        self.severity_level = severity_level
        self.task_id = task_id

        # Verify provided data:
        self._verification()
        
        # Collect object information:
        self._collect_object_information()
        
        # Try to save notification in database:
        try:
            notification = NotificationModel.objects.create(
                app_name=self.app_name,
                model_name=self.model_name,
                object_id=self.object_id,
                object_representation=self.object_representation,
                action_type=self.action_type,
                notification_type=self.notification_type,
                severity=self.severity_level,
                application=self.application,
                message=self.notification_message,
                task_id=self.task_id)
        except:
            return False
        else:
            return notification

    def _collect_object_information(self):
        # Check if object was provided:
        if self.correlated_object:
            # Collect app and model name based on object information:
            self.app_name = self.correlated_object.__class__._meta.app_label
            self.model_name = self.correlated_object.__class__.__name__
            # Collect object ID:
            self.object_id = self.correlated_object.id

    def _verification(self):
        """
        Provided data verification.
        """

        # Verify if the notification message variable is a valid sting:
        if isinstance(self.notification_message, str):
            if len(self.notification_message) > 256:
                raise ValueError('The provided notification message variable is to long (Allowed max 256 signs).')
        elif self.notification_message is not None:
            raise TypeError('The provided notification message variable must be string. '\
            f'Provided: "{self.notification_message}"')
        
        # Verify if the task ID variable is a valid sting:
        if isinstance(self.task_id, str):
            if len(self.task_id) > 256:
                raise ValueError('The provided task ID variable is to long (Allowed max 256 signs).')
        elif self.task_id is not None:
            raise TypeError('The provided task ID variable must be string. '\
            f'Provided: "{self.task_id}"')

        # Verify if the type variable is a valid sting:     
        if not isinstance(self.notification_type, int) and self.notification_type is not None:
            raise TypeError('The provided notification type variable must be integer. '\
            f' Provided: "{self.notification_type}"')

        # Verify if the action type variable is a valid sting:     
        if not isinstance(self.action_type, int) and self.action_type is not None:
            raise TypeError('The provided action type variable must be integer. '\
            f' Provided: "{self.action_type}"')

        # Verify if the severity level variable is a valid sting:     
        if not isinstance(self.severity_level, int) and self.severity_level is not None:
            raise TypeError('The provided severity level variable must be integer. '\
            f' Provided: "{self.severity_level}"')

        # Verify if the type variable is a valid sting:      
        if not isinstance(self.channel_name, str) and self.channel_name is not None:
            raise TypeError('The provided notification variable must be string. '\
            f' Provided: "{self.channel_name}"')

        # Verify if provided object is valid:
        if not isinstance(self.correlated_object, Model) and self.correlated_object is not None:
            if self.correlated_object is not None:
                raise TypeError('Provided object id not a valid Django object. '\
                f' Provided: "{self.correlated_object}"')
