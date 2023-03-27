# Django import:
import json
from django.shortcuts import render
from notification.notification import Notification
from django.contrib.sessions.backends.db import SessionStore
from inventory.models.host import Host
from management.settings import collect_global_settings
from executor.connections.http_connection import Connection
from executor.tasks.execute_executor import execute_executor_task
from connector.models.connection_template import ConnectionTemplate
from inventory.models.credentials import Credential
from inventory.models.platform import Platform
from autocli2.base.constants.execution_type import HttpExecutionTypeChoices

from celery import current_app
from autocli2.celery import app
from django.urls import reverse


# Notification:
notification = Notification('Test')

# Test view:
def notifications_test(request):

    
    return_output = notification.info(
        '#################')

    # s = SessionStore()

    # Collect data to display:
    data = {
        'page_title': 'Test RKKR - Notifications',
        'output': 'Welcome to notifications test!',
    }

    method = 1
    method = HttpExecutionTypeChoices.value_from_int(method)
    data['return_output'] = method

    # credential = Credential.objects.get(pk=1)
    # platform = Platform.objects.get(pk=1)
    # print('=====> ', platform.__class__)

    # host = Host.objects.create(
    #     name='Root test eeeee',
    #     hostname='4.4.4.4e5',
    #     credential=credential,
    #     platform=platform,
    #     is_root=False
    # )
    
    # task = execute_executor_task.delay(1)
    # task = execute_executor_task(1)
    # credential = reverse('api-inventory:credential-list')
    

    # host_one = Host.objects.get(pk=1)

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
