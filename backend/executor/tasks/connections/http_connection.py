# AutoCli2 - base task import:
from .create_execution import CreateExecutionBaseTask

# AutoCli2 - connections model import:
from executor.connections.http_connection import Connection

# AutoCli2 - connector model import:
from connector.models.connection_template import ConnectionTemplate

# AutoCli2 - inventory models import:
from inventory.models.host import Host

# AutoCli2 - executor models import:
from executor.models.executor import Executor


# Test taks class:
class HttpConnectionBaseTask(CreateExecutionBaseTask):
    """
    Base HTTP(S) connection class.
    """

    def _device_http_execution(self,
        host: Host,
        connection_templates: list[ConnectionTemplate],
        executor: Executor) -> tuple:
        """
        Xxx.

        [Int = Positive result, Int = Amount of connection templates]
        """
            
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
            template_http_method = template.http_method
            template_http_url = template.http_url
            template_http_params = template.http_params
            # Combine collected param data:
            http_params = self._combine_data(template_http_params, host_default_params)
            # Execute template:
            output = con.connection(
                template_http_method,
                template_http_url,
                http_params)
            # Create execution object:
            self._create_execution_object(host, template, executor, con, output)
            # Check connection response status:
            if con.response_status:
                positive_result += 1
        # Return connection status count:
        return (positive_result, len(connection_templates))
