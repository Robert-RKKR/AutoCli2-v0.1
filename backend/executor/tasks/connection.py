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
from inventory.models.credentials import Credential
from inventory.models.host import Host

# Helper function:
def combine_data(first, second):
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
        return False
   

# Test taks class:
class ConnectionBaseTask(BaseTask):
    """
    Xxx.
    """

    def _http_connection(self,
        connection_templates: ConnectionTemplate,
        credential: Credential,
        host: Host):

        # Collect host related data:
        if host.platform:
            self.host_default_header = host.platform.api_default_header
            self.host_default_params = host.platform.api_default_params
        else:
            self.host_default_header = None
            self.host_default_params = None

        # Collect template data:
        self.template_http_method = connection_templates.http_method
        self.template_http_url = connection_templates.http_url
        self.template_http_header = connection_templates.http_header
        self.template_http_params = connection_templates.http_params
        self.template_http_body = connection_templates.http_body
        # Combine collected heder data:
        self.http_header = combine_data(self.template_http_header, self.host_default_header)
        # Combine collected param data:
        self.http_params = combine_data(self.template_http_params, self.host_default_params)
        # Create connection:
        if self.http_header:
            con = Connection(host, self.http_header)
        else:
            con = Connection(host)
