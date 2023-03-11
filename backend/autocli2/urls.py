# Django import:
from django.contrib import admin
from django.urls import include
from django.urls import path, re_path

# URLs registration:
urlpatterns = [
    path('admin/', admin.site.urls),

    # Test view registration:
    path('test/', include('a_test.urls')),

    # Network API view registration:
    path('api-inventory/', include('inventory.api.urls')),

    # API taks views:
    path('api-task/', include('executor.api.urls')),
]
