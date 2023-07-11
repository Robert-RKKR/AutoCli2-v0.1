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
        to connect with Https server for HTTP/S connections.

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
        self.credential = host.credential
        self.platform = host.platform

        # Collect data from host credentials object:
        self.token = self.credential.token
        self.username = self.credential.username
        self.password = self.credential.password

        # Collect data from host platform object:
        self.http_token_heder_key = self.platform.http_token_heder_key
        self.http_token_heder_value = self.platform.http_token_heder_value
        self.http_pagination = self.platform.http_pagination
        self.http_next_page_code_path = self.platform.http_next_page_code_path
        self.http_next_page_link_path = self.platform.http_next_page_link_path
        self.http_pagination_param_key = self.platform.http_pagination_param_key
        self.http_data_path = self.platform.http_data_path
        self.http_default_header = self.platform.http_default_header
        self.http_default_params = self.platform.http_default_params

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
            results = con.get('/HTTP/S/v2/hosts')'
        
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
        # Log message:
        self.logger.debug('A new HTTP/S connection has been established, '\
            'the test request will be sent, to test connection', self.host,
            execution_time=self.execution_time)
        # Execute test connection:
        if self.test_connection():
            self.logger.debug('A test connection has been successfully made.',
                self.host, execution_time=self.execution_time)
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
        response = self._base_connection('GET', request_url, None, True, True)
        # If connection return status code from 1 to 299 return True:
        if self.response_status:
            return True
        else: # If not return False:
            return False
    
    def connection(self,
            method: str,
            url: str,
            parameters: dict = None,
            body = None,
            pagination: bool = True):
        """
        Universal method that require the HTTP(S) method to be
        executed (GET, POST ...).

        Parameters:
        -----------------
        method: string
            HTTP connection method (GET, POST, DELETE ...).
        url: string
            URL string that will be used when requesting the HTTP/S.
        parameters: dictionary
            Dictionary containing additional parameters, formatted as specified:
            {'Key': 'Value', ...}
        body: string (json, xml) / dictionary / list
            HTTP/S request body.
        pagination: bool
            If True response will be collected from all pages.
        """

        # Check if provided HTTP method is valid:
        if method in HttpExecutionTypeChoices:
            # Collect method:
            method = HttpExecutionTypeChoices.value_from_int(method)
            # Execute HTTP(S) request:
            return self._connection(method, url, parameters, body, pagination)
        else:
            raise NotImplementedError(
                f'Provided HTTP(S) method "{method}", is not supported')

    def get(self,
            url: str,
            parameters: dict = None,
            pagination: bool = True):
        """
        GET request method for HTTP(S) connection.

        Parameters:
        -----------------
        url: string
            URL string that will be used when requesting the HTTP/S.
        parameters: dictionary
            Dictionary containing additional parameters, formatted as specified:
            {'Key': 'Value', ...}
        pagination: bool
            If True response will be collected from all pages.
        """

        # Execute HTTP(S) request:
        return self._connection('GET', url, parameters, pagination=pagination)
    
    def post(self,
            url: str,
            parameters: dict = None,
            body: dict = None):
        """
        POST request method for HTTP(S) connection.

        Parameters:
        -----------------
        url: string
            URL string that will be used when requesting the HTTP/S.
        parameters: dictionary
            Dictionary containing additional parameters, formatted as specified:
            {'Key': 'Value', ...}
        body: string (json, xml) / dictionary / list
            HTTP/S request body.
        """

        # Execute HTTP(S) request:
        return self._connection('POST', url, parameters, body)
    
    def put(self,
            url: str,
            parameters: dict = None,
            body: dict = None):
        """
        PUT request method for HTTP(S) connection.

        Parameters:
        -----------------
        url: string
            URL string that will be used when requesting the HTTP/S.
        parameters: dictionary
            Dictionary containing additional parameters, formatted as specified:
            {'Key': 'Value', ...}
        body: string (json, xml) / dictionary / list
            HTTP/S request body.
        """

        # Execute HTTP(S) request:
        return self._connection('PUT', url, parameters, body)
    
    def delete(self,
            url: str,
            parameters: dict = None,
            body: dict = None):
        """
        DELETE request method for HTTP(S) connection.

        Parameters:
        -----------------
        url: string
            URL string that will be used when requesting the HTTP/S.
        parameters: dictionary
            Dictionary containing additional parameters, formatted as specified:
            {'Key': 'Value', ...}
        body: string (json, xml) / dictionary / list
            HTTP/S request body.
        """

        # Execute HTTP(S) request:
        return self._connection('DELETE', url, parameters, body)

    def _connection(self,
            request_method: str,
            request_url: str,
            request_parameters: dict = None,
            body = None,
            pagination: bool = True):
        """
        Main connection hub responsible for collecting parameters and pagination
        data to generate URL.
        """

        # Check connection status:
        if self.connection_status:
            if body:
                # Covert body dict and list to json format:
                if isinstance(body, dict) or isinstance(body, list):
                    body = json.dumps(body)
                # Start standard HTTP/S connection:
                response = self._base_connection(request_method, request_url, body)
            else:
                # Verify if the host url is a valid host object:
                if not isinstance(request_url, str):
                    raise TypeError('The provided url variable must be string.')
                # Verify if the parameters variable is a dictionary:
                if not isinstance(request_parameters, dict):
                    if request_parameters:
                        raise TypeError('The provided parameters variable '\
                            'must be a dictionary.')
                else: # Verify parameters dictionary variable:
                    for key in request_parameters:
                        if not isinstance(key, str):
                            raise TypeError('The provided key variable must be '\
                                f'list of dictionary. Received {key}')
                        if not isinstance(request_parameters[key], str):
                            raise TypeError('The provided key value variable '\
                                f'must be list of dictionary. '\
                                f'Received {request_parameters[key]}')
                # Check if connection request contains parameters:
                if request_parameters:
                    # Create URL based of all provided request parameters:
                    request_url = self._add_parameters_to_request_url(
                        request_parameters, request_url)
                # Check if pagination is enabled:
                if pagination:
                    # Collect all response pages:
                    response = self._pagination_connection(
                        request_parameters, request_method, request_url)
                else: # Start standard HTTP/S connection:
                    response = self._base_connection(request_method, request_url)
            # Return response:
            return response

    def _add_parameters_to_request_url(self,
            request_parameters: dict,
            request_url: str) -> str:
        """
        Returns URL string containing all provided request parameters.
        """

        # Mark first parameter:
        first_parameter = True
        # Convert default parameters to url:
        if self.http_default_params:
            # Iterate thru all default parameters:
            for request_parameter in self.http_default_params:
                # Create string parameter:
                parameter = f'{request_parameter}='\
                    f'{self.http_default_params[request_parameter]}'
                if first_parameter:
                    # Create a new URL with first parameter:
                    url = f'{request_url}?{parameter}'
                    # Un mark first parameter:
                    first_parameter = False
                else:
                    # Combine current URL with nex parameter:
                    url = f'{url}&{parameter}'
        # Convert provided parameters to url:
        if request_parameters:
            # Iterate thru all provided request parameters:
            for request_parameter in request_parameters:
                # Create string parameter:
                parameter = f'{request_parameter}='\
                    f'{request_parameters[request_parameter]}'
                if first_parameter:
                    # Create a new URL with first parameter:
                    url = f'{request_url}?{parameter}'
                    # Un mark first parameter:
                    first_parameter = False
                else:
                    # Combine current URL with nex parameter:
                    url = f'{url}&{parameter}'
        # Send debug message:
        self.logger.debug(f'A new URL has been created ({url}), based on the '\
            f'provided parameters ({request_parameters}).', self.host,
            execution_time=self.execution_time)
        # Return URL:
        return url
    
    def _get_cursor(self, response):
        """
        Collect information about next page or next cursor.
        """

        if isinstance(response, dict):
            # Use next page pagination method:
            if self.http_next_page_link_path:
                # Collect next page from request:
                for path_step in self.http_next_page_link_path:
                    response = response.get(path_step, False)
                # Change pagination cursor value:
                self.pagination_cursor = True
            else: # use next cursor pagination method:
                # Collect next page from request:
                for path_step in self.http_next_page_code_path:
                    response = response.get(path_step, False)
                # Change pagination cursor value:
                self.pagination_cursor = False
            # Send debug message:
            self.logger.debug(f'A new cursor / next page URL has been collected '\
                f'({response}).', self.host, execution_time=self.execution_time)
            # Return next cursor or False response:
            return response
        else:
            return False
    
    def _get_data(self, response: dict, collected_responses: dict):
        """
        Collect data from received HTTP/S response.
        """

        # Check if data path has been provided:
        if self.http_data_path:
            # Check response data type:
            if isinstance(response, dict):
                for path in self.http_data_path:
                    response = response.get(path, False)
            # Combine collected data:
            if isinstance(response, dict):
                if collected_responses:
                    collected_responses.update(response)
                else:
                    collected_responses = response
            elif isinstance(response, list):
                if collected_responses:
                    collected_responses = collected_responses + response
                else:
                    collected_responses = response
            # Send debug message:
            res = str(response)[:200]
            self.logger.debug(f'Data has been collected ({res} ...)'\
                f', based on provided data path ({self.http_data_path}).',
                self.host, execution_time=self.execution_time)
            # Return collected data:
            return collected_responses
    
    def _pagination_connection(self,
            request_parameters: dict,
            request_method: str,
            request_url: str) -> dict:
        """
        Collect all response pages based on received next pages or cursors.
        """
        
        # Collected responses declaration:
        collected_responses = None
        # First HTTP/S connection:
        response = self._base_connection(request_method, request_url)
        # Collect data from HTTP/S response:
        collected_responses = self._get_data(response, collected_responses)
        # Collect next cursor:
        next_cursor = self._get_cursor(response)
        # Check if received response contains next cursor info:
        if next_cursor:
            # Start main loop:
            while True:
                # Check if next cursor is provided:
                if next_cursor is None:
                    # Collect next cursor:
                    next_cursor = self._get_cursor(response)
                    # If there is no next cursor, break loop:
                    if not next_cursor:
                        break
                # Check pagination methods:
                if self.http_next_page_link_path:
                    # Next HTTP/S connection:
                    response = self._base_connection(
                        request_method, next_cursor, full_url=True)
                    # Collect data from HTTP/S response:
                    collected_responses = self._get_data(
                        response, collected_responses)
                    # Clean next cursor valuable:
                    next_cursor = None
                else:
                    # Add next cursor to URL:
                    if request_parameters:
                        url = f'{request_url}&{self.http_pagination_param_key}'\
                            f'={next_cursor}'
                    else:
                        url = f'{request_url}?{self.http_pagination_param_key}'\
                            f'={next_cursor}'
                    # Next HTTP/S connection:
                    response = self._base_connection(request_method, url)
                    # Collect data from HTTP/S response:
                    collected_responses = self._get_data(
                        response, collected_responses)
                    # Clean next cursor valuable:
                    next_cursor = None
        # Return collected responses:
        return collected_responses
    
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
        self.http_default_header[self.http_token_heder_key] = token_value

    def _base_connection(self,
            request_method: str,
            request_url: str,
            body: dict = None,
            full_url: str = False,
            test = False) -> dict or list:
        """
        The main function of the connection class, responsible for
        sending the HTTP(S) request.
        """

        # Create URP if full not provided:
        if full_url is False:
            request_url = f'https://{self.hostname}:{self.http_port}/{request_url}'
        # Check connection status:
        if self.connection_status or test:
            # Log the beginning of a new connection to the HTTP(S) server:
            self.logger.info('The initiation of a new HTTP(S) '\
                f'{request_method} request to "{request_url}" '\
                'has been started.', self.host)
            # Start clock count:
            start_time = time.perf_counter()
            # Connect to the host with password and username or by using token:
            if self.token:
                # Add token to HTTP(S) heder:
                self._add_token_to_heder()
                # Send HTTP(S) HTTP/S request with heder token authorization:
                request = requests.Request(
                    request_method,
                    request_url,
                    headers=self.http_default_header,
                    data=body)
            else: # Send HTTP(S) HTTP/S request with user and password authorization:
                request = requests.Request(
                    request_method,
                    request_url,
                    headers=self.http_default_header,
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
                        f'HTTP(S) {request_method} request sent to '\
                        f'"{request_url}" URL, receives an informative HTTP(S) '\
                        f'response. The response code is: {response.status_code}.',
                        self.host, execution_time=self.execution_time)
                    # Change response code:
                    self.response_code = response.status_code
                    # Change connection status to True:
                    self.response_status = True
                elif response.status_code < 300: # All response from 200 to 299.
                    self.logger.info(
                        f'HTTP(S) {request_method} request sent to '\
                        f'"{request_url}" URL, receives an successful HTTP(S) '\
                        f'response. The response code is: {response.status_code}.',
                        self.host, execution_time=self.execution_time)
                    # Change response code:
                    self.response_code = response.status_code
                    # Change connection status to True:
                    self.response_status = True
                elif response.status_code < 400: # All response from 300 to 399.
                    self.logger.warning(
                        f'HTTP(S) {request_method} request sent to '\
                        f'"{request_url}" URL, return error response. The '\
                        f'response code is: {response.status_code}.', self.host,
                        execution_time=self.execution_time)
                    # Change response code:
                    self.response_code = response.status_code
                    # Change connection status to False:
                    self.response_status = False
                elif response.status_code < 500: # All response from 400 to 499.
                    self.logger.error(
                        f'HTTP(S) {request_method} request sent to '\
                        f'"{request_url}" URL, return error response. The '\
                        f'response code is: {response.status_code}.', self.host,
                        execution_time=self.execution_time)
                    # Change response code:
                    self.response_code = response.status_code
                    # Change connection status to False:
                    self.response_status = False
                elif response.status_code < 600: # All response from 500 to 599.
                    self.logger.error(
                        f'HTTP(S) {request_method} request sent to '\
                        f'"{request_url}" URL, return error response. The '\
                        f'response code is: {response.status_code}.', self.host,
                        execution_time=self.execution_time)
                    # Change response code:
                    self.response_code = response.status_code
                    # Change connection status to False:
                    self.response_status = False
                
                # Convert response to python dictionary:
                response_text = response.text
                if test is False:
                    if self.response_status and response_text:
                        try: # Try to convert JSON response to python dictionary:
                            self.converted_response = json.loads(response_text)
                            self.json_response_status = True
                        except:
                            self.json_response_status = False
                            try: # Try to convert XML response to python dictionary:
                                self.converted_response = xmltodict.parse(response_text)
                                self.xml_response_status = True
                            except:
                                self.xml_response_status = False
                                self.converted_response = False
                        if self.converted_response is False:
                            # Log when python dictionary convert process fail:
                            self.logger.warning(
                                'Python JSON/XML -> dictionary convert process fail, '\
                                f'in relation to "{request_url}" URL request.',
                                self.host)
                            print(f'request_url {request_url}')
                            print(f'response_text {response_text}')
                            print(f'converted_response {self.converted_response}')
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
