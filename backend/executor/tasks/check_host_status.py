# Celery - application import:
from autocli2.celery import app

# AutoCli2 - base task import:
from autocli2.base.tasks.connection import ConnectionBaseTask

# AutoCli2 - HTTP Connection class import:
from executor.connections.http_connection import Connection


# Check host status task class:
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

    def _run(self, test, *args, **kwargs) -> None:
        print('===(CheckHostStatusTask)===> ', test)

# Task registration:
check_host_status_task = app.register_task(CheckHostStatusTask())# type: ignore
