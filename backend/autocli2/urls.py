# Django import:
from django.contrib import admin
from django.urls import include
from django.urls import path, re_path

# URLs registration:
urlpatterns = [
    path('admin/', admin.site.urls),

    # Test view registration:
    path('test/', include('a_test.urls')),
]
