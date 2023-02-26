# Base message model import:
from autocli2.base.models.base_model import BaseModel

# Notification model import:
from notification.models.notification import Notification as NotificationModel

# Channels import:
from channels.layers import get_channel_layer

# Channels registration:
channel_layer = get_channel_layer()

# Async import:
from asgiref.sync import async_to_sync

# Settings import:
from django.conf import settings
from management.settings import collect_global_settings

# Severity constants declaration:
DEBUG = 5
INFO = 4
WARNING = 3
ERROR = 2
CRITICAL = 1


# Messenger class:
class Messenger:
    """ Logger class. """

    def __init__(self,
        application: str = '--NoName--',
        task_id: str = None) -> None:
        
        # Notification constants:
        self.IS_NOTIFICATION = None

        # Verify if the application variable is a valid sting:
        if isinstance(application, str):
            if len(application) <= 64:
                self.__application = application
            else:
                raise ValueError('The provided application variable is to long '\
                '(Allowed max 64 signs).')
        else:
            raise TypeError('The provided application variable must be string.')

        # Verify if the task ID variable is a valid sting:
        if isinstance(task_id, str):
            if len(task_id) <= 256:
                self.__task_id = task_id
            else:
                raise ValueError('The provided task ID variable is to long (Allowed max 256 signs).')
        elif task_id is not None:
            raise TypeError('The provided task ID variable must be string. '\
            f'Provided: "{task_id}"')

        # Object information's:
        self.correlated_object = None
        self.app_name = None
        self.model_name = None
        self.object_id = None
        self.object_representation = None

        # Notification information's:
        self.message = None
        self.action_type = None
        self.severity_level = None

        # Default notification information's:
        self.notification_type = None
        self.is_notification = None

    @property
    def application(self):
        return self.__application

    @property
    def task_id(self):
        return self.__task_id

    def __repr__(self) -> str:
        "Messenger class representation"
        return f'{self.message}'

    def critical(self,
        message: str,
        correlated_object: BaseModel = None,
        action_type: int = 0) -> NotificationModel:
        """
        Create a new critical log / notification based on the following data:

        Parameters:
        -----------------
        message: string
            Notification message string value.
        correlated_object: Django model class object
            Correlated object.
        action_type: integer
            Type of action (1-Created, 2-Updated, 3-Deleted).
            Default: 0-None.
        """

        # Check that notification settings allow logging:
        if self.IS_NOTIFICATION:
            if CRITICAL > collect_global_settings('notification_level'):
                return None
        else: # Check that logger settings allow logging:
            if CRITICAL > collect_global_settings('logger_level'):
                return None
        # Create log:
        return self._create_message(
            message,
            correlated_object,
            action_type,
            CRITICAL)

    def error(self,
        message: str,
        correlated_object: BaseModel = None,
        action_type: int = 0) -> NotificationModel:
        """
        Create a new error log / notification based on the following data:

        Parameters:
        -----------------
        message: string
            Notification message string value.
        correlated_object: Django model class object
            Correlated object.
        action_type: integer
            Type of action (1-Created, 2-Updated, 3-Deleted).
            Default: 0-None.
        """

        # Check that notification settings allow logging:
        if self.IS_NOTIFICATION:
            if ERROR > collect_global_settings('notification_level'):
                return None
        else: # Check that logger settings allow logging:
            if ERROR > collect_global_settings('logger_level'):
                return None
        # Create log:
        return self._create_message(
            message,
            correlated_object,
            action_type,
            ERROR)

    def warning(self,
        message: str,
        correlated_object: BaseModel = None,
        action_type: int = 0) -> NotificationModel:
        """
        Create a new warning log / notification based on the following data:

        Parameters:
        -----------------
        message: string
            Notification message string value.
        correlated_object: Django model class object
            Correlated object.
        action_type: integer
            Type of action (1-Created, 2-Updated, 3-Deleted).
            Default: 0-None.
        """

        # Check that notification settings allow logging:
        if self.IS_NOTIFICATION:
            if WARNING > collect_global_settings('notification_level'):
                return None
        else: # Check that logger settings allow logging:
            if WARNING > collect_global_settings('logger_level'):
                return None
        # Create log:
        return self._create_message(
            message,
            correlated_object,
            action_type,
            WARNING)

    def info(self,
        message: str,
        correlated_object: BaseModel = None,
        action_type: int = 0) -> NotificationModel:
        """
        Create a new info log / notification based on the following data:

        Parameters:
        -----------------
        message: string
            Notification message string value.
        correlated_object: Django model class object
            Correlated object.
        action_type: integer
            Type of action (1-Created, 2-Updated, 3-Deleted).
            Default: 0-None.
        """

        # Check that notification settings allow logging:
        if self.IS_NOTIFICATION:
            if INFO > collect_global_settings('notification_level'):
                return None
        else: # Check that logger settings allow logging:
            if INFO > collect_global_settings('logger_level'):
                return None
        # Create log:
        return self._create_message(
            message,
            correlated_object,
            action_type,
            INFO)
                
    def debug(self,
        message: str,
        correlated_object: BaseModel = None,
        action_type: int = 0) -> NotificationModel:
        """
        Create a new debug log / notification based on the following data:

        Parameters:
        -----------------
        message: string
            Notification message string value.
        correlated_object: Django model class object
            Correlated object.
        action_type: integer
            Type of action (1-Created, 2-Updated, 3-Deleted).
            Default: 0-None.
        """

        # Check that notification settings allow logging:
        if self.IS_NOTIFICATION:
            if DEBUG > collect_global_settings('notification_level'):
                return None
        else: # Check that logger settings allow logging:
            if DEBUG > collect_global_settings('logger_level'):
                return None
        # Create log:
        return self._create_message(
            message,
            correlated_object,
            action_type,
            DEBUG)

    def _create_message(self,
        message: str,
        correlated_object: BaseModel,
        action_type: int,
        severity_level: int) -> NotificationModel:
        """ Create a new message. """

        # Collect data:
        self.message = message
        self.correlated_object = correlated_object
        self.action_type = action_type
        self.severity_level = severity_level

        # Verify provided variables:
        self._verification()
        
        # Collect object information:
        self._collect_object_information()

        # Prepare data dictionary:
        notification_data = {
            'type': 'send_collect',
            'message': self.message,
            'app_name': self.app_name,
            'model_name': self.model_name,
            'object_id': self.object_id,
            'object_representation': self.object_representation,
            'action_type': self.action_type,
            'notification_type': self.notification_type,
            'severity': self.severity_level,
            'application': self.application}

        if self.is_notification:
            # Send channel notification:
            async_to_sync(channel_layer.group_send)(self.channel_name, 
                notification_data)
        
        try: # Try to save notification in database:
            del notification_data['type']
            notification = NotificationModel.objects.create(
                **notification_data)
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
            # Try to collect object representation:
            try:
                self.object_representation = self.correlated_object.name
            except:
                self.object_representation = 'Empty'

    def _verification(self):
        """
        Provided data verification.
        """

        # Verify if the notification message variable is a valid sting:
        if isinstance(self.message, str):
            if len(self.message) > 256:
                raise ValueError('The provided notification message variable is to long (Allowed max 256 signs).')
        elif self.message is not None:
            raise TypeError('The provided notification message variable must be string. '\
            f'Provided: "{self.message}"')

        # Verify if provided object is valid:
        if not isinstance(self.correlated_object, BaseModel) and self.correlated_object is not None:
            if self.correlated_object is not None:
                raise TypeError('Provided object id not a valid Django object. '\
                f' Provided: "{self.correlated_object}"')

        # Verify if the action type variable is a valid sting:     
        if not isinstance(self.action_type, int) and self.action_type is not None:
            raise TypeError('The provided action type variable must be integer. '\
            f' Provided: "{self.action_type}"')
