# Python import:
import urllib.request
import threading
import datetime
import zipfile
import csv
import os

# Base task import:
from .http_connection import HttpConnectionBaseTask
from .ssh_connection import SshConnectionBaseTask

# Connections model import:
from connector.models.connection_template import ConnectionTemplate

# Inventory models import:
from inventory.models.host import Host

# Executors models import:
from executor.models.executor import Executor


# Test taks class:
class ConnectionBaseTask(HttpConnectionBaseTask, SshConnectionBaseTask):
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

        # Collect host data collection protocol:
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
