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

    def _run(self, executor_id, *args, **kwargs) -> None:
        try: # Try to collect executor:
            executor = Executor.objects.get(pk=executor_id)
        except:
            pass # Pass for now.
        else:
            # Check executor type:
            if executor.executor_type == 1:
                pass
            elif executor.executor_type == 2:
                # Collect executor data:
                hosts = executor.hosts.all()
                connection_templates = executor.connection_templates.all()
                # Execute template:
                self._http_connections(
                    hosts, connection_templates, executor)

# Task registration:
ExecutorTask = app.register_task(ExecutorTask())
