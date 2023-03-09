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
class HttpConnectionBaseTask(BaseTask, CreateExecutionBaseTask):
    """
    Xxx.
    """

    def _device_http_execution(self,
        host: Host,
        connection_templates: list[ConnectionTemplate],
        executor: Executor) -> tuple:
        """ Xxx. """
            
        # Collect default header / params values from host object:
        if host.platform:
            host_default_header = host.platform.api_default_header
            host_default_params = host.platform.api_default_params
        else:
            host_default_header = {}
            host_default_params = {}
        # Create HTTP connection:
        if host_default_header:
            con = Connection(host, host_default_header)
        else:
            con = Connection(host)

        # Count template execution:
        positive_result = 0
        # Iterate thru all provided templates:
        for template in connection_templates:
            # Collect template data:
            template_http_method = template.get_http_method_display()# type: ignore
            template_http_url = template.http_url
            template_http_params = template.http_params
            # Combine collected param data:
            http_params = self._combine_data(template_http_params, host_default_params)
            # Execute template:
            output = con.connection(
                template_http_method,
                template_http_url,# type: ignore
                http_params)
            # Collect host, credentials and template representations:
            representation = self._collect_execution_data(
                host, template)
            # Collect execution data:
            execution_data = {
                'executor': executor,
                'host': host,
                'connection_template': template,
                'credential': host.credential,
                'task_id': self.task_id,
                'execution_status': con.status,
                'https_response_status': con.status,
                'https_response_code': con.response_code,
                'https_response': 'output',
                'host_representation':
                 representation['host_representation'],
                'connection_template_representation': 
                 representation['connection_template_representation'],
                'credential_representation':
                 representation['credential_representation']}
            try: # Try to create a new execution object:
                Execution.objects.create(**execution_data)
            except:
                self.logger.error(
                    'An error has occurred during the creation of a new '\
                    f'execution object.')
            # Check connection status:
            if con.status:
                positive_result += 1
        # Return connection status count:
        return (positive_result, len(connection_templates))
