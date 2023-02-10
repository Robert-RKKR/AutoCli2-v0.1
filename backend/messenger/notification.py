# Messenger class import:
from .messenger import Messenger

# Nitinication constants:
IS_NOTIFICATION = True
NOTIFICATION_TYPE = 1


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
        channel_name: str = 'notification',
        task_id: str = None) -> None:
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
            Taks ID related with cellery task.
        """

        # Extend iict function from Messenger class:
        super().__init__()

        # Verify if the channel name variable is a valid sting:
        if isinstance(application, str):
            self.__channel_name = channel_name
        else:
            raise TypeError('The provided application variable must be string.')

        # Default notification informations:
        self.notification_type = NOTIFICATION_TYPE
        self.is_notification = IS_NOTIFICATION

    @property
    def channel_name(self):
        return self.__channel_name
