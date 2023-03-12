# Celery application import:
from autocli2.celery import app

# Base task import:
from autocli2.base.tasks.connection import ConnectionBaseTask

# Connection class import:
from executor.connections.http_connection import Connection


# Test taks class:
class CollectHostDataTask(ConnectionBaseTask):
    """
    Xxx.
    """

    # Basic task information:    
    name = 'Correlate collected data'
    description = 'Correlate data collected from device, into database.'
    queue = 'collect_data'

    # Define logger / notification application name:
    notification_name = 'CollectHostDataTask'
    logger_name = 'CollectHostDataTask'
    channel_name = 'collect_data'

    def _run(self, test, *args, **kwargs) -> None:
        print('===(CollectHostDataTask)===> ', test)

# Task registration:
collect_host_data_task = app.register_task(CollectHostDataTask())
