# Django import:
import json
from django.shortcuts import render
from notification.notification import Notification
from executor.tasks.execute_executor import execute_executor_task


# Notification:
notification = Notification('Test')

# Test view:
def notifications_test(request):

    
    return_output = notification.info(
        '------------ New Test ------------')

    # s = SessionStore()

    # Collect data to display:
    data = {
        'page_title': 'Test RKKR - Notifications',
        'output': 'Welcome to notifications test!',
    }

    task = execute_executor_task.delay(1)
    # task = execute_executor_task(1)
    data['return_output'] = task
   
    # GET method:
    return render(request, 'test.html', data)
