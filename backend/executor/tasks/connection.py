# Python import:
import urllib.request
import threading
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
        """ 
        Single-threading connection method is responsible for collecting
        data from single remote hosts at the same time.
        """
        
        # Start timer:
        start_timer = self._start_timer()
        # Collect host execution status:
        positive_result = 0
        # Iterate thru all provided devices:
        for host in hosts:
            # Execute all provided templates on current host:
            output = self._device_execution(
                host, connection_templates, executor)
            # Increase positive results when output is True:
            if output:
                positive_result += 1
        # End timer:
        end_time = self._end_timer(start_timer)
        # Create user notification:
        if positive_result > 0:
            # Creative user notification for one or more positive results:
            self.notification.info(
                f'The data collection process running on the {len(hosts)} '\
                'device/s was successful. Data has been collected '\
                f'from {positive_result} device/s.', executor,
                execution_time=end_time)
        else:
            # Creative user notification in the absence of positive results:
            self.notification.warning(
                f'The data collection process running on the {len(hosts)} '\
                'device/s was unsuccessful. No data was collected.', executor,
                execution_time=end_time)

    def multithreading_connection(self,
        hosts: list[Host],
        connection_templates: list[ConnectionTemplate],
        executor: Executor):
        """ 
        Multi-threading connection method is responsible for collecting data
        from multiple remote hosts at the same time.
        """

        # Define threads list:
        threads = list()
        # Iterate thru all provided devices:
        for host in hosts:
            # Run thread:
            thread = threading.Thread(target=self._device_execution,
                args=(host, connection_templates, executor))
            # Add current thread to threads list:
            threads.append(thread)
            # Start current thread:
            thread.start()

        # Wait to end of all threads execution:
        for index, thread in enumerate(threads):
            thread.join()

    def _device_execution(self,
        host: Host,
        connection_templates: list[ConnectionTemplate],
        executor: Executor) -> bool:
        """ 
        The device execution method is responsible for verifying the
        protocol used to connect to the remote host.
        """

        # Start timer:
        start_timer = self._start_timer()

        # Check host data collection protocol:
        data_collection_protocol = host.data_collection_protocol
        # Start HTTP / SSH connection process:
        if data_collection_protocol == 1:
            output = self._device_ssh_execution(
                host, connection_templates, executor)
        elif data_collection_protocol == 2:
            output = self._device_http_execution(
                host, connection_templates, executor)
        else: # Log error:
            self.logger.error(
                'Host object contains unsupported  "data_collection_protocol" '\
                f'value: {data_collection_protocol}.', host)
            # Return false results:
            return False
            
        # End timer:
        end_time = self._end_timer(start_timer)
        # Collect template output data:
        collected_templates = output[0]
        templates = output[1]
        # Check if template execution process was successful:
        if collected_templates > 0:
            # Creative user notification for one or more positive results:
            self.notification.info(
                f'The template collection process running on the {host.name} '\
                f'device was successful. {collected_templates} template/s '\
                f'were collected from {templates} available.', host,
                execution_time=end_time)
            # Return positive results:
            return True
        else:
            # Creative user notification in the absence of positive results:
            self.notification.warning(
                f'The template collection process running on the {host.name} '\
                'device was unsuccessful. No data was collected.', host,
                execution_time=end_time)
            # Return false results:
            return False

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
            http_params = combine_data(template_http_params, host_default_params)
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

    def _device_ssh_execution(self,
        host: Host,
        connection_templates: list[ConnectionTemplate],
        executor: Executor) -> tuple:
        """ Xxx. """

        raise NotImplementedError('SSH is not implemented yet')
    
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
