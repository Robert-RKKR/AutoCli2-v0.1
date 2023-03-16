# Celery - application import:
from celery.result import AsyncResult

# Celery - application import:
from autocli2.celery import app

# AutoCli2 - base view set import:
from autocli2.base.api.base_viewset import BaseRetrieveViewSet


# Task views classes:
class TaskStatusView(BaseRetrieveViewSet):
    
    def collect_data(self, task_id):
        """
        Return detail of tasks currently executed by workers.
        """

        # Collect information about celery task:
        task_result = AsyncResult(task_id)
        result = {
            'task_id': task_id,
            'task_status': task_result.status,
            'task_result': task_result.result}
        # Return collected data:
        return result
    

class TaskStatusViewTest(BaseRetrieveViewSet):
    
    def collect_data(self, task_id):
        """
        Return detail of tasks currently executed by workers.
        """
        
        try: # Try to collect Celery related data:
            celery_data = app.control.inspect().query_task(task_id)
        except: # Return false if the process has failed:
            celery_data = False
        finally:
            return celery_data
