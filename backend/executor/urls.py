# Django import:
from django.urls import path

# Application import:
from .views.test import test

# App name registration:
app_name = 'test'

# URLs registration:
urlpatterns = [
    path('test', test, name='test'),
]
