# Django - admin import:
from django.contrib import admin

# AutoCli2 - base admin models import:
from autocli2.base.admins.based_admin import BaseAdmin

# AutoCli2 - notification model import:
from notification.models.notification import Notification
from notification.models.change_log import ChangeLog


# All notification admin classes:
@admin.register(Notification)
class NotificationAdmin(BaseAdmin):

    list_display = (
        'pk', 'timestamp', 'action_type', 'object_id',
        'object_representation', 'severity', 'notification_type',
        'task_id', 'application', 'message',
    )
    list_display_links = (
        'pk',
    )
    list_filter = (
        'app_name', 'administrator', 'model_name', 'action_type',
        'notification_type', 'severity', 'application',
    )
    search_fields = (
        'message', 'object_representation', 'task_id', 'object_id',
    )
    fieldsets = (
        ('Basic information', {
            'classes': ('wide', 'extrapretty',),
            'fields': ('administrator', 'notification_type', 'severity',
                       'task_id', 'application',)
        }),
        ('Notification information', {
            'classes': ('wide', 'extrapretty',),
            'fields': ('app_name', 'model_name', 'object_representation',
                       'object_id', 'object_url'),
        }),
        ('Message', {
            'classes': ('wide', 'extrapretty',),
            'fields': ('message',),
        }),
        ('Execution time', {
            'classes': ('wide', 'extrapretty',),
            'fields': ('execution_time',),
        }),
    )
    readonly_fields = (
        'timestamp', 'notification_type', 'object_representation', 'severity',
        'notification_type', 'task_id', 'application', 'message', 'app_name',
        'model_name', 'object_representation', 'object_id', 'administrator',
        'object_url'
    )
    empty_value_display = '--None--'


@admin.register(ChangeLog)
class ChangLogAdmin(BaseAdmin):

    list_display = (
        'pk', 'administrator', 'timestamp', 'action_type', 'model_name',
        'object_representation',
    )
    list_display_links = (
        'pk',
    )
    list_filter = (
        'app_name', 'administrator', 'model_name', 'action_type',
        'after',
    )
    search_fields = (
        'object_representation', 'object_id', 'after',
    )
    fieldsets = (
        ('Basic information', {
            'classes': ('wide', 'extrapretty',),
            'fields': ('administrator', 'app_name', 'model_name',
                       'object_representation', 'object_id', 'object_url')
        }),
        ('Object Json representation', {
            'classes': ('wide', 'extrapretty',),
            'fields': ('after',),
        }),
    )
    readonly_fields = (
        'administrator', 'timestamp', 'action_type', 'administrator', 'app_name',
        'object_representation', 'after', 'object_id', 'model_name', 'object_url'
    )
    empty_value_display = '--None--'
