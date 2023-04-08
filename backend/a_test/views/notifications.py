# Django import:
import json
from django.shortcuts import render
from notification.notification import Notification
from executor.tasks.execute_executor import execute_executor_task
from inventory.models.host import Host
from executor.connections.ssh_connection import Connection
from notification.models.notification import Notification as NotificationModel


# Notification:
notification = Notification('Test')

# Test view:
def notifications_test(request):

    # Collect data to display:
    data = {
        'page_title': 'Test RKKR - Notifications',
        'output': 'Welcome to notifications test!',
    }

    host = Host.objects.get(pk=26)
    
    return_output = notification.info(
        '------------ New Test ------------', host)
    
    connection = Connection(host, '384dg8ht858rfhu4h83r83fw')
    connection.start_connection()
    # output = connection.send_enable([
    #     'show ip int brief',
    #     'show interfaces',
    #     'show cdp details',
    #     'show ip router'])
    output = connection.send_enable([
        'show interfaces'])
    
    noti = NotificationModel.objects.get(pk=37)
    # task = execute_executor_task.delay(1)
    # task = execute_executor_task(1)
    data['return_output'] = noti.object_url
   
    # GET method:
    return render(request, 'test.html', data)
