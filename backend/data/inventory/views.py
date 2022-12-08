# Django import:
from django.shortcuts import render

# Test view:
def test(request):

    # Collect data to display:
    data = {
        'page_title': 'Test RKKR',
        'output': 'Welcome!',
    }
    
    # GET method:
    return render(request, 'test.html', data)