# Django import:
from django.contrib import admin

# Notification log model import:
from .models.credentials import Credential
from .models.platform import Platform
from .models.region import Region
from .models.site import Site
from .models.host import Host


# All messenger admin classes:
admin.site.register(Credential)
admin.site.register(Platform)
admin.site.register(Region)
admin.site.register(Site)
admin.site.register(Host)
