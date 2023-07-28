# Django import:
from django.shortcuts import render
from notification.logger import Logger
from notification.notification import Notification
from inventory.models.platform import Platform
from inventory.models.host import Host
from connector.models.connection_template import ConnectionTemplate
from executor.connections.http_connection import Connection
from executor.models.executor import Executor
from executor.tasks.glencore.so_network import sentinelone_network_task
from executor.tasks.execute_executor import execute_executor_task

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

    # platform = Platform.objects.get(pk=1)
    # outputs.append(platform)
    # host = Host.objects.get(pk=1)
    # outputs.append(host)
    # param = {'limit': '1000', 'sortBy': 'createdAt', 'sortOrder': 'desc'}
    # with Connection(host) as conn:
    #     responde = conn.get('web/api/v2.1/private/bulk-tasks', param)

    # data['return_output'] = sentinelone_network_task()


    host = Host.objects.get(pk=1)
    # data['return_output'] = execute_executor_task(1)

    executor = Executor.objects.get(pk=1)
    templates = executor.connection_templates.all()
    collect = []
    for template in templates:
        collect.append(template.executor_set.all())
    data['return_output'] = executor.executorconnectiontemplate_set.all()

    # GET method:
    return render(request, 'test.html', data)
