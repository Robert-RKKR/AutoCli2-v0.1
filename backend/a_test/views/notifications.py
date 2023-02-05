# Django import:
from django.shortcuts import render
from messenger.notification import Notification

# Test view:
def notifications_test(request):

    # Collect data to display:
    data = {
        'page_title': 'Test RKKR - Notifications',
        'output': 'Welcome to notifications test!',
    }

    notification = Notification('Test')
    return_output = notification.notification(
        'Welcome in AutoCli 2 page.'
    )
    return_output = notification.logger('Hello RKKR', task_id='dkjd3u83ywhu3hf83')
    data['return_output'] = return_output
    
    # GET method:
    return render(request, 'test.html', data)
