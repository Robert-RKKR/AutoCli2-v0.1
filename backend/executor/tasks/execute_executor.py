# Celery - application import:
from autocli2.celery import app

# AutoCli2 - connection class import:
from executor.tasks.connections.connection import ConnectionTask

# AutoCli2 - executor import:
from executor.models.executor import Executor

# Functions:
def collect_templates_ordered_by_order(templates):
    # Use the sorted function to sort the templates:
    sorted_templates = sorted(
        templates, key=lambda template: template.order)
    # Collect the 'connection_template' objects in a list:
    connection_templates = [
        template.connection_template for template in sorted_templates]
    # Return the list as a tuple:
    return tuple(connection_templates)

@app.task(bind=True, name='execute_executor_task', base=ConnectionTask)
def execute_executor_task(self, executor_id: int):
    # Init task:
    self.init_task()
    try: # Try to collect executor:
        executor = Executor.objects.get(pk=executor_id)
    except:
        self.logger.error(
            f'Executor object with ID: {executor_id}, has not been found.')
    else: # Collect executor data:
        hosts = executor.hosts.all()
        # Collect templates:
        templates = executor.executorconnectiontemplate_set.all()
        ordered_templates = collect_templates_ordered_by_order(templates)
        # Execute template:
        return self.singlethreading_connection(
            hosts, ordered_templates, executor)
