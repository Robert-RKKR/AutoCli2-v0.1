# Celery Import:
from celery import Task

# Python Import:
import time

# Application Import:
from notification.notification import Notification
from notification.logger import Logger


# Base task class
class BaseTask(Task):

    # Basic celery attributes:
    ignore_result = False
    validation_class = ''
    public = True
    task_id = 'None'

    # Task identity attributes:
    description = ''
    name = 'default'
    queue = 'rkkr'

    # Define logger / notification application name:
    notification_name = 'BaseTask'
    logger_name = 'BaseTask'
    channel_name = 'notification'


    def run(self, *args, **kwargs) -> None:
        # Collect process ID:
        self.task_id = self.request.id
        # Logger initialization:
        self.logger = Logger(self.logger_name, self.task_id)
        # Notification initialization:
        self.notification = Notification(
            self.notification_name,
            self.task_id,
            self.channel_name)
        # Run task in delay:
        return self._run(*args, **kwargs)

    def _run(self, *args, **kwargs) -> bool:
        return True

    def _start_timer(self) -> None:
        """
        Start task execution time counting.
        """

        # Start timer:
        self._start_time = time.perf_counter()

    def _end_timer(self) -> float:
        """
        End task execution time counting.
        """

        # Finish clock count & method execution time:
        finish_time = time.perf_counter()
        # Return execution timer value:
        return round(finish_time - self._start_time, 5)

    def _check_output_status(self, output) -> bool:
        if output == {} or output == [] or output is None or output is False:
            return False
        else:
            return True
