# Celery - application import:
from autocli2.celery import app

# AutoCli2 - connection class import:
from executor.tasks.connections.connection import ConnectionTask

# AutoCli2 - executor import:
from executor.models.executor import Executor

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
        connection_templates = executor.connection_templates.all()
        # Execute template:
        return self.singlethreading_connection(
            hosts, connection_templates, executor)
