# Python import:
import urllib.request
import threading
import datetime
import zipfile
import csv
import os

# Base task import:
from .create_execution import CreateExecutionBaseTask
from .base_task import BaseTask

# Connection class import:
from executor.connections.http_connection import Connection

# Connections model import:
from connector.models.connection_template import ConnectionTemplate

# Inventory models import:
from inventory.models.host import Host

# Executors models import:
from executor.models.execution import Execution
from executor.models.executor import Executor

# Settings import:
from management.settings import collect_global_settings


# Test taks class:
class SshConnectionBaseTask(BaseTask, CreateExecutionBaseTask):
    """
    Xxx.
    """

    def _device_ssh_execution(self,
        host: Host,
        connection_templates: list[ConnectionTemplate],
        executor: Executor) -> tuple:
        """ Xxx. """

        raise NotImplementedError('SSH is not implemented yet')
