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
   
def http_template_execution(host: Host,
    connection_template: ConnectionTemplate,
    con: Connection):

    # Collect host related data:
    if host.platform:
        host_default_params = host.platform.api_default_params
    else:
        host_default_params = {}
    # Collect template data:
    template_http_method = connection_template.get_http_method_display()
    template_http_url = connection_template.http_url
    template_http_params = connection_template.http_params
    template_http_body = connection_template.http_body
    # Combine collected param data:
    http_params = combine_data(template_http_params, host_default_params)
    # Execute template:
    output = con.connection(
        template_http_method,
        template_http_url,
        http_params)
    # Return HTTPS request output:
    return output

def http_templates_execution(host: Host,
    connection_templates: list[ConnectionTemplate]):

    # Collect host related data:
    if host.platform:
        host_default_header = host.platform.api_default_header
    else:
        host_default_header = {}
    # Create HTTP connection:
    if host_default_header:
        con = Connection(host, host_default_header)
    else:
        con = Connection(host)
    # Execute template:
    collected_outputs = {}
    # Iterate thru all provided templates:
    for template in connection_templates:
        # Collect output from template execution:
        output = http_template_execution(
            host, template, con)
        # Add output to collected output variable:
        collected_outputs[template] = output
    # Return all collected template outputs:
    return collected_outputs

# Test taks class:
class ConnectionBaseTask(BaseTask):
    """
    Xxx.
    """
        
    def _http_connections(self,
    hosts: list[Host],
    connection_templates: list[ConnectionTemplate]):
        
        
        # Execute devices:
        collected_outputs = {}
        # Iterate thru all provided devices:
        for host in hosts:
            # Collect output from device templates executions:
            output = http_templates_execution(
                host, connection_templates)
            # Add output to collected output variable:
            collected_outputs[host] = output

        return collected_outputs
