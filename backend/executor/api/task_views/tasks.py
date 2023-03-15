# Django - models import:
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

# Celery - application import:
from celery.result import AsyncResult

# View functions:
@csrf_exempt
def get_task_status(request, task_id):
    task_result = AsyncResult(task_id)
    result = {
        'page_results': {
            'task_id': task_id,
            'task_status': task_result.status,
            'task_result': task_result.result
        }  
    }
    return JsonResponse(result, status=200)
