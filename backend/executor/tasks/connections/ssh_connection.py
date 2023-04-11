# Python - libraries import:
import urllib.request
import threading
import datetime
import zipfile
import csv
import os

# AutoCli2 - base task import:
from .create_execution import CreateExecutionBaseTask

# AutoCli2 - connector model import:
from connector.models.connection_template import ConnectionTemplate

# AutoCli2 - inventory models import:
from inventory.models.host import Host

# AutoCli2 - executor models import:
from executor.models.executor import Executor


# Test taks class:
class SshConnectionBaseTask(CreateExecutionBaseTask):
    """
    Xxx.
    """

    def _device_ssh_execution(self,
        host: Host,
        connection_templates: list[ConnectionTemplate],
        executor: Executor) -> tuple:
        """
        Xxx.
        [Int = Positive result, Int = Amount of connection templates]
        """

        # Count template execution:
        positive_result = 0

        # Return connection status count:
        return (positive_result, len(connection_templates))
