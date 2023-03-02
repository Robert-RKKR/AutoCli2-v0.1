# Django import:
from django.contrib import admin

# Notification log model import:
from .models.administrator_settings import AdministratorSetting
from .models.global_settings import GlobalSetting
# from .models.administrator import Administrator


# All management admin classes:
@admin.register(GlobalSetting)
class GlobalSettingAdmin(admin.ModelAdmin):

    list_display = (
        'pk', 'is_active', 'name', 'is_current', 'created', 'updated'
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


@admin.register(AdministratorSetting)
class AdministratorSettingAdmin(admin.ModelAdmin):

    list_display = (
        'pk', 'default_credentials',
    )
    search_fields = (
        'pk',
    )
    fieldsets = (
        ('Basic information', {
            'classes': ('wide', 'extrapretty',),
            'fields': ('default_credentials', 'administrator')
        }),
    )
