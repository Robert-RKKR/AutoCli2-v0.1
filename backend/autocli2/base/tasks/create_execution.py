# Python import:
import urllib.request
import threading
import datetime
import zipfile
import csv
import os

# Base task import:
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
class CreateExecutionBaseTask(BaseTask):
    """
    Xxx.
    """
    
    def _collect_execution_data(self,
        host: Host,
        template: ConnectionTemplate) -> dict:
        """ Collect objects representations. """

        # Collect host credential representation:
        if host.credential:
            credential_name = host.credential.name
            credential_username = host.credential.name
            credential_representation = f'{credential_name}: '\
                f'{credential_username}'
        else:
            credential_representation = collect_global_settings(
                'default_user')
        # Collect template representation:
        if template.ssh_command:
            connection_template_representation = f'{template.name}: '\
                f'{template.ssh_command}'
        else:
            connection_template_representation = f'{template.name}: '\
                f'{template.http_url}'
        # Collect host representation:
        host_representation = f'{host.name}: {host.hostname}'
        # Return representations:
        return {
            'credential_representation': credential_representation,
            'connection_template_representation': connection_template_representation,
            'host_representation': host_representation}
