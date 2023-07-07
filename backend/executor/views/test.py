# Django import:
from django.shortcuts import render
from notification.logger import Logger
from notification.notification import Notification
from inventory.models.platform import Platform
from inventory.models.host import Host
from executor.connections.http_connection import Connection

# Notification:
notification = Notification('Test')

# Test view:
def test(request):

    # Collect data to display:
    data = {
        'page_title': 'Test RKKR - Notifications',
        'output': 'Welcome to notifications test!',
    }

    outputs = []
    logger = Logger('HTTP(S) connection')
    
    # outputs.append(notification.critical('Test info notification critical'))
    # outputs.append(notification.error('Test info notification error'))
    # outputs.append(notification.warning('Test info notification warning'))
    # outputs.append(notification.info('Test info notification info'))

    platform = Platform.objects.get(pk=1)
    outputs.append(platform)
    host = Host.objects.get(pk=1)
    outputs.append(host)

    param = {'limit': '1000', 'sortBy': 'createdAt', 'sortOrder': 'desc'}
    with Connection(host) as conn:
        responde = conn.get('web/api/v2.1/private/bulk-tasks', param)

    output = responde

    data['return_output'] = len(output)
   
    # GET method:
    return render(request, 'test.html', data)
