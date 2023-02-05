# Django import:
from django.urls import path

# Application import:
from .views.notifications import notifications_test

# App name registration:
app_name = 'test'

# URLs registration:
urlpatterns = [
    path('notifications', notifications_test, name='notifications_test'),
]
