# Python - jinja2 and json:
from jinja2 import Template
import json

# Django - model to dict:
from django.forms.models import model_to_dict

# AutoCli2 - base task import:
from autocli2.base.tasks.base_task import BaseTask

# AutoCli2 - executors model import:
from executor.models.execution import Execution

# AutoCli2 - constance import:
from autocli2.base.constants.execution_protocol import ExecutionProtocolChoices


# Test taks class:
class ExecutionBaseTask(BaseTask):
    """
    Base execution class task.
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
                'execution object.')
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
    
    def _fill_tamplet_data(self, template_dict: dict, host):
        """ Xxx. """

        # Collect all models:
        credential = host.credential
        platform = host.platform
        site = host.site
        region = site.region
        all_models = {
            'host': host,
            'credential': credential,
            'platform': platform,
            'site': site,
            'region': region}
        # Collect all data from models:
        models_data = {}
        for model_name in all_models:
            # Collect model:
            one_model = all_models[model_name]
            if one_model:
                # Collect modeL data:
                model_data = model_to_dict(one_model)
                # Add model data to collected data:
                models_data[model_name] = model_data

        # Convert HTML/S body to JSON:
        template_json = json.dumps(template_dict)
        try: # Trt to crate a Jinja2 template object:
            template = Template(template_json)
        except Exception as error:
            # Create debug message:
            self.logger.debug(
                f'Provided HTTP/S body is not valid: {error}')
            # Return base body value:
            return template_dict
        else:
            try: # Try to render the template with the dictionary as context:
                rendered_html = template.render(
                    host=models_data.get('host', None),
                    credential=models_data.get('credential', None),
                    platform=models_data.get('platform', None),
                    site=models_data.get('site', None),
                    region=models_data.get('region', None))
            except Exception as error:
                # Create debug message:
                self.logger.debug(
                    f'Template field rendering process field: {error}')
                # Return base body value:
                return template_dict
            else:
                # Create debug message:
                self.logger.debug(
                    'Template field rendering process was '\
                    f'success: {rendered_html}')
        
        # Return all collected data:
        return rendered_html
