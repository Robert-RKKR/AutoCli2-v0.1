# Django import:
from django.contrib import admin

# Notification log model import:
from message.notification.models.notification import Notification


# Notification admin class:
@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):

    list_display = (
        'pk', 'timestamp', 'object_id', 'app_name', 'model_name', 'type', 'severity', 'task_id', 'application', 'message',
    )
    list_filter = (
        'app_name', 'model_name', 'type', 'severity', 'task_id',
    )
    search_fields = (
        'message',
    )
    fieldsets = (
        ('Basic information', {
            'classes': ('wide', 'extrapretty',),
            'fields': ('type', 'severity', 'task_id', 'application',)
        }),
        ('Change object information', {
            'classes': ('wide', 'extrapretty',),
            'fields': ('app_name', 'model_name', 'object_id',),
        }),
        ('Message', {
            'classes': ('wide', 'extrapretty',),
            'fields': ('message',),
        }),
    )
