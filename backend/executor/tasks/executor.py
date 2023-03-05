# Celery application import:
from autocli2.celery import app

# Base task import:
from .connection import ConnectionBaseTask

# Connection class import:
from executor.connections.http_connection import Connection

# Executors models import:
from executor.models.execution import Execution
from executor.models.executor import Executor


# Test taks class:
class ExecutorTask(ConnectionBaseTask):
    """
    Xxx.
    """

    # Basic task information:    
    name = 'Executor'
    description = 'Xxx.'
    queue = 'execution'

    # Define logger / notification application name:
    notification_name = 'ConnectionExecutor'
    logger_name = 'ConnectionExecutor'
    channel_name = 'execution'

    def _run(self, executor: Executor, *args, **kwargs) -> None:
        # Check provided data:
        if not isinstance(executor, Executor):
            raise TypeError('Provided executor object is not a valid Executor '\
            f'object. Provided: "{executor}"')
        print('======> ', executor)

# Task registration:
# task = app.register_task(ExecutorTask())
