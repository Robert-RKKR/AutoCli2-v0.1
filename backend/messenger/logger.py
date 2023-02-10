# Messenger class import:
from .messenger import Messenger

# Nitinication constants:
NOTIFICATION_TYPE = 2


# Logger class:
class Logger(Messenger):
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

        # Extend iict function from Messenger class:
        super().__init__()

        # Default notification informations:
        self.notification_type = NOTIFICATION_TYPE
