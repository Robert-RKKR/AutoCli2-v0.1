# Django import:
import json
from django.shortcuts import render
from notification.notification import Notification
from inventory.models.host import Host
from executor.connections.ssh_connection import Connection as Ssh
from executor.connections.http_connection import Connection as Http
from autocli2.base.constants.task import TaskChoices
from executor.tasks.execute_executor import execute_executor_task

# Notification:
notification = Notification('Test')

# Test view:
def notifications_test(request):

    # Collect data to display:
    data = {
        'page_title': 'Test RKKR - Notifications',
        'output': 'Welcome to notifications test!',
    }


    
    return_output = notification.info(
        '------------ New Test ------------')
    
    host = Host.objects.get_or_create(
        name='Test HTTP host London underground',
        hostname='api.tfl.gov.uk',
        data_collection_protocol=2)[0]
    con = Http(host)
    con.start_connection()
    response = con.get('BikePoint')
    output = response
    
    # connection = Connection(host, '384dg8ht858rfhu4h83r83fw')
    # connection.start_connection()
    # output = connection.send_enable([
    #     'show ip int brief',
    #     'show interfaces',
    #     'show cdp details',
    #     'show ip router'])
    # output = connection.send_enable([
    #     'show ip int brief'])
    # output = connection.send_config([
    #     'interface GigabitEthernet2',
    #     'ip address 192.168.34.1 255.255.255.0'
    # ])
    
    # task = ExecuteExecutorTask.delay(1)
    # output = ExecuteExecutorTask(1)
    data['return_output'] = output
   
    # GET method:
    return render(request, 'test.html', data)
