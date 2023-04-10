# Django import:
import json
from django.shortcuts import render
from notification.notification import Notification
from inventory.models.host import Host
from executor.connections.ssh_connection import Connection
from autocli2.base.constants.task import TaskChoices
from executor.tasks.execute_task import execute_task

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
    
    output = execute_task(5)
    
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
