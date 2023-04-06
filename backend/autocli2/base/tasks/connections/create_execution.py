# AutoCli2 - base task import:
from autocli2.base.tasks.base_task import BaseTask

# AutoCli2 - executors model import:
from executor.models.execution import Execution

# AutoCli2 - constance import:
from autocli2.base.constants.execution_protocol import ExecutionProtocolChoices
from autocli2.base.constants.response_type import ResponseTypeChoices


# Test taks class:
class CreateExecutionBaseTask(BaseTask):
    """
    Xxx.
    """

    def _create_execution_object(self,
        host, template, executor, con, output):
        """
        Create execution object based on provided and collected data.
        """

        # Collect host data collection protocol:
        data_collection_protocol = host.data_collection_protocol
        # Collect host, credentials and template representations:
        representation = self._collect_execution_data(
            host, template, data_collection_protocol)
        # Collect execution data:
        execution_data = {
            'executor': executor,
            'host': host,
            'connection_template': template,
            'credential': host.credential,
            'task_id': self.task_id,
            'execution_status': con.response_status,
            'host_representation':
                representation['host_representation'],
            'connection_template_representation': 
                representation['connection_template_representation'],
            'credential_representation':
                representation['credential_representation']}
        # Collect data based on connection protocol type (HTTP/SSH)::
        if data_collection_protocol == ExecutionProtocolChoices.SSH:
            execution_data['ssh_raw_data_status'] = con.raw_data_status
            execution_data['ssh_processed_data_status'] = con.processed_data_status
            execution_data['ssh_raw_data'] = con.raw_data
            execution_data['ssh_processed_data'] = con.processed_data
        elif data_collection_protocol == ExecutionProtocolChoices.HTTP:
            execution_data['http_response_code'] = con.response_code
            execution_data['http_response'] = output
        try: # Try to create a new execution object:
            execution_object = Execution.objects.create(**execution_data)
        except:
            self.logger.error(
                'An error has occurred during the creation of a new '\
                f'execution object.')
            # Return False if object was not created:
            return False
        else:
            # Update execution status value:
            execution_object.execution_status = execution_object.is_response_valid()
            execution_object.save(update_fields=['execution_status'])
            # Return created execution object:
            return execution_object
    
    def _collect_execution_data(self,
        host, template, data_collection_protocol) -> dict:
        """
        Collect objects representations.
        """

        # Collect host credential representation:
        if host.credential:
            credential_representation = host.credential.name
        else:
            credential_representation = None
        # Collect template representation:
        if data_collection_protocol == ExecutionProtocolChoices.SSH:
            connection_template_representation = f'{template.name}: '\
                f'{template.ssh_command}'
        elif data_collection_protocol == ExecutionProtocolChoices.HTTP:
            connection_template_representation = f'{template.name}: '\
                f'{template.http_url}'
        else:
            connection_template_representation = None
        # Collect host representation:
        host_representation = f'{host.name}: {host.hostname}'
        # Return representations:
        return {
            'credential_representation': credential_representation,
            'connection_template_representation': connection_template_representation,
            'host_representation': host_representation}
