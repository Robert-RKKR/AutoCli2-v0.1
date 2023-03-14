# Python - libraries import:
import urllib.request
import threading
import datetime
import zipfile
import csv
import os

# AutoCli2 - base task import:
from autocli2.base.tasks.create_execution import CreateExecutionBaseTask

# AutoCli2 - executor class import:
from executor.connections.ssh_connection import Connection

# AutoCli2 - connector model import:
from connector.models.connection_template import ConnectionTemplate

# AutoCli2 - inventory models import:
from inventory.models.host import Host

# AutoCli2 - executor models import:
from executor.models.execution import Execution
from executor.models.executor import Executor

# AutoCli2 - management import:
from management.settings import collect_global_settings


# Test taks class:
class SshConnectionBaseTask(CreateExecutionBaseTask):
    """
    Xxx.
    """

    def _device_ssh_execution(self,
        host: Host,
        connection_templates: list[ConnectionTemplate],
        executor: Executor) -> tuple:
        """ Xxx. """

        raise NotImplementedError('SSH is not implemented yet')
