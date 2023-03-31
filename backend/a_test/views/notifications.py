# Django import:
import json
from django.shortcuts import render
from notification.notification import Notification

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

    data['return_output'] = return_output
   
    # GET method:
    return render(request, 'test.html', data)
