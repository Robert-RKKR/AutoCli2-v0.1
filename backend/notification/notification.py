# Messenger class import:
from .messenger import Messenger


# Notification class:
class Notification(Messenger):
    """
    Notification class.

    Methods:
    --------
    critical:
        Create critical severity notification.
    error:
        Create error severity notification.
    warning:
        Create warning severity notification.
    info:
        Create info severity notification.
    debug:
        Create debug severity notification.
    """

    def __init__(self,
        application: str = '--NoName--',
        task_id: str = 'None',
        channel_name: str = 'notification') -> None:
        """
        Notification class.
        Provided the ability to notify users of events via
        Django channels and database.

        Parameters:
        -----------------
        application: string
            Name of the application that triggers notifications.
        channel_name: string
            Channel name used to send notifications to users.
        task_id: string
            Taks ID related with celery task.
        """

        # Extend init function from Messenger class:
        super().__init__(application, task_id)

        # Notification constants:
        self.IS_NOTIFICATION = True
        self.NOTIFICATION_TYPE = 1

        # Verify if the channel name variable is a valid sting:
        if isinstance(channel_name, str):
            self.__channel_name = channel_name
        else:
            raise TypeError('The provided application variable must be string.')

        # Default notification information's:
        self.notification_type = self.NOTIFICATION_TYPE
        self.is_notification = self.IS_NOTIFICATION

    @property
    def channel_name(self):
        return self.__channel_name
