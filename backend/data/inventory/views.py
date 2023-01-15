# Django import:
from django.shortcuts import render
from message.notification.notification import Notification

# Test view:
def test(request):

    # Collect data to display:
    data = {
        'page_title': 'Test RKKR',
        'output': 'Welcome!',
    }

    notification = Notification('AutoCli 2')
    notification.send(
        'Welcome in AutoCli 2 page.'
    )
    
    # GET method:
    return render(request, 'test.html', data)