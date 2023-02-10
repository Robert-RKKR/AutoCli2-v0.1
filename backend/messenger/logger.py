# Document description:
__author__ = 'Robert Tadeusz Kucharski'
__version__ = '3.0'

# Django import:
from django.db.models import Model

# Base message model import:
from .base_message import BaseMessageModel

# Notification model import:
from messenger.models.notification import Notification as NotificationModel

# Settings import:
from django.conf import settings

# Nitinication constants:
NOTIFICATION_TYPE = 2

# Severity constants declaration:
DEBUG = 5
INFO = 4
WARNING = 3
ERROR = 2
CRITICAL = 1


# Logger class:
class Logger:
    """
    Logger class.

    Methods:
    --------
    critical:
        Create critical severity log.
    error:
        Create error severity log.
    warning:
        Create warning severity log.
    info:
        Create info severity log.
    debug:
        Create debug severity log.
    """

    def __init__(self,
        application: str = '--NoName--',
        task_id: str = None) -> None:
        """
        Logger class.
        Provided the ability to log events in database.

        Parameters:
        -----------------
        application: string
            Name of the application that triggers notifications.
        task_id: string
            Taks ID related with cellery task.
        """

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
            if len(self.task_id) <= 256:
                self.__task_id = task_id
            else:
                raise ValueError('The provided task ID variable is to long (Allowed max 256 signs).')
        elif self.task_id is not None:
            raise TypeError('The provided task ID variable must be string. '\
            f'Provided: "{self.task_id}"')

        # Object informations:
        self.correlated_object = None
        self.app_name = None
        self.model_name = None
        self.object_id = None
        self.object_representation = None

        # Notification informations:
        self.notification_message = None
        self.action_type = None
        self.severity_level = None

        # Default notification informations:
        self.notification_type = NOTIFICATION_TYPE

    @property
    def application(self):
        return self.__application

    @property
    def task_id(self):
        return self.__task_id

    def __repr__(self) -> str:
        "Logger class representation"
        return f'Logger({self.notification_message})'

    def critical(self,
        notification_message: str,
        correlated_object: Model = None,
        action_type: int = 0) -> NotificationModel:
        """
        Create a new critical notification based on the following data:

        Parameters:
        -----------------
        notification_message: string
            Notification message string value.
        correlated_object: Django model class object
            Correlated object.
        action_type: integer
            Type of action (1-Created, 2-Updated, 3-Deleted).
            Default: 0-None.
        """

        # Run process of log and details log creation:
        if settings.NOTIFICATION_DEBUG:
            return self._create_logger(
                notification_message,
                correlated_object,
                action_type,
                CRITICAL)

    def _create_logger(self,
        notification_message: str,
        correlated_object: Model,
        action_type: int,
        severity_level: int) -> NotificationModel:
        """ Create a new logger message. """

        # Collect data:
        self.notification_message = notification_message
        self.correlated_object = correlated_object
        self.action_type = action_type
        self.severity_level = severity_level

        # Verify provided vairables:
        self._verification()
        
        # Collect object information:
        self._collect_object_information()

        # Prepare data dictionary:
        notification_data = {
            'type': 'send_collect',
            'message': self.notification_message,
            'app_name': self.app_name,
            'model_name': self.model_name,
            'object_id': self.object_id,
            'object_representation': self.object_representation,
            'action_type': self.action_type,
            'notification_type': self.notification_type,
            'severity': self.severity_level,
            'application': self.application}
        
        # Try to save notification in database:
        try:
            del notification_data['type']
            notification = NotificationModel.objects.create(
                notification_data)
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
        if isinstance(self.notification_message, str):
            if len(self.notification_message) > 256:
                raise ValueError('The provided notification message variable is to long (Allowed max 256 signs).')
        elif self.notification_message is not None:
            raise TypeError('The provided notification message variable must be string. '\
            f'Provided: "{self.notification_message}"')

        # Verify if provided object is valid:
        if not isinstance(self.correlated_object, BaseMessageModel) and self.correlated_object is not None:
            if self.correlated_object is not None:
                raise TypeError('Provided object id not a valid Django object. '\
                f' Provided: "{self.correlated_object}"')

        # Verify if the action type variable is a valid sting:     
        if not isinstance(self.action_type, int) and self.action_type is not None:
            raise TypeError('The provided action type variable must be integer. '\
            f' Provided: "{self.action_type}"')
