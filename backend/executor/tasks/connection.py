# Python import:
import urllib.request
import datetime
import zipfile
import csv
import os

# Base task import:
from autocli2.base.tasks.base_task import BaseTask

# Connection class import:
from executor.connections.http_connection import Connection

# Connections model import:
from connector.models.connection_template import ConnectionTemplate

# Inventory models import:
from inventory.models.host import Host

# Executors models import:
from executor.models.execution import Execution
from executor.models.executor import Executor

# Django exception import:
from django.db import IntegrityError

# Settings import:
from management.settings import collect_global_settings

# Helper function:
def combine_data(first, second) -> dict:
    # Check if provided data belongs to dictionary instance:
    if not isinstance(first, dict):
        first = None
    if not isinstance(second, dict):
        second = None
    # Combine provided data if valid:
    if first and second:
        # Combine provided data:
        second.update(first)
        # Return combined data:
        return second
    elif first:
        return first
    elif second:
        return second
    else:
        return {}


# Test taks class:
class ConnectionBaseTask(BaseTask):
    """
    Abstract connection task that includes the basic functionality of HTTP(S)
    and SSH connections, for other tasks.
    """
        
    def singlethreading_connection(self,
        hosts: list[Host],
        connection_templates: list[ConnectionTemplate],
        executor: Executor):
        
        # Iterate thru all provided devices:
        for host in hosts:
            self._device_execution(
                host, connection_templates, executor)

    def multithreading_connection(self,
        hosts: list[Host],
        connection_templates: list[ConnectionTemplate],
        executor: Executor):

        raise NotImplementedError('Multithreading connection is not implemented yet')

    def _device_execution(self,
        host: Host,
        template: list[ConnectionTemplate],
        executor: Executor):

            # Collect default header from host object:
            if host.platform:
                host_default_header = host.platform.api_default_header
            else:
                host_default_header = {}
            # Collect default params from host object:
            if host.platform:
                host_default_params = host.platform.api_default_params
            else:
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
                # Collect template execution protocol:
                execution_protocol = template.execution_protocol
                # Execute template using SSH protocol:
                if execution_protocol == 1:
                    result = self._ssh_template_execution(
                        con, host, template, executor)
                # Execute template using HTTP(S) protocol:
                elif execution_protocol == 2:
                    result = self._http_template_execution(
                        con, host, template, executor)
                else: # Log error:
                    self.logger.error(
                        'Template object contains unsupported  "execution_protocol" '\
                        f'value: {execution_protocol}.', template)
                # Check connection status:
                if result:
                    positive_result += 1

    def _ssh_template_execution(self,
        host: Host,
        template: ConnectionTemplate,
        executor: Executor):

        raise NotImplementedError('SSH is not implemented yet')

    def _http_template_execution(self,
        con: Connection,
        host: Host,
        template: ConnectionTemplate,
        executor: Executor):

            # Collect template data:
            template_http_method = template.get_http_method_display()
            template_http_url = template.http_url
            template_http_params = template.http_params
            # Combine collected param data:
            http_params = combine_data(template_http_params, host_default_params)
            # Execute template:
            output = con.connection(
                template_http_method,
                template_http_url,
                http_params)
            # Collect object representation:
            if host.credential:
                credential_name = host.credential.name
                credential_username = host.credential.name
                credential_representation = f'{credential_name}: '\
                    f'{credential_username}'
            else:
                credential_representation = collect_global_settings(
                    'default_user')
            if template.ssh_command:
                connection_template_representation = f'{template.name}: '\
                    f'{template.ssh_command}'
            else:
                connection_template_representation = f'{template.name}: '\
                    f'{template.http_url}'
            host_representation = f'{host.name}: {host.hostname}'
            # Collect execution data:
            execution_data = {
                'executor': executor,
                'host': host,
                'connection_template': template,
                'credential': host.credential,
                'task_id': self.task_id,
                'execution_status': con.status,
                'https_response_statusTESTTESTTESTTESTTEST': con.status,
                'https_response_code': con.response_code,
                'https_response': output,
                'host_representation': host_representation,
                'connection_template_representation': 
                 connection_template_representation,
                'credential_representation': credential_representation}
            try: # Try to create a new execution object:
                execution = Execution.objects.create(**execution_data)
            except IntegrityError as error:
                self.logger.error(
                    'An error has occurred during the creation of a new '\
                    f'execution object. Error: {error}')
            # Return template execution result:
            return con.status
