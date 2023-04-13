# Celery - application import:
from autocli2.celery import app

# AutoCli2 - connection class import:
from executor.tasks.class_tasks.collect_host_data import CollectHostData

@app.task(bind=True, name='collect_host_data', base=CollectHostData)
def collect_host_data(self, executor_id):
    # Init task:
    self.init_task()
