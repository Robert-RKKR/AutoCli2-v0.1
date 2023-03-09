# Python Import:
import requests
import xmltodict
import json
import time

# Logger import:
from notification.logger import Logger

# Application Import:
from inventory.models.host import Host

# Settings import:
from management.settings import collect_global_settings

# Constance:
METHODS = [
    'GET',
    'POST'
]


# HTTP connection class:
class Connection:
    
    # Logger class initiation:
    logger = Logger('SSH connection')

    def __init__(self, host: Host, headers: dict = {}) -> None:
        """
        Xxx.

        Class attributes:
        -----------------
        Host: Host object
            Xxx.

        Methods:
        --------
        xxx: (url, connectionType='GET', payload=None)
            Xxx
        """
        
        # Verify if the host variable is a valid host object:
        if not isinstance(host, Host):
            raise TypeError('The provided host must be instance of Host class.')
        # Verify if the headers variable is a valid sting:
        if not isinstance(headers, dict) and not headers is None:
            raise TypeError('The provided headers variable must be dictionary.')

        # Collect data from host object:
        self.__host = host
        self.hostname = host.hostname
        self.http_port = host.http_port
        self.certificate = host.certificate_check

        # Collect data from host credentials object:
        if host.credential:
            self.token = host.credential.token
            self.username = host.credential.username
            self.password = host.credential.password
        else:
            self.token = None
            self.username = collect_global_settings('default_user')
            self.password = collect_global_settings('default_password')

        # Headers declaration:
        self.headers = headers

        # Connection status:
        self.raw_data_status = False
        self.processed_data_status = False
        self.raw_data = None
        self.processed_data = None

        # Execution timer:
        self.execution_time = None

    @property
    def host(self):
        return self.__host