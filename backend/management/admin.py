# Django import:
from django.contrib import admin

# Notification log model import:
from .models.administrator_settings import AdministratorSetting
from .models.global_settings import GlobalSetting
# from .models.administrator import Administrator


# All messenger admin classes:
admin.site.register(AdministratorSetting)
# admin.site.register(Administrator)

# All management admin classes:
@admin.register(GlobalSetting)
class GlobalSettingAdmin(admin.ModelAdmin):

    list_display = (
        'pk', 'name', 'is_current',
    )
    search_fields = (
        'name',
    )
    fieldsets = (
        ('Basic information', {
            'classes': ('wide', 'extrapretty',),
            'fields': ('is_current', 'name', 'description',)
        }),
        ('Notification settings', {
            'classes': ('wide', 'extrapretty',),
            'fields': ('notification_level', 'logger_level',),
        }),
    )
