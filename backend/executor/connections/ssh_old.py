# Document description:
__author__ = 'Robert Tadeusz Kucharski'
__version__ = '3.1'

# Python Import:
import textfsm
import time
import io

# Netmiko Import:
from netmiko.exceptions import AuthenticationException
from netmiko.exceptions import NetMikoTimeoutException
from netmiko.ssh_autodetect import SSHDetect
from netmiko import ConnectHandler
from paramiko import ssh_exception

# Logger import:
from messages.logger.logger import Logger

# Device model import:
from network.inventory.models.device_type_template import DeviceTypeTemplate
from network.inventory.models.device_type import DeviceType
from network.inventory.models.device import Device

# Collect settings function import:
from system.settings.settings import collect_setting

# Logger class initiation:
logger = Logger('SSH connection')

INVALID = [
    'invalid input detected',
    'cdp is not enabled',
    'incomplete command',
    'no spanning tree instance exists',
    'lldp is not enabled',
    'snmp agent not enabled'
]


# Main connection class:
class Connection:
    """
    The class uses an SSH connection to connect to the
    device and perform available operations.
    
    Methods:
    -----------------
    start_connection:
        Start SSH connection with provided device.
    end_connection:
        End current SSH connection.
    test_connection:
        Test connection to provided device.
    update_device_type:
        Update provide device type.
    send_enable:
        Send enabled command/s to provided device,
        returns cli command/s output.
    send_enabled_dict:
        Send enabled command/s to provided device,
        returns cli output and processed command/s data.
    send_config:
        Send configuration command/s to provided device.
    execute_device_type_templates:
        Run all device type template. available for provided
        device. returns cli output and processed command/s data.
    send_config_dict:
        Not implemented yet.
    """

    def __init__(self,
        device: Device,
        task_id: str = None,
        repeat_connection: int = 2,
        repeat_connection_time: int = 2,
    ) -> None:
        """
        Parameters:
        -----------------
        device: Device object
            Provided device object, to establish network connection.
        task_id: String
            Specifies the Celery task ID value, that will be added to logs messages.
        repeat_connection: Integer
            Specifies how many times the network connection will be retried.
        repeat_connection_time: Integer
            Determines how long the network connection will be attempted.
        """

        # Verify if the provided device variable is a valid Device object:
        if isinstance(device, Device):
            try:
                # Collect basic device data:
                self.device_certificate = device.certificate
                self.device_credential = device.credential
                self.device_https_port = device.https_port
                self.device_hostname = device.hostname
                self.device_ssh_port = device.ssh_port
                self.device_type = device.device_type
                self.device_token = device.token
                self.device_name = device.name
                self.device_object = device
                self.device_repr = f'{self.device_name}:{self.device_hostname}'

                # Collect user data:
                if self.device_credential is None:
                    # Use default user data:
                    self.device_username = collect_setting(
                        'default_username', default='admin')
                    self.device_password = collect_setting(
                        'default_password', default='password')
                else: # Collect username and password from credential Model:
                    self.device_username = self.device_credential.username
                    self.device_password = self.device_credential.password

                # Device supported declaration:
                if self.device_type:
                    if self.device_type.name == 'Unsupported':
                        self.supported_device = False
                    else:
                        self.supported_device = True
                else:
                    self.supported_device = None

            except:
                raise TypeError('Provided device object is not compatible '\
                    'with connection class.')

        else:
            raise TypeError('The provided device variable must be a '\
                'valid object of the Device class.')

        # Validation of the other provided data:
        self._validate_provided_data(task_id, repeat_connection, repeat_connection_time)

        # Connection declarations:
        self.connection_status = None
        self.connection = None
        # Connection timer declaration:
        self.connection_timer = None

    def __repr__(self) -> str:
        """ Connection class representation. """
        return f'<Class connection ({self.device_name}/{self.device_hostname})>'

    def __enter__(self) -> 'Connection':
        """
        Use Connection class with python with command:
        with Connection(device) as con:
            output = con.send_enable('show version')
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
        exc_traceback,
    ):

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
            
            # Check if device need autodetect device type:
            if self.supported_device is None:
                logger.info(f'Device type of the device: {self.device_repr}, must be discovered.',
                    code_id='45366876978216757567883248573975',
                    object=self.device_object)
                # Update device type based on information collected via SSH protocol:
                update_device_type = self.update_device_type()
                # Connect to network device, if device type was collected:
                if update_device_type:
                    self._ssh_connect()
            else: # Connect to network device:
                self._ssh_connect()

            # Start connection timer if connected successfully established:
            if self.connection_status:
                # Start connection timer:
                self._start_connection_timer()
                # Return Connection class object:
                return self
            else: # Return False value:
                return False
        
        else: # Log that connection is already establish:
            logger.warning(f'Connection to device: {self.device_repr} '\
                'is already established.',
                code_id='58397698345748759427958743978654',
                object=self.device_object)
            # Return Connection class object:
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
                logger.warning('Connection is already ended.',
                    code_id='35743659348567486946754794595654',
                    object=self.device_object)
            else:
                # Log close of SSH connection:
                logger.info('SSH session ended.',
                    code_id='79237587073468678967477285487494',
                    object=self.device_object)
            finally:
                # End connection timer:
                self._end_connection_timer()

    def test_connection(self) -> bool:
        """
        Open test SSH connection.
        """

        # Start a new SSH connection:
        device_type = self._ssh_connect(autodetect=True)
        # Return connection status:
        if device_type:
            return True
        else:
            return False

    def update_device_type(self) -> str:
        """
        Obtain network device type information using SSH protocol.
        And update Device type object.
        Return:
        --------
        Collected device type name.
        """

        # Log beginning of network device type checking process:
        logger.info(f'Started acquiring information about the device type '\
            f'of device: {self.device_repr}.',
            code_id='45987897427586734579937923758345',
            object=self.device_object)

        # Connect to device to check device type, using SSH protocol:
        discovered_device_type_name = self._ssh_connect(autodetect=True)

        if discovered_device_type_name:

            try: # Collecting device type object:
                discovered_device_type_name = str(discovered_device_type_name).strip()
                device_type_object = DeviceType.objects.get(netmiko_name=discovered_device_type_name) 
            except:
                # Log unsupported device type:
                logger.warning(f'Device type {discovered_device_type_name} '\
                    f'of device: {self.device_name}, is not supported.',
                    code_id='53984757569847568947569439023142',
                    object=self.device_object)
                # Change supported value to unsupported:
                self.supported_device = False
                try: # Try to collect unsupported device type:
                    device_type_object = DeviceType.objects.get(name='Unsupported')
                except:
                    logger.critical('Could not collect Unsupported device type.',
                        code_id='04930574037590847092843985739209',
                        object=self.device_object)
                # Return False:
                return False
            else:
                # Log successful device type collection:
                logger.info(f'Device: {self.device_repr} '\
                    f'is running {device_type_object.name} software.',
                    code_id='87394958738420432733295809238490',
                    object=self.device_object)
                # Change supported value to supported:
                self.supported_device = True
                # Change current device type to new one:
                self.device_object.device_type = device_type_object
                self.device_type = device_type_object

                try: # Try to update device type object:
                    self.device_object.save(update_fields=['device_type']) 
                except: # Return exception if there is a problem during
                    # the update of the device type object:
                    logger.critical(f'Exception occurs, durning device type update '\
                        f'process (device: {self.device_repr}).',
                        code_id='45778589346798743750765946045895',
                        object=self.device_object)
                else:
                    logger.info(f'Device type of device: {self.device_repr} has been updated.',
                        code_id='45827095295629370482756732094358',
                        object=self.device_object)

                # Return collected device type name:
                return discovered_device_type_name

        else:
            # Log that device type has not been discovered:
            logger.warning(f'Device type of device: '\
                f'{self.device_repr}, has not been discovered.',
                code_id='53984757569847568947569443904564',
                object=self.device_object)
            # If connection attempt was unsuccessful,
            # return False:
            return False

    def send_enable(self, commands: str or list) -> dict:
        """
        Retrieves a string or list containing network CLI command/s,
        and sends them to a network device using SSH protocol.
        ! Usable only with enable levels commend/s.
        
        Parameters:
        -----------------
        commands: String
            Provided device object, to establish a SSH connection.
        commands: List
            Provided device object, to establish a SSH connection.
        Return:
        --------
        Dictionary containing command/s output.
        """

        # Check if provided command variable is valid string or list:
        if not isinstance(commands, str) and not isinstance(commands, list):
            # Raise exception:
            raise TypeError('The provided command/s variable must be a string or list.')

        # Check connection status:
        if self.connection_status:

            # Start clock count:
            start_time = self._start_execution_timer()
            # Declare return data dictionary:
            return_data = {}

            # First option: command is string:
            if isinstance(commands, str):
                # Save command execution output to dictionary:
                return_data[commands] = self._enabled_command_execution(commands)
            elif isinstance(commands, list):
                for command in commands:
                    if isinstance(command, str):
                        # Save command execution output to dictionary:
                        return_data[command] = self._enabled_command_execution(command)
                    else: # Raise exception:
                        raise TypeError('Wrong data type.')

            # Finish clock count & method execution time:
            execution_time = self._end_execution_timer(start_time)
            # Log time of command/s execution:
            logger.info(f'Execution of "{commands}" enabled command/s '\
                f'taken {execution_time} seconds.',
                code_id='4038784967958o756763487543645645',
                execution=execution_time,
                object=self.device_object)
            # Return data:
            return return_data
        
        # If connection is not active,
        # inform that the command/s cannot be sent:
        else:
            logger.error(f'Command/s could not be executed because SSH '\
                f'connection with device: {self.device_name}:'\
                f'{self.device_hostname}, is not active.',
                code_id='85796789475925793485849346779674',
                object=self.device_object)

    def send_config(self, commands: str or list) -> dict:
        """
        Retrieves a string or list containing network CLI command/s,
        and sends them to a network device using SSH protocol.
        ! Usable only with configuration terminal levels commends.
        
        Parameters:
        -----------------
        commands: String
            Provided device object, to establish a SSH connection.
        commands: List
            Provided device object, to establish a SSH connection.
        Return:
        --------
        String containing command/s output.
        """

        # Check if provided command variable is valid string or list:
        if not isinstance(commands, str) or not isinstance(commands, list):
            # Raise exception:
            raise TypeError('The provided command/s variable must be a string or list.')

        # Check connection status:
        if self.connection_status:

            # Start clock count:
            start_time = self._start_execution_timer()

            # Collect data from device:
            return_data = self._config_command_execution(commands)

            # Finish clock count & method execution time:
            execution_time = self._end_execution_timer(start_time)
            # Log time of command/s execution:
            logger.info(f'Execution of "{commands}" configuration command/s '\
                f'taken {execution_time} seconds.',
                code_id='45837565869734945824578465374589',
                execution=execution_time,
                object=self.device_object)

            # Return data:
            return return_data

        # If connection is not active,
        # inform that the command/s cannot be sent:
        else:
            logger.error(f'Command/s could not be executed because SSH '\
                f'connection with device: {self.device_repr} is not active.',
                code_id='43565892742368562758284832947343',
                object=self.device_object)

    def send_enabled_dict(self, commands: str or list) -> dict:
        """
        Retrieves a string or list containing network CLI command/s,
        and sends them to a network device using SSH protocol.
        Collected commands are process to receive dictionary output,
        based on Device type templates.
        ! Usable only with enable levels commend/s.
        
        Parameters:
        -----------------
        commands: String
            Provided device object, to establish a SSH connection.
        commands: List
            Provided device object, to establish a SSH connection.
        Return:
        --------
        Dictionary containing command/s output and process data.
        """

        # Declare return data dictionary:
        return_data = {}
        # Collect command/s output:
        commands_output = self.send_enable(commands)
        try:
            # Iterate thu collected command/s outputs:
            for command_name in commands_output:

                # Collect command data:
                command_output = commands_output[command_name]
                # Check if command output is valid:
                if command_output:
                    # Process collected command output:
                    processed_data = self._process_command_output_to_dictionary(
                        command_name.strip(), command_output)
                    # Prepare return data:
                    data = {
                        'command_name': command_name,
                        'command_output': command_output,
                        'processed_data': processed_data['output'],
                        'processed_error': processed_data['error']}
                else:
                    # Prepare return data:
                    data = {
                        'command_name': command_name,
                        'command_output': False,
                        'processed_data': False,
                        'processed_error': 'Command output was not received.'}
                # Add collected data to return data:
                return_data[command_name] = data
        except:
            return False

        # Return collected data:
        return return_data

    def send_config_dict(self, commands: str or list, fsm_template = False) -> dict:
        """
        """

        print('Unsupported')

    def execute_device_type_templates(self) -> dict:
        """
        Collects all device type templates commands,
        and sends them to a network device using SSH protocol.
        Collected commands are process to receive dictionary output,
        based on Device type templates.
        ! Usable only with enable levels commend/s.
        """

        # Define data output:
        output_data = None
        # Define command list:
        commands = []
        # Collect all device type templates:
        all_device_type_templates = DeviceTypeTemplate.objects.filter(
            device_type=self.device_type,
            special=False,
            vrf=False)
        # Iterate thru all collected templates:
        for device_type_templates in all_device_type_templates:
            commands.append(device_type_templates.command)
        # Send all collected commands to device:
        output_data = self.send_enabled_dict(commands)
        # Return data output or False if data output list is empty:
        if output_data:
            return output_data
        else: # If data output list is empty, return False:
            return False

    def _enabled_command_execution(self, command: str) -> str:
        """
        Enabled command execution.
        """
        
        # Log start of command execution: 
        logger.info(f'The process of execution a new enabled command "{command}" has '\
            f'been started on device: {self.device_repr}.',
            code_id='48376895768937458999702748593454',
            object=self.device_object)

        try: # Try to execute provided CLI command:
            command_output = self.connection.send_command(
                command_string=command)
        
        except UnboundLocalError as error:
            # Log information about the error of the sent command:
            logger.error(f'An error occurred during sending a CLI '\
                f'enabled command "{command}" to the device: '\
                f'{self.device_repr}\n{error}',
                code_id='48376895768937458999702748573456',
                object=self.device_object)
            # Return False:
            return False
        except OSError as error:
            # Log information about the error of the sent command:
            logger.error(f'An error occurred during sending a CLI '\
                f'enabled command "{command}" to the device: '\
                f'{self.device_repr}\n{error}',
                code_id='48376895768937458999702748526427',
                object=self.device_object)
            # Return False:
            return False
        except TypeError as error:
            # Log information about the error of the sent command:
            logger.error(f'An error occurred during sending a CLI '\
                f'enabled command "{command}" to the device: '\
                f'{self.device_repr}\n{error}',
                code_id='48376895768937458999702748557246',
                object=self.device_object)
            # Return False:
            return False

        else:
            # Log end of command execution:
            logger.info(f'Enabled command "{command}" has been sent to '\
                f'{self.device_repr}.',
                code_id='45937576967845796874673497346456',
                object=self.device_object)

            # Check if command output is valid:
            for invalid in INVALID:
                # If command output contains invalid string or is None,
                # return False and send log:
                if command_output is None or invalid in command_output.lower():
                    # Log invalid command output:
                    logger.info(f'Enabled command "{command}" send to '\
                        f'{self.device_repr} '\
                        'return no data or return invalid response.',
                        code_id='34753968794278589347307485934645',
                        object=self.device_object)
                    return False
            
            # Return data:
            return command_output

    def _config_command_execution(self, command: str) -> str:
        """
        Configuration command execution.
        """
        
        # Log start of command execution: 
        logger.info(f'The process of execution a new configuration command "{command}" has '\
            f'been started on device: {self.device_repr}.',
            code_id='34567895768937458999702748593454',
            object=self.device_object)

        try: # Try to execute provided CLI command:
            command_output = self.connection.send_config_set(command)
        
        except UnboundLocalError as error:
            # Log information about the error of the sent command:
            logger.error(f'An error occurred during sending a CLI '\
                f'configuration command "{command}" to the device: '\
                f'{self.device_repr}\n{error}',
                code_id='26745895768937458999702748573456',
                object=self.device_object)
            # Return False:
            return False
        except OSError as error:
            # Log information about the error of the sent command:
            logger.error(f'An error occurred during sending a CLI '\
                f'configuration command "{command}" to the device: '\
                f'{self.device_repr}\n{error}',
                code_id='26745895768937458999702748526427',
                object=self.device_object)
            # Return False:
            return False
        except TypeError as error:
            # Log information about the error of the sent command:
            logger.error(f'An error occurred during sending a CLI '\
                f'configuration command "{command}" to the device: '\
                f'{self.device_repr}\n{error}',
                code_id='26745895768937458999702748557246',
                object=self.device_object)
            # Return False:
            return False

        else:
            # Log end of command execution:
            logger.info(f'Configuration command "{command}" has been sent to '\
                f'{self.device_repr}.',
                code_id='26745968794278589347307485934645',
                object=self.device_object)
            
            # Return data:
            return command_output

    def _validate_provided_data(self, task_id, repeat_connection, repeat_connection_time) -> None:
        """
        Validate provided data.
        """

        # Verify if the specified taks_id variable is a string:
        if task_id is None or isinstance(task_id, str):
            # Celery task ID declaration:
            self.task_id = task_id
        else:
            raise TypeError('The provided task ID variable must be a string.')

        # Verify if the specified repeat connection variable is a integer:
        if repeat_connection is None or isinstance(repeat_connection, int):
            # Celery task ID declaration:
            self.repeat_connection = repeat_connection
        else:
            raise TypeError('The provided repeat connection variable must be a integer.')

        # Verify if the specified repeat connection time variable is a integer:
        if repeat_connection_time is None or isinstance(repeat_connection_time, int):
            # Celery task ID declaration:
            self.repeat_connection_time = repeat_connection_time
        else:
            raise TypeError('The provided repeat connection variable must be a integer.')

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

    def _start_connection_timer(self) -> None:
        """
        Start connection time counting.
        """

        # Start clock count:
        self.connection_timer = time.perf_counter()

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
            connection_timer = round(finish_time - self.connection_timer, 5)
            # Update global connection timer:
            self.connection_timer = connection_timer
            # Log time of SSH session:
            logger.info(f'SSH session was active for {self.connection_timer} seconds.',
                code_id='23345367424534254360995656646765',
                task_id=self.task_id,
                execution=self.connection_timer,
                object=self.device_object)
            # Reset connection timer:
            self.connection_timer = False

            # Return end connection time:
            return connection_timer

        else: # Raise error that connection timer is not set up:
            raise BrokenPipeError('The End connection timer method was '/
                'executed before the Start connection timer method or '/
                'after the connection timer value was reset.')

    def _sleep(self) -> None:
        """
        Sleep defined amount of time.
        """

        time.sleep(self.repeat_connection_time)

    def _ssh_connect(self, autodetect: bool = False) -> str:
        """ 
        Connect to device using SSH protocol.
        Parameters:
        -----------------
        commands: bool
            Detect device type.
        Return:
        --------
        The type of network device or connection status.
        """

        def log_connection_exception(connection_attempt, error):
            # Log error on last attempt:
            if connection_attempt == self.repeat_connection:
                # Log authentication exception:
                logger.error(f'Application was unable to establish SSH connection '\
                    f'to device: {self.device_name} (Last attempt). '\
                    f'Last error:\n{error}.',
                    code_id='93428735587384593649347783782395',
                    task_id=self.task_id,
                    object=self.device_object)
                # Change connection status to False.
                self.connection_status = False
                # Return False:
                return self.connection_status
            else: # Log authentication exception:
                logger.error(f'Error occurred during SSH connection to device:'\
                    f' {self.device_repr} '\
                    f'(Attempt: {connection_attempt}).\n{error}',
                    code_id='48753984592309457596283904835934',
                    task_id=self.task_id,
                    object=self.device_object)
                # Change connection status to False.
                self.connection_status = False

        # Check if device is supported before connection attempt:
        if self.supported_device is False:

            if not autodetect:
                logger.error(f'Device: {self.device_repr}, is not supported.',
                    code_id='34893858374598734897479485769456',
                    task_id=self.task_id,
                    object=self.device_object)
            # Change connection status:
            self.connection_status = False

        elif self.supported_device or autodetect:

            # Performs a specified number of SSH connection attempts to network device.
            for connection_attempt in range(1, self.repeat_connection + 1):

                # Sleep before second and rest of conception attempts:
                if connection_attempt > 1:
                    self._sleep()

                # Log stat of a new SSH connection attempt:
                logger.info(f'SSH connection to device: {self.device_repr}, '\
                    f'has been started (Attempt: {connection_attempt}).',
                    code_id='48734859373923718475395598735746',
                    task_id=self.task_id,
                    object=self.device_object)

                try: # Try connect to device, using SSH protocol:
                    # Check if the device type must be detected automatically:
                    if autodetect:
                        # Connect to device to check device type, using SSH protocol:
                        self.connection = SSHDetect(**{
                            'device_type': 'autodetect',
                            'host': self.device_hostname,
                            'port': self.device_ssh_port,
                            'username': self.device_username,
                            'password': self.device_password})
                    else:
                        # Connect to device, using SSH protocol:
                        self.connection = ConnectHandler(**{
                            'device_type': self.device_type.netmiko_name,
                            'host': self.device_hostname,
                            'port': self.device_ssh_port,
                            'username': self.device_username,
                            'password': self.device_password})

                # Handel SSH connection exceptions:
                except AuthenticationException as error:
                    # Log connection exception:
                    log_connection_exception(connection_attempt, error)
                except NetMikoTimeoutException as error:
                    # Log connection exception:
                    log_connection_exception(connection_attempt, error)
                except ssh_exception.SSHException as error:
                    # Log connection exception:
                    log_connection_exception(connection_attempt, error)
                except OSError as error:
                    # Log connection exception:
                    log_connection_exception(connection_attempt, error)
                except TypeError as error:
                    # Log connection exception:
                    log_connection_exception(connection_attempt, error)
                except ValueError as error:
                    # Log connection exception:
                    log_connection_exception(connection_attempt, error)

                else:
                    # Change connection status to True.
                    self.connection_status = True
                    # Log the start of a new connection:
                    logger.info(f'SSH connection to device: {self.device_repr}, '\
                        f'has been established (Attempt: {connection_attempt}).',
                        code_id='48734859373923718475395598735746',
                        task_id=self.task_id,
                        object=self.device_object)
                    # if autodetect is True, collect device type name:
                    if autodetect:    
                        # Collect information about device type:
                        device_type = self.connection.autodetect()
                        self.connection_status = False
                        self.connection = False
                        return device_type
                    else: # Return connection:
                        return self.connection_status

            # Return connection status:
            return self.connection_status

    def _process_command_output_to_dictionary(self, command = str, command_output = str) -> list:
        """
        Convert commands output to dictionary based on Text FSM templates.
        """

        # Log start of the command process:
        logger.info(f'SFM process on command "{command}" collected from device: '\
            f'{self.device_repr}, has been started.',
            code_id='49537874598379083278974524899254',
            object=self.device_object)

        # FSM result list declaration:
        fsm_result = []
        # Return data declaration:
        return_data = {
            'output': None,
            'error': None,
        }
        # Try to Collect fsm template:
        try:
            fsm_template_object = DeviceTypeTemplate.objects.get(
                command=command, device_type=self.device_type)
        except:
            # Return False value:
            return_data['output'] = False
            return_data['error'] = f'Provided command "{command}" is not supported.'
            # Log unsupported command:
            logger.warning(f'Provided command "{command}" is not '\
                'supported by any SFM available template.',
                code_id='43768438673692697486247856873464',
                object=self.device_object)
        else:
            # Collect data from template object:
            fsm_template = fsm_template_object.sfm_expression
            template_as_file = io.StringIO(fsm_template)
            try: # Try to parse collected data from Text FSM:
                fsm = textfsm.TextFSM(template_as_file)
                result = fsm.ParseText(command_output)
                # Create one or many dict from Text FSM result:
                for value in result:
                    fsm_result.append(dict(zip(fsm.header, value)))
            except textfsm.TextFSMTemplateError as error:
                # Log error during Text FSM process:
                logger.error(f'Error occurred during SFM operation on device: '\
                    f'{self.device_repr}\n{error}',
                    code_id='43527880467579473896025095748654',
                    object=self.device_object)
                # Return False value:
                return_data['output'] = False
                return_data['error'] = str(error)
            except textfsm.TextFSMError as error:
                # Log error during Text FSM process:
                logger.error(f'Error occurred during SFM operation on device: '\
                    f'{self.device_repr}\n{error}',
                    code_id='54628976579063784736097753945645',
                    object=self.device_object)
                # Return False value:
                return_data['output'] = False
                return_data['error'] = str(error)
            else:
                logger.info(f'SFM process on command "{command}" collected from '\
                    f'device: {self.device_repr}, has been accomplish.',
                    code_id='54897698547687354069975809474056',
                    object=self.device_object)
                # Return FSM process output:
                return_data['output'] = fsm_result
                return_data['error'] = False
        
        # Return collected data
        return return_data