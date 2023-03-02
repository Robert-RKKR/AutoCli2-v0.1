# Django import:
from django.contrib import admin

# base admin class import:
from autocli2.base.admins.based_admin import BaseAdmin

# Notification log model import:
from .models.converted_data import ConvertedData
from .models.execution import Execution
from .models.executor import Executor
from .models.snapshot import Snapshot


# All messenger admin classes:
@admin.register(Executor)
class ExecutorAdmin(BaseAdmin):

    list_display = (
        'name', 'is_active', 'status', 'output', 'results',
        'created', 'updated'
    )
    list_display_links = (
        'name',
    )
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
            'fields': ('is_active', 'created', 'updated', 'name',
                       'description', 'executor_type')
        }),
        ('Task type executor', {
            'classes': ('wide', 'extrapretty',),
            'fields': ('task', 'task_arguments')
        }),
        ('Host type executor', {
            'classes': ('wide', 'extrapretty',),
            'fields': ('execution_protocol', 'hosts',
                       'connection_templates', 'credential')
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
class SnapshotAdmin(BaseAdmin):

    list_display = (
        'name', 'is_active', 'created', 'updated'
    )
    list_display_links = (
        'name',
    )
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
class ConvertedDataAdmin(BaseAdmin):

    list_display = (
        'pk', 'value', 'json_value', 'created', 'updated'
    )
    list_display_links = (
        'pk',
    )
    list_filter = (
        'snapshot',
    )
    search_fields = (
        'value', 'json_value'
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
        'created', 'updated', 'snapshot', 'data_template',
        'execution', 'value', 'json_value'
    )
    empty_value_display = '--None--'


@admin.register(Execution)
class ExecutionAdmin(BaseAdmin):

    list_display = (
        'pk', 'executor', 'hosts', 'connection_templates', 'credential',
        'result_status', 'created', 'updated'
    )
    list_display_links = (
        'pk',
    )
    list_filter = (
        'executor', 'hosts', 'connection_templates', 'credential',
        'result_status'
    )
    search_fields = (
        'value', 'json_value'
    )
    fieldsets = (
        ('Basic information', {
            'classes': ('wide', 'extrapretty',),
            'fields': ('created', 'updated', 'executor')
        }),
        ('Execution information', {
            'classes': ('wide', 'extrapretty',),
            'fields': ('hosts', 'connection_templates', 'credential',
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
        'created', 'updated', 'ssh_raw_data_status', 'ssh_processed_data_status',
        'ssh_raw_data', 'ssh_processed_data', 'https_response_status',
        'https_response_code', 'https_response', 'hosts', 'connection_templates',
        'credential', 'result_status', 'executor'
    )
    empty_value_display = '--None--'
