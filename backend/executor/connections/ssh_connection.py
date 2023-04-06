# Python - library import:
import time

# Python - regex import:
import re

# Paramiko - exceptions import:
from paramiko import ssh_exception

# Netmiko - exceptions import:
from netmiko.exceptions import AuthenticationException
from netmiko.exceptions import NetMikoTimeoutException

# Netmiko - connection import:
from netmiko.ssh_autodetect import SSHDetect
from netmiko import ConnectHandler

# AutoCli2 - Settings import:
from management.settings import collect_global_settings

# AutoCli2 - Logger import:
from notification.logger import Logger

# AutoCli2 - other model import:
from inventory.models.platform import Platform
from inventory.models.host import Host


# HTTP connection class:
class Connection:

    def __init__(self,
        host: Host,
        task_id: str = None) -> None:
        """
        Xxx.

        Class attributes:
        -----------------
        host: Host object
            Xxx.
        task_id: str
            Celery task ID.

        Methods:
        --------
        xxx: 
            Xxx
        """
        
        # Verify if the host variable is a valid host object:
        if not isinstance(host, Host):
            raise TypeError('The provided host must be instance of Host class.')
        # Verify if the task ID variable is a valid string:
        if not isinstance(task_id, str):
            raise TypeError('The provided task ID must be string.')
    
        # Logger class initiation:
        self.logger = Logger('SSH connection', task_id)

        # Collect data from host object:
        self.__host = host
        self.hostname = host.hostname
        self.ssh_port = host.ssh_port
        self.platform_name = host.platform.name
        self.host_repr = f'{host.name}:{host.hostname}'

        # Collect data from host platform object:
        self.ssh_invalid_responses = host.platform.ssh_invalid_responses
        self.ssh_platform_type = host.platform.ssh_platform_type

        # Platform type support declaration:
        if self.platform_name == 'Unsupported':
            self.is_platform_type_supported = False
        else:
            self.is_platform_type_supported = True

        # Platform type support declaration:
        if self.platform_name == 'Discover':
            self.is_platform_type_discover = False
        else:
            self.is_platform_type_discover = True

        # Collect data from host credentials object:
        self.username = host.credential.username
        self.password = host.credential.password

        # Collect data from host platform object:
        self.ssh_invalid_responses = host.platform.ssh_invalid_responses

        # Connection status declaration:
        self.connection_status = False
        self.connection = False

        # Response declaration:
        self.converted_response = None
        self.raw_response = None

        # Response status declaration:
        self.converted_response_status = False
        self.raw_response_status = False

        # Connection status declaration:
        self.raw_data_status = False
        self.processed_data_status = False
        self.raw_data = None
        self.processed_data = None

        # Timeout declaration:
        self.connection_timeout = collect_global_settings('ssh_timeout')
        self.repeat_connection = collect_global_settings('ssh_repeat')

        # Connection timer declaration:
        self.connection_timer = None

        # Execution timer declaration:
        self.execution_time = None

    @property
    def host(self):
        return self.__host

    def __repr__(self) -> str:
        """
        Connection class representation.
        """
        return f'<Class SSH connection ({self.hostname}:{self.ssh_port})>'

    def __enter__(self) -> 'Connection':
        """
        Use Connection class with python 'with' command:
        'with Connection(host) as con:
            output = con.send_enable('show version')'
        
        Return:
        --------
        Connection class object.
        """
        
        try: # Try to start SSH connection:
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

        # End SSH connection:
        self.end_connection()

    def start_connection(self) -> 'Connection':
        """
        Start a new SSH connection.

        Return:
        --------
        Connection class object.
        """

        # Check connection status:
        if self.connection_status:
            # Return Connection class object:
            return self
        else: # Check whether the hots needs to detect platform type:
            if self.is_platform_type_discover:
                # Connect to host:
                self._ssh_connect()
            else: # If host platform type must be detect:
                self.logger.debug(f'Host {self.host_repr} platform '\
                    'type must be discovered.', self.host)
                # Update platform type based on information
                # collected via SSH protocol:
                platform_type = self.update_platform_type()
                # Connect to host, if platform type was collected:
                if platform_type:
                    self._ssh_connect()
            # Start connection timer if connection is successfully established:
            if self.connection_status:
                # Start connection timer:
                self._start_connection_timer()
                # Return Connection class object:
                return self
            else: # Return False if the connection is not established:
                return False
    
    def end_connection(self) -> None:
        """ 
        End current SSH connection.
        """

        # Check connection status:
        if self.connection_status:
            try: # Try to close SSH connection:
                self.connection.disconnect()
            except: # Log that connection is already ended:
                self.logger.warning(f'Connection with host {self.host_repr} '\
                    'is already ended.', self.host)
            else: # Log close of SSH connection:
                self.logger.info(f'SSH session with host {self.host_repr} '\
                    'ended.', self.host)
            finally:
                # Change connection status:
                self.connection_status = False
                # Erase connection:
                self.connection = False
                # End connection timer:
                self._end_connection_timer()

    def test_connection(self) -> bool:
        """
        Open test SSH connection.
        """

        # Start a new SSH connection:
        Connection_status = self._ssh_connect()
        # Return connection status:
        return Connection_status

    def update_platform_type(self) -> bool:
        """
        Obtain network platform type using SSH protocol.
        Update Host platform field based on collected data.
        
        Return:
        --------
        Boolean value: True if platform type was collected
        or False if platform type was not collected.
        """

        # Log start of platform type discovery process:
        self.logger.debug(f'Started acquiring information about the type '\
            f'of platform for host: {self.host_repr}.', self.host)
        # Connect to host to check platform type, using SSH protocol:
        discovered_platform_type = self._ssh_connect(autodetect=True)
        # Check response of autodiscover process:
        if discovered_platform_type:
            # Convert collected platform type name:
            discovered_platform_type = str(discovered_platform_type).strip()
            # Collect platform type object/s:
            platform_type_objects = Platform.objects.filter(
                ssh_platform_type=discovered_platform_type,
                is_ssh_supported=True)
            # Check if object/s were found:
            if platform_type_objects.exists():
                # Collect first matching platform:
                platform_type_object = platform_type_objects[0] # ???
                # Change platform support status to True:
                self.is_platform_type_supported = True
                # Log successful platform type collection:
                self.logger.info('Host platform type has been discoverd. '\
                    f'Host: {self.host_repr} is running on '\
                    f'{platform_type_object.name} software.',
                    self.host)
            else:
                # Log unsupported platform type:
                self.logger.warning(f'Platform type {discovered_platform_type} '\
                    f'of host: {self.host_repr}, is not supported.',
                    self.host)
                # Change platform support status to False:
                self.is_platform_type_supported = False
                try: # Try to collect Unsupported platform object:
                    platform_type_object = Platform.objects.get(
                        name='Unsupported')
                except: # if Unsupported platform object doesn't exist:
                    platform_type_object = Platform.objects.get(
                        name='Unsupported')
            # Update host platform:
            self.host.platform = platform_type_object
            self.host.save(update_fields=['platform'])
            # Change discover status to True:
            self.is_platform_type_discover = True
            # Update platform type:
            self.ssh_platform_type = platform_type_object.ssh_platform_type
            # Return collected platform status:
            return True
        else: # Log that platform type has not been discovered:
            self.logger.warning(f'Host: {self.host_repr} platform type, '\
                'has not been discovered.', self.host)
            # If connection attempt was unsuccessful, return False value:
            return False

    def send_enable(self, commands: list) -> dict:
        """
        Retrieves a list containing network CLI command/s,
        and sends them to a network device using SSH protocol.
        ! Usable only with enable levels commend/s.
        
        Parameters:
        -----------------
        commands: List
            Provided device object, to establish a SSH connection.

        Return:
        --------
        Dictionary containing command/s output.
        {
            'command': 'command output',
        }
        """

        # Check if provided command variable is valid list:
        if not isinstance(commands, list):
            # Raise exception:
            raise TypeError('The provided command/s variable must be a string.')

        # Check connection status:
        if self.connection_status:
            # Start clock count:
            start_time = self._start_execution_timer()
            # Declare return data dictionary:
            return_data = {}
            # Execute enabled command:
            for command in commands:
                # Save command execution output to dictionary:
                return_data[command] = self._enabled_command_execution(
                    command)
            # Finish clock count:
            execution_time = self._end_execution_timer(start_time)
            # Log time of command/s execution:
            self.logger.info(f'Execution of "{commands}" enabled command/s '\
                f'taken {execution_time} seconds.', self.host)
            # Return data:
            return return_data
        # If connection is not active,
        # inform that the command/s cannot be sent:
        else:
            self.logger.error(f'Command/s could not be executed because SSH '\
                f'connection with host {self.host_repr}, is not active.',
                self.host)

    def send_config(self, commands: list) -> dict:
        """
        Retrieves a list containing network CLI command/s,
        and sends them to a network device using SSH protocol.
        ! Usable only with configuration terminal levels commends.
        
        Parameters:
        -----------------
        commands: List
            Provided device object, to establish a SSH connection.

        Return:
        --------
        String containing command/s output.
        """

        # Check if provided command variable is valid list:
        if not isinstance(commands, list):
            # Raise exception:
            raise TypeError('The provided command/s variable must be a string.')

        # Check connection status:
        if self.connection_status:
            # Start clock count:
            start_time = self._start_execution_timer()
            # Collect data from device:
            return_data = self._config_command_execution(commands)
            # Finish clock count & method execution time:
            execution_time = self._end_execution_timer(start_time)
            # Log time of command/s execution:
            self.logger.info(f'Execution of "{commands}" configuration '\
                f'command/s taken {execution_time} seconds.', self.host)
            # Return data:
            return return_data
        # If connection is not active,
        # inform that the command/s cannot be sent:
        else:
            self.logger.error(f'Command/s could not be executed because SSH '\
                f'connection with host {self.host_repr}, is not active.',
                self.host)

    def _enabled_command_execution(self, command: str) -> str:
        """
        SSH execution of enabled command.
        """
        
        # Check if provided command is valid:
        if isinstance(command, str):
            # Log start execution of SSH command: 
            self.logger.info(f'The process of execution a new enabled '\
                f'command "{command}" has been started on device: '\
                f'{self.host_repr}.', self.host)
            try: # Try to execute provided CLI command:
                command_response = self.connection.send_command(
                    command_string=command)
            except UnboundLocalError as exception:
                # Log information about the exception of the sent command:
                self.logger.error(f'An exception occurred during sending '\
                    f'a CLI enabled command "{command}" to the device: '\
                    f'{self.host_repr}\n{exception}', self.host)
                # Return False:
                return False
            except OSError as exception:
                # Log information about the exception of the sent command:
                self.logger.error(f'An exception occurred during sending '\
                    f'a CLI enabled command "{command}" to the device: '\
                    f'{self.host_repr}\n{exception}', self.host)
                # Return False:
                return False
            except Exception as exception:
                # Log information about the exception of the sent command:
                self.logger.error(f'An exception occurred during sending '\
                    f'a CLI enabled command "{command}" to the device: '\
                    f'{self.host_repr}\n{exception}', self.host)
                # Return False:
                return False
            else: # Log end of command execution:
                self.logger.info(f'Enabled command "{command}" has been '\
                    f'sent to {self.host_repr}.', self.host)
                # Check if command output is valid:
                is_response_valid = self._is_response_valid(command_response)
                # If command response is valid return command response:
                if is_response_valid:
                    return command_response
                else: # If command response is not valid return empty string:
                    return ''
        else: # Raise exception:
            raise TypeError('Provided command is not valid.')

    def _config_command_execution(self, commands: str) -> str:
        """
        SSH execution of configuration command/s.
        """
        
        # Log start of command execution: 
        self.logger.info(f'The process of execution a new configuration '\
            f'command "{commands}" has been started on device: '\
            f'{self.host_repr}.', self.host)
        try: # Try to execute provided CLI command:
            command_response = self.connection.send_config_set(commands)
        except UnboundLocalError as exception:
            # Log information about the exception of the sent command:
            self.logger.error(f'An exception occurred during sending '\
                f'a CLI enabled command "{commands}" to the device: '\
                f'{self.host_repr}\n{exception}', self.host)
            # Return False:
            return False
        except OSError as exception:
            # Log information about the exception of the sent command:
            self.logger.error(f'An exception occurred during sending '\
                f'a CLI enabled command "{commands}" to the device: '\
                f'{self.host_repr}\n{exception}', self.host)
            # Return False:
            return False
        except Exception as exception:
            # Log information about the exception of the sent command:
            self.logger.error(f'An exception occurred during sending '\
                f'a CLI enabled command "{commands}" to the device: '\
                f'{self.host_repr}\n{exception}', self.host)
            # Return False:
            return False
        else:
            # Log end of command execution:
            self.logger.info(f'Configuration command "{commands}" has '\
                f'been sent to {self.host_repr}.', self.host)
            # Return data:
            return command_response
    
    def _is_response_valid(self, command_response: str) -> bool:
        """
        Check if provided response is valid:
        """

        # Collect invalid responses:
        invalid_response_list = collect_global_settings('ssh_invalid_responses')
        # Check if invalid response list is valid:
        if isinstance(invalid_response_list, list):
            # iterate thru all provided expressions:
            for expression in invalid_response_list:
                try: # Try to collect expression:
                    regex_pattern = rf'{expression}'
                    re.compile(regex_pattern)
                except Exception as exception:
                    # Log compile regex exception:
                    self.logger.error(f'Expression {expression} is not '\
                        f'valid ({exception}).')
                else: # Check regex match:
                    if re.fullmatch(regex_pattern, str(command_response)):
                        return False
        # If not match fund return True response:
        return True

    def _ssh_connect(self, autodetect: bool = False) -> bool or str:
        """ 
        Connect to host using SSH protocol.
        
        Parameters:
        -----------------
        autodetect: bool
            If True will try to detect Host platform type.
        
        Return:
        --------
        If autodetect value is True will return host platform type,
        or connection status if autodetect value is False.
        """

        # Check if host platform is supported:
        if self.is_platform_type_supported or autodetect:
            # Performs a specified number of SSH connection attempts:
            for connection_attempt in range(1, self.repeat_connection + 1):
                # Sleep before second and rest of conception attempts:
                if connection_attempt > 1:
                    self._sleep()
                # Log stat of a new SSH connection attempt:
                self.logger.info(f'SSH connection to host: {self.host_repr}, '\
                    f'has been started (Attempt: {connection_attempt}/'\
                    f'{self.repeat_connection}).', self.host)
                try: # Try connect to host, using SSH protocol:
                    # Check if the platform type must be detected:
                    if autodetect:
                        # Connect to host to check platform type:
                        self.connection = SSHDetect(**{
                            'device_type': 'autodetect',
                            'host': self.hostname,
                            'port': self.ssh_port,
                            'username': self.username,
                            'password': self.password})
                    else: # Connect to device, using SSH protocol:
                        self.connection = ConnectHandler(**{
                            'device_type': self.ssh_platform_type,
                            'host': self.hostname,
                            'port': self.ssh_port,
                            'username': self.username,
                            'password': self.password})
                # Handel SSH connection exceptions:
                except AuthenticationException as exception:
                    # Log authentication exception:
                    self.logger.error(f'Exception occurred during SSH '\
                        f'connection to host: {self.host_repr} (Attempt: '\
                        f'{connection_attempt}/{self.repeat_connection}).'\
                        f'\n{exception}', self.host)
                    # Change connection status to False.
                    self.connection_status = False
                except NetMikoTimeoutException as exception:
                    # Log connection exception:
                    self.logger.error(f'Exception occurred during SSH '\
                        f'connection to host: {self.host_repr} (Attempt: '\
                        f'{connection_attempt}/{self.repeat_connection}).'\
                        f'\n{exception}', self.host)
                    # Change connection status to False.
                    self.connection_status = False
                except ssh_exception.SSHException as exception:
                    # Log connection exception:
                    self.logger.error(f'Exception occurred during SSH '\
                        f'connection to host: {self.host_repr} (Attempt: '\
                        f'{connection_attempt}/{self.repeat_connection}).'\
                        f'\n{exception}', self.host)
                    # Change connection status to False.
                    self.connection_status = False
                except Exception as exception:
                    # Log connection exception:
                    self.logger.error(f'Exception occurred during SSH '\
                        f'connection to host: {self.host_repr} (Attempt: '\
                        f'{connection_attempt}/{self.repeat_connection}).'\
                        f'\n{exception}', self.host)
                    # Change connection status to False.
                    self.connection_status = False
                else:
                    # Change connection status to True.
                    self.connection_status = True
                    # Log the start of a new connection:
                    self.logger.info(f'SSH connection to device: '\
                        f'{self.host_repr}, has been established (Attempt: '\
                        f'{connection_attempt}/{self.repeat_connection}).',
                        self.host)
                    # if autodetect is True, collect device type name:
                    if autodetect:    
                        # Collect information about device type:
                        platform_type = self.connection.autodetect()
                        # Break connection:
                        self.end_connection()
                        # Return platform type:
                        return platform_type
                    else: # Return connection status:
                        return self.connection_status
            # Return connection status:
            return self.connection_status
        else:
            self.logger.warning(f'Host {self.host_repr} platform type, '\
                'is not supported.', self.host)
            # Change connection status:
            self.connection_status = False

    def _sleep(self) -> None:
        """
        Sleep defined amount of time.
        """

        time.sleep(self.connection_timeout)

    def _start_connection_timer(self) -> None:
        """
        Start connection time counting.
        """

        # Start clock count:
        self.start_connection_time = time.perf_counter()

    def _end_connection_timer(self) -> float:
        """
        End connection time counting, and log result.

        Return:
        --------
        Method will return connection end time value.
        """

        # Check if connection timer is set up:
        if self.connection_timer:
            # Finish clock count & method execution time:
            finish_time = time.perf_counter()
            connection_timer = round(finish_time - self.start_connection_time, 5)
            # Update global connection timer:
            self.connection_timer = connection_timer
            # Log time of SSH session:
            self.logger.info(f'SSH session with host {self.host_repr} was '\
                f'active for {self.connection_timer} seconds.', self.host)
            # Reset connection timer:
            self.connection_timer = False
            # Return end connection time:
            return connection_timer
        else: # Raise error that connection timer is not set up:
            raise BrokenPipeError('The End connection timer method was '/
                'executed before the Start connection timer method or '/
                'after the connection timer value was reset.')
    
    def _start_execution_timer(self) -> float:
        """
        Start command execution time.

        Return:
        --------
        Method will return start time value.
        """

        # Start clock count:
        return time.perf_counter()

    def _end_execution_timer(self, start_time) -> float:
        """
        End command execution time counting.

        Return:
        --------
        Method will return execution end time value.
        """

        # Finish clock count & method execution time:
        finish_time = time.perf_counter()
        execution_time = round(finish_time - start_time, 5)

        # Return end execution time:
        return execution_time
