# Django - admin import:
from django.contrib import admin

# AutoCli2 - base admin models import:
from autocli2.base.admins.based_admin import BaseAdmin

# AutoCli2 - management model import:
from management.models.administrator_settings import AdministratorSetting
from management.models.global_settings import GlobalSetting
# from management.models.administrator import Administrator


# All management admin classes:
@admin.register(GlobalSetting)
class GlobalSettingAdmin(BaseAdmin):

    list_display = (
        'pk', 'name', 'is_current', 'created', 'updated'
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
class AdministratorSettingAdmin(BaseAdmin):

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
