# Django import:
from django.urls import path

# Application import:
from data.inventory.views import test

# App name registration:
app_name = 'inventory'

# URLs registration:
urlpatterns = [
    path('test/', test, name='test'),
]
