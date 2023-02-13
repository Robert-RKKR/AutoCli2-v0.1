# Django import:
from django.shortcuts import render
from notification.notification import Notification
from django.contrib.sessions.backends.db import SessionStore
from inventory.models.host import Host

# Test view:
def notifications_test(request):

    s = SessionStore()

    # Collect data to display:
    data = {
        'page_title': 'Test RKKR - Notifications',
        'output': 'Welcome to notifications test!',
    }

    host_one = Host.objects.get(pk=1)

    notification = Notification('Test')
    # return_output = notification.info(
    #     '1 - Welcome in AutoCli2 application')
    return_output = notification.info(
        '2 - Welcome in AutoCli2 application',
        host_one, 2)
    data['return_output'] = return_output
    
    # GET method:
    return render(request, 'test.html', data)
