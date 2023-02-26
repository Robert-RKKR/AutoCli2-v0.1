# Django import:
from django.contrib import admin

# Notification log model import:
from .models.converted_data import ConvertedData
from .models.execution import Execution
from .models.executor import Executor
from .models.snapshot import Snapshot


# All messenger admin classes:
admin.site.register(ConvertedData)
admin.site.register(Execution)
admin.site.register(Snapshot)

@admin.register(Executor)
class ExecutorAdmin(admin.ModelAdmin):

    list_display = (
        'name', 'is_active', 'status', 'output', 'results'
    )
    list_display_links = ('name',)
    list_filter = (
        'hosts', 'connection_templates', 'credential',
        'execution_protocol', 'executor_type'
    )
    search_fields = (
        'hosts', 'connection_templates', 'credential',
        'execution_protocol', 'executor_type', 'task'
    )
    fieldsets = (
        ('Basic information', {
            'classes': ('wide', 'extrapretty',),
            'fields': ('is_active', 'created', 'updated', 'name', 'description')
        }),
        ('Type of executor', {
            'classes': ('wide', 'extrapretty',),
            'fields': ('execution_protocol', 'executor_type')
        }),
        ('Task type executor', {
            'classes': ('wide', 'extrapretty',),
            'fields': ('task', 'task_arguments', 'task_id')
        }),
        ('Host type executor', {
            'classes': ('wide', 'extrapretty',),
            'fields': ('hosts', 'connection_templates', 'credential')
        }),
        ('Executor status', {
            'classes': ('wide', 'extrapretty',),
            'fields': ('status', 'output', 'results')
        })
    )
    readonly_fields = (
        'created', 'updated',
    )
    empty_value_display = '(None)'

