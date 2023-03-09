# Python import:
import urllib.request
import threading
import datetime
import zipfile
import csv
import os

# Base task import:
from .base_task import BaseTask

# Connections model import:
from connector.models.connection_template import ConnectionTemplate

# Inventory models import:
from inventory.models.host import Host

# Executors models import:
from executor.models.execution import Execution

# Settings import:
from management.settings import collect_global_settings


# Test taks class:
class CreateExecutionBaseTask(BaseTask):
    """
    Xxx.
    """

    def _create_execution_object(self,
        host, template, executor, con, output):
        """
        Create execution object based on provided and collected data.
        """

        # Collect host data collection protocol:
        data_collection_protocol = host.data_collection_protocol
        # Collect host, credentials and template representations:
        representation = self._collect_execution_data(
            host, template, data_collection_protocol)
        # Collect data based on connection protocol type (HTTP/SSH)::
        if data_collection_protocol == 1:
            execution_data = {
                'ssh_raw_data_status': con.raw_data_status,
                'ssh_processed_data_status': con.processed_data_status,
                'ssh_raw_data': con.raw_data,
                'ssh_processed_data': con.processed_data}
        elif data_collection_protocol == 2:
            execution_data = {
                'https_response_code': con.response_code,
                'https_response': output}
        # Collect execution data:
        execution_data.update({
            'executor': executor,
            'host': host,
            'connection_template': template,
            'credential': host.credential,
            'task_id': self.task_id,
            'execution_status': con.status,
            'host_representation':
                representation['host_representation'],
            'connection_template_representation': 
                representation['connection_template_representation'],
            'credential_representation':
                representation['credential_representation']})
        try: # Try to create a new execution object:
            execution_object = Execution.objects.create(**execution_data)
        except:
            self.logger.error(
                'An error has occurred during the creation of a new '\
                f'execution object.')
            # Return False if object was not created:
            return False
        else:
            # Return created execution object:
            return execution_object
    
    def _collect_execution_data(self,
        host, template, data_collection_protocol) -> dict:
        """
        Collect objects representations.
        """

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
        if data_collection_protocol == 1:
            connection_template_representation = f'{template.name}: '\
                f'{template.ssh_command}'
        elif data_collection_protocol == 2:
            connection_template_representation = f'{template.name}: '\
                f'{template.http_url}'
        else:
            connection_template_representation = None
        # Collect host representation:
        host_representation = f'{host.name}: {host.hostname}'
        # Return representations:
        return {
            'credential_representation': credential_representation,
            'connection_template_representation': connection_template_representation,
            'host_representation': host_representation}
