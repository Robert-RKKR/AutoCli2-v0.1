# Python - libraries import:
import requests
import xmltodict
import urllib3
import json
import time

# AutoCli2 - Settings import:
from management.settings import collect_global_settings

# AutoCli2 - Logger import:
from notification.logger import Logger

# AutoCli2 - other model import:
from inventory.models.host import Host

# AutoCli2 - management model import:
from management.settings import collect_global_settings

# AutoCli2 - constance import:
from autocli2.base.constants.execution_type import HttpExecutionTypeChoices

# Disable ssl warnings:
urllib3.disable_warnings()


# HTTP connection class:
class Connection:

    def __init__(self,
        host: Host,
        header: dict = {},
        task_id: str = None) -> None:
        """
        The HTTP(S) connection class uses requests library,
        to connect with Https server for API connections.

        Class attributes:
        -----------------
        Host: Host object
            The host used to establish the HTTP(S) connection.
        heder: dictionary
            Header that will be added to HTTP(S) request.
        task_id: str
            Celery task ID.

        Methods:
        --------
        connection:
            Universal method that require the HTTP(S) method to be
            executed (GET, POST ...).
        get:
            GET request method for HTTP(S) connection.
        """
        
        # Verify if the host variable is a valid host object:
        if not isinstance(host, Host):
            raise TypeError('The provided host must be instance of Host class.')
        # Verify if the header variable is a valid sting:
        if not isinstance(header, dict) and not header is None:
            raise TypeError('The provided header variable must be dictionary.')
    
        # Logger class initiation:
        self.logger = Logger('HTTP(S) connection', task_id)

        # Collect data from host object:
        self.__host = host
        self.hostname = host.hostname
        self.http_port = host.http_port
        self.certificate = host.certificate_check

        # Collect data from host credentials object:
        self.token = host.credential.token
        self.username = host.credential.username
        self.password = host.credential.password

        # Collect data from host platform object:
        self.http_token_heder_key = host.platform.http_token_heder_key
        self.http_token_heder_value = host.platform.http_token_heder_value
        self.http_pagination = host.platform.http_pagination
        self.http_next_page_code_path = host.platform.http_next_page_code_path
        self.http_next_page_link_path = host.platform.http_next_page_link_path
        self.http_pagination_param_key = host.platform.http_pagination_param_key
        self.http_data_path = host.platform.http_data_path
        self.http_default_header = host.platform.http_default_header
        self.http_default_params = host.platform.http_default_params

        # header declaration:
        self.header = header

        # Connection status declaration:
        self.connection_status = False

        # Response declaration:
        self.converted_response = None
        self.response_code = None

        # Response status declaration:
        self.response_status = False
        self.xml_response_status = None
        self.json_response_status = None

        # Execution timer declaration:
        self.execution_time = None

        # Timeout declaration:
        self.connection_timeout = collect_global_settings('http_timeout')

    def __enter__(self) -> 'Connection':
        """
        Use Connection class with python 'with' command:
        'with Connection(host) as con:
            results = con.get('/api/v2/hosts')'
        
        Return:
        --------
            Connection class object.
        """
        
        try: # Try to start HTTP(S) connection:
            response = self.start_connection()
            if not response:
                return False
        except:
                return False
        else:
            # In case of success,
            # return Connection class object:
            return self

    def __exit__(self,
        exc_type,
        exc_value,
        exc_traceback) -> None:

        # End HTTP(S) connection:
        self.session.close()

    def start_connection(self) -> 'Connection':
        """
        Start a new HTTP(S) session.

        Return:
        --------
        Connection class object.
        """

        # Create http session declaration:
        self.session = requests.Session()
        
        # Execute test connection:
        if self.test_connection():
            self.connection_status = True
            return self
        else:
            return False

    @property
    def host(self):
        return self.__host

    def __repr__(self) -> str:
        """
        Connection class representation.
        """
        return f'<Class HTTP(S) connection ({self.hostname}:{self.http_port})>'
    
    def test_connection(self) -> bool:
        """
        Execute tes HTTP connection.
        """

        # Prepare test request:
        request_url = f'https://{self.hostname}:{self.http_port}'
        # Execute test connection:
        response = self._connection('GET', request_url, None, True)
        # If connection return status code from 1 to 299 return True:
        if self.response_status:
            return True
        else: # If not return False:
            return False
    
    def connection(self, method: str, url: str, parameters: dict = {}):
        """
        Universal method that require the HTTP(S) method to be
        executed (GET, POST ...).

        Parameters:
        -----------------
        method: string
            HTTP connection method (GET, POST, DELETE ...).
        url: string
            URL string that will be used when requesting the API.
        parameters: dictionary
            Dictionary containing additional parameters, formatted as specified:
            {'Key': 'Value', ...}
        """

        # Check if provided HTTP method is valid:
        if method in HttpExecutionTypeChoices:
            # Collect method:
            method = HttpExecutionTypeChoices.value_from_int(method)
            # Execute HTTP(S) request:
            return self._connection_center(method, url, parameters)
        else:
            raise NotImplementedError(
                f'Provided HTTP(S) method "{method}", is not supported')

    def get(self, url: str, parameters: dict = {}):
        """
        GET request method for HTTP(S) connection.

        Parameters:
        -----------------
        url: string
            URL string that will be used when requesting the API.
        parameters: dictionary
            Dictionary containing additional parameters, formatted as specified:
            {'Key': 'Value', ...}
        """

        # Execute HTTP(S) request:
        return self._connection_center('GET', url, parameters)
    
    def post(self, url: str, parameters: dict = {}):
        """
        POST request method for HTTP(S) connection.

        Parameters:
        -----------------
        url: string
            URL string that will be used when requesting the API.
        parameters: dictionary
            Dictionary containing additional parameters, formatted as specified:
            {'Key': 'Value', ...}
        """

        # Execute HTTP(S) request:
        return self._connection_center('POST', url, parameters)
    
    def put(self, url: str, parameters: dict = {}):
        """
        PUT request method for HTTP(S) connection.

        Parameters:
        -----------------
        url: string
            URL string that will be used when requesting the API.
        parameters: dictionary
            Dictionary containing additional parameters, formatted as specified:
            {'Key': 'Value', ...}
        """

        # Execute HTTP(S) request:
        return self._connection_center('PUT', url, parameters)
    
    def delete(self, url: str, parameters: dict = {}):
        """
        DELETE request method for HTTP(S) connection.

        Parameters:
        -----------------
        url: string
            URL string that will be used when requesting the API.
        parameters: dictionary
            Dictionary containing additional parameters, formatted as specified:
            {'Key': 'Value', ...}
        """

        # Execute HTTP(S) request:
        return self._connection_center('DELETE', url, parameters)

    def _connection_center(self, request_method, url, parameters, body=None):
        """
        Main connection hub responsible for collecting parameters and pagination
        data to generate URL.
        """

        # Check connection status:
        if self.connection_status:
            # Verify if the host url is a valid host object:
            if not isinstance(url, str):
                raise TypeError('The provided url variable must be string.')
            # Verify if the parameters variable is a dictionary:
            if not isinstance(parameters, dict) and not parameters is None:
                raise TypeError('The provided parameters variable '\
                    'must be list of dictionary.')
            else: # Verify parameters dictionary variable:
                for key in parameters:
                    if not isinstance(key, str):
                        raise TypeError('The provided key variable must be list '\
                            f'of dictionary. Received {key}')
                    if not isinstance(parameters[key], str):
                        raise TypeError('The provided key value variable must '\
                            f'be list of dictionary. Received {parameters[key]}')
            # Collect parameters:
            if parameters:
                url = self._add_parameters_to_url(url, parameters)
            # Paginate API request:

            # TEMPORARY:
            request_url = f'https://{self.hostname}:{self.http_port}/{url}'
            return self._connection(request_method, request_url, body)

    def _add_parameters_to_url(self, url, parameters) -> str:
        """
        Add provided parameter into URL string.
        """

        # Declaim first parameter bool value:
        first_parameter = True
        # Iterate thru all parameters:
        for parameter_key in parameters:
            # Collect parameter data:
            parameter_value = parameters[parameter_key]
            # Add parameter to URL:
            if first_parameter:
                url = f'{url}?{parameter_key}={parameter_value}'
                # Change first parameter value to False:
                first_parameter = False
            else:
                url = f'{url}&{parameter_key}={parameter_value}'
        # Return URL with parameters:
        return url

    def _add_token_to_heder(self) -> None:
        """
        Method to add a token to the header.
        """

        # Prepare token value:
        if self.http_token_heder_value:
            token_value = f'{self.http_token_heder_value} {self.token}'
        else:
            token_value = self.token
        # Add token heder to HTTP(S) heder:
        self.header[self.http_token_heder_key] = token_value

    def _connection(self,
            request_method, request_url, body, test = False) -> dict or list:
        """
        The main function of the connection class, responsible for
        sending the HTTP(S) request.
        """

        if self.connection_status or test:
            # Log the beginning of a new connection to the HTTP(S) server:
            self.logger.info('The initiation of a new HTTP(S) '\
                f'request to "{request_url}" has been started.', self.host)
            # Start clock count:
            start_time = time.perf_counter()
            # Connect to the host with password and username or by using token:
            if self.token:
                # Add token to HTTP(S) heder:
                self._add_token_to_heder()
                # Send HTTP(S) API request with heder token authorization:
                request = requests.Request(
                    request_method,
                    request_url,
                    headers=self.header,
                    data=body)
            else: # Send HTTP(S) API request with user and password authorization:
                request = requests.Request(
                    request_method,
                    request_url,
                    headers=self.header,
                    auth=(self.username, self.password),
                    data=body)
            # Confect session with request data:
            prepare_request = self.session.prepare_request(request)
            try: # Try to establish a connection to a host:
                response = self.session.send(
                    prepare_request,
                    verify=self.certificate,
                    timeout=self.connection_timeout)
            except requests.exceptions.SSLError as exception:
                self.logger.error(str(exception), self.host)
                # Change connection status to False:
                self.response_status = False
                return self.response_status
            except requests.exceptions.Timeout as exception:
                self.logger.error(str(exception), self.host) 
                # Change connection status to False:
                self.response_status = False
                return self.response_status
            except requests.exceptions.InvalidURL as exception:
                self.logger.error(str(exception), self.host)        
                # Change connection status to False:
                self.response_status = False
                return self.response_status
            except requests.exceptions.ConnectionError as exception:
                self.logger.error(str(exception), self.host)        
                # Change connection status to False:
                self.response_status = False
                return self.response_status
            except Exception as exception:
                self.logger.error(str(exception), self.host)        
                # Change connection status to False:
                self.response_status = False
                return self.response_status
            else:
                # Finish clock count & method execution time:
                finish_time = time.perf_counter()
                self.execution_time = round(finish_time - start_time, 5)
                # Check response status:
                if response.status_code < 200: # All response from 0 to 199.
                    self.logger.warning(
                        f'HTTP(S) request sent to "{request_url}" URL, receives '\
                        'an informative HTTP(S) response. The response code is: '\
                        f'{response.status_code}.', self.host,
                        execution_time=self.execution_time)
                    # Change response code:
                    self.response_code = response.status_code
                    # Change connection status to True:
                    self.response_status = True
                elif response.status_code < 300: # All response from 200 to 299.
                    self.logger.info(
                        f'HTTP(S) request sent to "{request_url}" URL, receives '\
                        'a successful HTTP(S) response. The response code is: '\
                        f'{response.status_code}.', self.host,
                        execution_time=self.execution_time)
                    # Change response code:
                    self.response_code = response.status_code
                    # Change connection status to True:
                    self.response_status = True
                elif response.status_code < 400: # All response from 300 to 399.
                    self.logger.warning(
                        f'HTTP(S) request sent to "{request_url}" URL, return '\
                        'error response. The response code is: '\
                        f'{response.status_code}.', self.host,
                        execution_time=self.execution_time)
                    # Change response code:
                    self.response_code = response.status_code
                    # Change connection status to False:
                    self.response_status = False
                elif response.status_code < 500: # All response from 400 to 499.
                    self.logger.error(
                        f'HTTP(S) request sent to "{request_url}" URL, return '\
                        'error response. The response code is: '\
                        f'{response.status_code}.', self.host,
                        execution_time=self.execution_time)
                    # Change response code:
                    self.response_code = response.status_code
                    # Change connection status to False:
                    self.response_status = False
                elif response.status_code < 600: # All response from 500 to 599.
                    self.logger.error(
                        f'HTTP(S) request sent to "{request_url}" URL, return '\
                        'error response. The response code is: '\
                        f'{response.status_code}.', self.host,
                        execution_time=self.execution_time)
                    # Change response code:
                    self.response_code = response.status_code
                    # Change connection status to False:
                    self.response_status = False
                
                # Convert response to python dictionary:
                response_text = response.text
                if self.response_status and response_text:
                    try: # Try to convert JSON response to python dictionary:
                        self.converted_response = json.loads(response_text)
                        self.json_response_status = True
                    except:
                        self.converted_response = False
                        self.json_response_status = False
                        try: # Try to convert XML response to python dictionary:
                            self.converted_response = xmltodict.parse(response_text)
                            self.xml_response_status = True
                        except:
                            self.xml_response_status = False
                    if self.xml_response_status is False and self.json_response_status is False:
                        # Log when python dictionary convert process fail:
                        self.logger.warning(
                            'Python JSON/XML -> dictionary convert process fail, '\
                            f'in relation to "{request_url}" URL request.',
                            self.host)
                    # Return response:
                    return self.converted_response
                else:
                    self.logger.debug(
                        f'HTTP(S) response received for "{request_url}" URL '\
                        'request was empty', self.host)
                    return ''
        else: # If connection is not active, inform that the command cannot be sent:
            self.logger.error(f'Command/s could not be executed because SSH '\
                f'connection with {request_url} URL, is not active.',
                self.host)
