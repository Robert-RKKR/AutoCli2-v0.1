# Django import:
from django.shortcuts import render
from notification.notification import Notification

# Notification:
notification = Notification('Test')

# Test view:
def test(request):

    # Collect data to display:
    data = {
        'page_title': 'Test RKKR - Notifications',
        'output': 'Welcome to notifications test!',
    }

    notifications = []
    notifications.append(notification.critical('Test info notification critical'))
    notifications.append(notification.error('Test info notification error'))
    notifications.append(notification.warning('Test info notification warning'))
    notifications.append(notification.info('Test info notification info'))
    output = notifications

    data['return_output'] = output
   
    # GET method:
    return render(request, 'test.html', data)
