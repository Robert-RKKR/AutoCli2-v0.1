# Django import:
from django.shortcuts import render
from notification.notification import Notification
from django.contrib.sessions.backends.db import SessionStore
from inventory.models.host import Host
from management.settings import collect_global_settings
from executor.connections.http_connection import Connection
from executor.tasks.execute_executor import ExecuteExecutorTask
from connector.models.connection_template import ConnectionTemplate

# Test view:
def notifications_test(request):

    # s = SessionStore()

    # Collect data to display:
    data = {
        'page_title': 'Test RKKR - Notifications',
        'output': 'Welcome to notifications test!',
    }
    task = ExecuteExecutorTask(2)# type: ignore
    data['return_output'] = task# type: ignore

    host_one = Host.objects.get(pk=1)

    notification = Notification('Test')
    # return_output = notification.info(
    #     '1 - Welcome in AutoCli2 application')
    return_output = notification.info(
        '#################',
        host_one, 2)
    # # con = Connection(host_one)
    # # data['return_output'] = con.get('restconf/data/Cisco-IOS-XE-native:native')

    # from django.core.serializers import serialize
    # import json
    # output = serialize('json', [host_one], use_natural_foreign_keys=True, use_natural_primary_keys=True)
    # data['return_output'] = json.loads(output)[0]['fields'].keys()

    # template = ConnectionTemplate.objects.get(pk=1)
    # data['return_output'] = template.get_http_method_display()
   
    # GET method:
    return render(request, 'test.html', data)
