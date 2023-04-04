# Python - library import:
import time

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
                if platform_type: # ???????????????????????????????????????????????????????????????? str like proper output?
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
            # Try to close SSH connection:
            try:
                self.connection.disconnect()
            except: # Log that connection is already ended:
                self.logger.warning('Connection is already ended.', self.host)
            else:
                # Log close of SSH connection:
                self.logger.info('SSH session ended.', self.host)
            finally:
                # End connection timer:
                self._end_connection_timer()

    def update_platform_type(self) -> str:
        """
        Obtain network platform type using SSH protocol.
        And then update Host platform field.
        
        Return:
        --------
        Collected platform type name.
        """

        # Log start of platform type discovery process:
        self.logger.debug(f'Started acquiring information about the type '\
            f'of platform for host: {self.host_repr}.', self.host)
        # Connect to host to check platform type, using SSH protocol:
        discovered_platform_type = self._ssh_connect(autodetect=True)
        # Convert collected platform type name:
        discovered_platform_type = str(discovered_platform_type).strip()
        # Check response of autodiscovery process:
        if discovered_platform_type:
            # Collect platform type object/s:
            platform_type_objects = Platform.objects.filter(
                ssh_platform_type=discovered_platform_type,
                is_ssh_supported=True)
            # Check if object/s were found:
            if platform_type_objects.exists():
                # Collect first matching platform:
                platform_type_object = platform_type_objects[0] #??????????????????????????????????
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
            # Update platfrom type:
            self.ssh_platform_type = platform_type_object.ssh_platform_type
            # Return collected platform type name:
            return discovered_platform_type
        else: # Log that platform type has not been discovered:
            self.logger.warning(f'Host: {self.host_repr} platform type, '\
                'has not been discovered.', self.host)
            # If connection attempt was unsuccessful, return False value:
            return False

    def _sleep(self) -> None:
        """
        Sleep defined amount of time.
        """

        time.sleep(self.repeat_connection_time)

    def _ssh_connect(self, autodetect: bool = False) -> str:
        """ 
        Connect to host using SSH protocol.
        
        Parameters:
        -----------------
        autodetect: bool
            If True will try to dedect Host platform type.
        
        Return:
        --------
        The type of host platform.
        """

        def log_connection_exception(connection_attempt, exception):
            # Log exception on last attempt:
            if connection_attempt == self.repeat_connection:
                # Log authentication exception:
                self.logger.error(f'Application was unable to establish SSH connection '\
                    f'to device: {self.device_name} (Last attempt). '\
                    f'Last error:\n{exception}.',
                    task_id=self.task_id,
                    object=self.device_object)
                # Change connection status to False.
                self.connection_status = False
                # Return False:
                return self.connection_status
            else: # Log authentication exception:
                self.logger.error(f'Exception occurred during SSH connection to device:'\
                    f' {self.host_repr} '\
                    f'(Attempt: {connection_attempt}).\n{exception}',
                    task_id=self.task_id,
                    object=self.device_object)
                # Change connection status to False.
                self.connection_status = False

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
                    f'{self.repeat_connection}).', self)
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
                    else:
                        # Connect to device, using SSH protocol:
                        self.connection = ConnectHandler(**{
                            'device_type': self.ssh_platform_type,
                            'host': self.hostname,
                            'port': self.ssh_port,
                            'username': self.username,
                            'password': self.password})
                # Handel SSH connection exceptions:
                except AuthenticationException as exception:
                    # Log connection exception:
                    log_connection_exception(connection_attempt, exception)
                except NetMikoTimeoutException as exception:
                    # Log connection exception:
                    log_connection_exception(connection_attempt, exception)
                except ssh_exception.SSHException as exception:
                    # Log connection exception:
                    log_connection_exception(connection_attempt, exception)
                except OSError as exception:
                    # Log connection exception:
                    log_connection_exception(connection_attempt, exception)
                except TypeError as exception:
                    # Log connection exception:
                    log_connection_exception(connection_attempt, exception)
                except ValueError as exception:
                    # Log connection exception:
                    log_connection_exception(connection_attempt, exception)
                else:
                    # Change connection status to True.
                    self.connection_status = True
                    # Log the start of a new connection:
                    self.logger.info(f'SSH connection to device: {self.host_repr}, '\
                        f'has been established (Attempt: {connection_attempt}/'\
                        f'{self.repeat_connection}).', self)
                    # if autodetect is True, collect device type name:
                    if autodetect:    
                        # Collect information about device type:
                        platform_type = self.connection.autodetect()
                        self.connection_status = False
                        self.connection = False
                        return platform_type
                    else: # Return connection:
                        return self.connection_status
            # Return connection status:
            return self.connection_status
        else:
            self.logger.warning(f'Host: {self.host_repr} platform type, '\
                'is not supported.', self)
            # Change connection status:
            self.connection_status = False
