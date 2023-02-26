# Python Import:
import requests
import xmltodict
import json
import time

# Logger import:
from notification.logger import Logger

# Application Import:
from inventory.models.host import Host


# HTTP connection class:
class Connection:
    
    # Logger class initiation:
    logger = Logger('HTTP/S connection')

    def __init__(self, host: Host, headers: dict = None) -> None:
        """
        The HTTP/S connection class uses requests library,
        to connect with Https server for API connections.

        Class attributes:
        -----------------
        Host: Host object
            Xxx.
        heder: dictionary
            Xxx.

        Methods:
        --------
        get: (url, connectionType='GET', payload=None)
            Xxx
        """

        # Verify if the host variable is a valid host object:
        if not isinstance(host, Host):
            raise TypeError('The provided host must be instance of Host class.')
        # Verify if the headers variable is a valid sting:
        if not isinstance(headers, dict):
            raise TypeError('The provided headers variable must be dictionary.')

        # Collect data from host object:
        self.__host = host
        self.hostname = host.hostname
        self.http_port = host.http_port
        self.certificate = host.certificate_check

        # Collect data from host credentials object:
        self.token = host.credential.token
        self.username = host.credential.username
        self.password = host.credential.password

        # Headers declaration:
        self.headers = headers

        # Connection status:
        self.converted_response = None
        self.connection_status = None
        self.xml_status = None
        self.json_status = None

        # Execution timer:
        self.execution_time = None

    @property
    def host(self):
        return self.__host
    
    def __repr__(self):
        """
        Connection class representation is IP address /
        hostname of HTTP/S server.
        """
        return self.hostname

    def get(self, url: str, params: list[str] = None):
        """
        Connection class representation is IP address /
        hostname of HTTP/S server.

        Parameters:
        -----------------
        url: string
            Xxx.
        params: list of strings
            Xxx.
        """

        return self._connection_center('GET', url, params)

    def _connection_center(self, request_method, url, params, body=None):
        """ Xxx. """

        # Verify if the host url is a valid host object:
        if not isinstance(url, str):
            raise TypeError('The provided url variable must be string.')
        # Verify if the params variable is a valid sting:
        if not isinstance(params, list):
            raise TypeError('The provided params variable must be list of strings.')

        request_url = f'https://{self.hostname}:{self.http_port}/{url}'

        return self._connection(request_method, request_url, body)

    def _connection(self, request_method, request_url, body):
        """ Xxx. """

        # Log the beginning of a new connection to the HTTP/S server:
        Connection.logger.info('Starting a new HTTP/S connection.', self.host)
        # Start clock count:
        start_time = time.perf_counter()
        # Create session:
        session = requests.Session()
        # Connect to the network device with password and username or by using token:
        if self.token:
            request = requests.Request(
                request_method,
                request_url,
                headers=self.headers,
                data=body,
            )
        else:
            request = requests.Request(
                request_method,
                request_url,
                headers=self.headers,
                auth=(self.username, self.password),
                data=body,
            )
        # Confect session with request data:
        prepare_request = session.prepare_request(request)
        try: # Try to establish a connection to a network device:
            response = session.send(
                prepare_request,
                verify=self.certificate,)
        except requests.exceptions.SSLError as error:
            Connection.logger.error(str(error), self.host)
            # Change connection status to False:
            self.status = False
            return self.status
        except requests.exceptions.Timeout as error:
            Connection.logger.error(str(error), self.host) 
            # Change connection status to False:
            self.status = False
            return self.status
        except requests.exceptions.InvalidURL as error:
            Connection.logger.error(str(error), self.host)        
            # Change connection status to False:
            self.status = False
            return self.status
        except requests.exceptions.ConnectionError as error:
            Connection.logger.error(str(error), self.host)        
            # Change connection status to False:
            self.status = False
            return self.status
        else:
            # Finish clock count & method execution time:
            finish_time = time.perf_counter()
            self.execution_time = round(finish_time - start_time, 5)
            # Check response status:
            if response.status_code < 200: # All response from 0 to 199.
                Connection.logger.warning(
                    f'Connection to {self.hostname}, '\
                        'was a informational HTTPS request. '\
                        f'HTTP/S code {response.status_code}', self.host,
                        execution_time=self.execution_time)
                # Change connection status to True:
                self.status = True
            elif response.status_code < 300: # All response from 200 to 299.
                Connection.logger.info(
                    f'Connection to {self.hostname}, '\
                        'was a success HTTPS request. '\
                        f'HTTP/S code {response.status_code}', self.host,
                        execution_time=self.execution_time)
                # Change connection status to True:
                self.status = True
            elif response.status_code < 400: # All response from 300 to 399.
                Connection.logger.warning(
                    f'Connection to {self.hostname}, '\
                        'returned redirection HTTPS error. '\
                        f'HTTP/S code {response.status_code}', self.host,
                        execution_time=self.execution_time)
                # Change connection status to False:
                self.status = False
            elif response.status_code < 500: # All response from 400 to 499.
                Connection.logger.error(
                    f'Connection to {self.hostname}, '\
                        'returned client HTTPS error. '\
                        f'HTTP/S code {response.status_code}', self.host,
                        execution_time=self.execution_time)
                # Change connection status to False:
                self.status = False
            elif response.status_code < 600: # All response from 500 to 599.
                Connection.logger.error(
                    f'Connection to {self.hostname}, '\
                        'returned server HTTPS error. '\
                        f'HTTP/S code {response.status_code}', self.host,
                        execution_time=self.execution_time)
                # Change connection status to False:
                self.status = False
            
            # Convert response to python dictionary:
            response_text = response.text
            if self.status and response_text:
                try: # Try to convert JSON response to python dictionary:
                    self.converted_response = json.loads(response_text)
                    self.json_status = True
                except:
                    self.converted_response = False
                    self.json_status = False
                    try: # Try to convert XML response to python dictionary:
                        self.converted_response = xmltodict.parse(response_text)
                        self.xml_status = True
                    except:
                        self.xml_status = False
                if self.xml_status is False and self.json_status is False:
                    # Log when python dictionary convert process fail:
                    Connection.logger.warning(
                        'Python JSON/XML -> dictionary convert process fail.',
                        self.host)
                # Return response:
                return self.converted_response
            else:
                Connection.logger.debug(
                        'HTTP/S response was empty', self.host)
                return False
