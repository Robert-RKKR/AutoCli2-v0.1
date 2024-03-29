# AutoCli2 - base task import:
from .create_execution import ExecutionBaseTask

# AutoCli2 - connections model import:
from executor.connections.http_connection import Connection

# AutoCli2 - connector model import:
from connector.models.connection_template import ConnectionTemplate

# AutoCli2 - inventory models import:
from inventory.models.host import Host

# AutoCli2 - executor models import:
from executor.models.executor import Executor


# Test taks class:
class HttpConnectionBaseTask(ExecutionBaseTask):
    """
    Base HTTP(S) connection class.
    """

    def _single_host_http_execution(self,
        host: Host,
        connection_templates: list[ConnectionTemplate],
        executor: Executor) -> tuple:
        """
        Xxx.

        [Int = Positive result, Int = Amount of connection templates]
        """
            
        # Collect default header / params values from host object:
        if host.platform:
            host_default_header = host.platform.http_default_header
            host_default_params = host.platform.http_default_params
        else:
            host_default_header = {}
            host_default_params = {}
        # Create HTTP connection:
        if host_default_header:
            con = Connection(host, host_default_header)
        else:
            con = Connection(host)
        # Start connection:
        con.start_connection()
        # Count template execution:
        positive_result = 0
        # Iterate thru all provided templates:
        for template in connection_templates:
            # Collect template data:
            template_http_method = template.http_method
            template_http_url = template.http_url
            template_http_params = template.http_params
            template_http_body = template.http_body
            # Fill tamplet body with data:
            template_http_body = self._fill_tamplet_data(
                template_http_body, host)
            # Combine collected param data:
            http_params = self._combine_data(
                template_http_params, host_default_params)
            # Execute template:
            output = con.connection(
                method=template_http_method,
                url=template_http_url,
                parameters=http_params,
                body=template_http_body)
            # Add output to collected data: !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            if self.all_collected_data.get('collected', None):
                self.all_collected_data['collected'][template.pk] = output
            else:
                self.all_collected_data['collected'] = {
                    template.pk: output}
            # Create execution object:
            self._create_execution_object(
                host, template, executor, con, output)
            # Check connection response status:
            if con.response_status:
                positive_result += 1
        # Return connection status count:
        return (positive_result, len(connection_templates))
        