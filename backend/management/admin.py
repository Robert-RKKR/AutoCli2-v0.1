# Django - admin import:
from django.contrib import admin

# AutoCli2 - base admin models import:
from autocli2.base.admins.based_admin import BaseAdmin

# AutoCli2 - management model import:
from management.models.global_settings import GlobalSettings


@admin.register(GlobalSettings)
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
            'fields': ('notification_level', 'logger_level'),
        }),
        ('Timeout settings', {
            'classes': ('wide', 'extrapretty',),
            'fields': ('http_timeout', 'ssh_timeout'),
        }),
        ('SSH settings', {
            'classes': ('wide', 'extrapretty',),
            'fields': ('ssh_invalid_responses',),
        }),
    )
