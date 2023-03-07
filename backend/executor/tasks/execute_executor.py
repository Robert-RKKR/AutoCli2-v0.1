# Celery application import:
from autocli2.celery import app

# Base task import:
from .connection import ConnectionBaseTask

# Connection class import:
from executor.connections.http_connection import Connection

# Executors models import:
from executor.models.executor import Executor

# Task import:
from executor.tasks.check_host_status import CheckHostStatusTask
from executor.tasks.collect_host_data import CollectHostDataTask


# Test taks class:
class ExecuteExecutorTask(ConnectionBaseTask):
    """
    Xxx.
    """

    # Basic task information:    
    name = 'Execute executor'
    description = 'Xxx.'
    queue = 'execution'

    # Define logger / notification application name:
    notification_name = 'ConnectionExecutor'
    logger_name = 'ConnectionExecutor'
    channel_name = 'execution'

    def _run(self, executor_id, *args, **kwargs) -> None:
        try: # Try to collect executor:
            executor = Executor.objects.get(pk=executor_id)
        except:
            self.logger.error(
                f'Executor object with ID: {executor_id}, has not been found.')
        else:
            # Check executor type:
            if executor.executor_type == 1:
                # Collect execution data:
                task_id = executor.task
                task_arguments = executor.task_arguments
                # Rune provided task:
                if task_id == 1:
                    CollectHostDataTask(task_arguments)# type: ignore
                elif task_id == 2:
                    CheckHostStatusTask(task_arguments)# type: ignore
            elif executor.executor_type == 2:
                # Collect executor data:
                hosts = executor.hosts.all()
                connection_templates = executor.connection_templates.all()
                # Execute template:
                self.singlethreading_connection(
                    hosts, connection_templates, executor)
            else:
                self.logger.error(
                    'Executor object contains unsupported  "executor_type" '\
                    f'value: {executor.executor_type}.', executor)

# Task registration:
ExecuteExecutorTask = app.register_task(ExecuteExecutorTask())# type: ignore
