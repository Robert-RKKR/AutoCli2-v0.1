# Celery application import:
from autocli2.celery import app

# Base task import:
from .connection import ConnectionBaseTask

# Connection class import:
from executor.connections.http_connection import Connection


# Test taks class:
class CheckHostStatusTask(ConnectionBaseTask):
    """
    Xxx.
    """

    # Basic task information:    
    name = 'Check host status'
    description = 'Check host/s status, using SSH / HTTP(S) protocol.'
    queue = 'status_check'

    # Define logger / notification application name:
    notification_name = 'CheckHostStatus'
    logger_name = 'CheckHostStatus'
    channel_name = 'status_check'

    def _run(self, pks: list[int], *args, **kwargs) -> None:
        # Check provided data:
        if isinstance(pks, list):
            for pk in pks:
                if not isinstance(pk, int):
                    raise TypeError('The provided pk variable '\
                    f'must be list of strings. Provided: "{pk}"')
        else:
            raise TypeError('The provided pk variable '\
            f'must be list of strings. Provided: "{pks}"')
        # T

# Task registration:
CheckHostStatusTask = app.register_task(CheckHostStatusTask())
