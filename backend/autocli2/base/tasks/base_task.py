# Python - library import:
import time

# AutoCli2 - task import:
from autocli2.celery import app

# AutoCli2 - notification import:
from notification.notification import Notification
from notification.logger import Logger


# Base task class
class BaseTask(app.Task):

    # Abstract task:
    abstract = True

    def init_task(self) -> None:
        # Collect process ID:
        self.task_id = self.request.id
        # Logger initialization:
        self.logger = Logger(self.name, self.task_id)
        # Notification initialization:
        self.notification = Notification(
            self.name,
            self.task_id,
            self.name)


    def _start_timer(self) -> float:
        """
        Start task execution time counting.
        """

        # Start timer:
        return time.perf_counter()

    def _end_timer(self, start_time) -> float:
        """
        End task execution time counting.
        """

        # Finish clock count & method execution time:
        finish_time = time.perf_counter()
        # Return execution timer value:
        return round(finish_time - start_time, 5)

    def _check_output_status(self, output) -> bool:
        if output == {} or output == [] or output is None or output is False:
            return False
        else:
            return True

    # Helper function:
    def _combine_data(self, first, second) -> dict:
        # Check if provided data belongs to dictionary instance:
        if not isinstance(first, dict):
            first = None
        if not isinstance(second, dict):
            second = None
        # Combine provided data if valid:
        if first and second:
            # Combine provided data:
            second.update(first)
            # Return combined data:
            return second
        elif first:
            return first
        elif second:
            return second
        else:
            return {}
