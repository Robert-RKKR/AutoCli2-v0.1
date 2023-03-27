# AutoCli2 - notification model import:
from notification.messenger import Messenger

# AutoCli2 - constance import:
from autocli2.base.constants.notification_type import NotificationTypeChoices


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
        task_id: str = 'None') -> None:
        """
        Logger class.
        Provided the ability to log events in database.

        Parameters:
        -----------------
        application: string
            Name of the application that triggers notifications.
        task_id: string
            Taks ID related with celery task.
        """
        # Extend init function from Messenger class:
        super().__init__(application, task_id)

        # Notification constants:
        self.IS_NOTIFICATION = False
        self.NOTIFICATION_TYPE = NotificationTypeChoices.BACKLOG


        # Default notification information's:
        self.notification_type = self.NOTIFICATION_TYPE
