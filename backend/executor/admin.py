# Django import:
from django.contrib import admin

# Notification log model import:
from .models.converted_data import ConvertedData
from .models.execution import Execution
from .models.executor import Executor
from .models.snapshot import Snapshot


# All messenger admin classes:
@admin.register(Executor)
class ExecutorAdmin(admin.ModelAdmin):

    list_display = (
        'name', 'is_active', 'status', 'output', 'results'
    )
    list_display_links = ('name',)
    list_filter = (
        'is_active', 'connection_templates', 'credential',
        'execution_protocol', 'executor_type'
    )
    search_fields = (
        'hosts', 'connection_templates', 'credential',
        'execution_protocol', 'executor_type', 'task',
        'description'
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
    empty_value_display = '--None--'


@admin.register(Snapshot)
class SnapshotAdmin(admin.ModelAdmin):

    list_display = (
        'name', 'is_active', 'status', 'created'
    )
    list_display_links = ('name',)
    list_filter = (
        'is_active', 'created'
    )
    search_fields = (
        'name', 'description',
    )
    fieldsets = (
        ('Basic information', {
            'classes': ('wide', 'extrapretty',),
            'fields': ('is_active', 'created', 'updated', 'name', 'description')
        }),
    )
    readonly_fields = (
        'created', 'updated',
    )
    empty_value_display = '--None--'


@admin.register(ConvertedData)
class ConvertedDataAdmin(admin.ModelAdmin):

    list_display = (
        'pk', 'created', 'updated', 'value', 'json_value'
    )
    list_display_links = ('pk',)
    list_filter = (
        'is_active', 'snapshot'
    )
    search_fields = (
        'name', 'description', 'value', 'json_value'
    )
    fieldsets = (
        ('Basic information', {
            'classes': ('wide', 'extrapretty',),
            'fields': ('created', 'updated', 'snapshot',
                        'data_template', 'execution')
        }),
        ('Converted data', {
            'classes': ('wide', 'extrapretty',),
            'fields': ('value', 'json_value')
        }),
    )
    readonly_fields = (
        'created', 'updated',
    )
    empty_value_display = '--None--'


@admin.register(Execution)
class ExecutionAdmin(admin.ModelAdmin):

    list_display = (
        'pk', 'executor', 'hosts', 'connection_templates', 'credential', 'result_status'
    )
    list_display_links = ('pk',)
    list_filter = (
        'is_active', 'snapshot'
    )
    search_fields = (
        'name', 'description', 'value', 'json_value'
    )
    fieldsets = (
        ('Basic information', {
            'classes': ('wide', 'extrapretty',),
            'fields': ('created', 'updated', 'executor',
                        'hosts', 'connection_templates', 'credential',
                        'result_status')
        }),
        ('Status information', {
            'classes': ('wide', 'extrapretty',),
            'fields': ('ssh_raw_data_status', 'ssh_processed_data_status')
        }),
        ('Collected SSH data', {
            'classes': ('wide', 'extrapretty',),
            'fields': ('ssh_raw_data', 'ssh_processed_data')
        }),
        ('Collected HTTP(S) data', {
            'classes': ('wide', 'extrapretty',),
            'fields': ('https_response_status', 'https_response_code',
                        'https_response')
        }),
    )
    readonly_fields = (
        'created', 'updated',
    )
    empty_value_display = '--None--'
