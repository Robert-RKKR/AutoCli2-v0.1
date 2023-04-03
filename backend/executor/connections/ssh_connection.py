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
        self.host_repr = f'{host.name}:{host.hostname}'

        # Collect data from host platform object:
        self.ssh_invalid_responses = host.platform.ssh_invalid_responses
        self.ssh_platform_type = host.platform.ssh_platform_type

        # Platform type support declaration:
        if self.ssh_platform_type == 'unsupported':
            self.is_platform_type_supported = False
        else:
            self.is_platform_type_supported = True

        # Platform type support declaration:
        if self.ssh_platform_type == 'discovery':
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
        if not self.connection_status:
            # Check whether the hots needs to autodetect the platform type:
            if self.is_platform_type_discover is False:
                self.logger.debug(f'Host {self.host_repr} platform '\
                    'type must be discovered.', self.host)
                # Update platform type based on information collected via SSH protocol:
                update_platform_type = self.update_platform_type()
                # Connect to host, if platform type was collected:
                if update_platform_type:
                    self._ssh_connect()
            else: # Connect to host:
                self._ssh_connect()
            # Start connection timer if connection is successfully established:
            if self.connection_status:
                # Start connection timer:
                self._start_connection_timer()
                # Return Connection class object:
                return self
            else: # Return False if the connection is not established:
                return False
        else: # Return Connection class object:
            return self
    
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
        Obtain network platform type information using SSH protocol.
        And update Host platform type field.
        Return:
        --------
        Collected platform type name.
        """

        # Log beginning of host platform type discovery process:
        self.logger.debug(f'Started acquiring information about the platform type '\
            f'of host: {self.host_repr}.', self.host)
        # Connect to host to check platform type, using SSH protocol:
        discovered_platform_type_name = self._ssh_connect(autodetect=True)

        if discovered_platform_type_name:
            try: # Collecting platform type object:
                discovered_platform_type_name = str(discovered_platform_type_name).strip()
                # Collect platforms that contain provided platform type:
                platform_type_object = Platform.objects.filter(
                    ssh_platform_type=discovered_platform_type_name,
                    is_ssh_supported=True) 
            except:
                # Log unsupported platform type:
                self.logger.warning(f'platform type {discovered_platform_type_name} '\
                    f'of host: {self.host_repr}, is not supported.',
                    self.host)
                # Change supported value to unsupported:
                self.supported_device = False
                try: # Try to collect unsupported platform type:
                    platform_type_object = Host.objects.get(name='Unsupported')
                except:
                    self.logger.critical('Could not collect Unsupported platform type.',
                        self.host)
                # Return False:
                return False
            else:
                # Log successful platform type collection:
                self.logger.info(f'Host: {self.host_repr} '\
                    f'is running {platform_type_object.name} software.',
                    self.host)
                # Change supported value to supported:
                self.supported_device = True
                # Change current platform type to new one:
                self.device_object.platform_type = platform_type_object
                self.platform_type = platform_type_object

                try: # Try to update platform type object:
                    self.device_object.save(update_fields=['platform_type']) 
                except: # Return exception if there is a problem during
                    # the update of the platform type object:
                    self.logger.critical(f'Exception occurs, durning platform type update '\
                        f'process (device: {self.host_repr}).',
                        self.host)
                else:
                    self.logger.info(f'platform type of host: {self.host_repr} has been updated.',
                        self.host)
                # Return collected platform type name:
                return discovered_platform_type_name
        else: # Log that platform type has not been discovered:
            self.logger.warning(f'Host: {self.host_repr} platform type, '\
                'has not been discovered.', self.host)
            # If connection attempt was unsuccessful, return False value:
            return False
