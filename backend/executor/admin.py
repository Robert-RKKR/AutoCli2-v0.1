# Django - admin import:
from django.contrib import admin

# AutoCli2 - base admin models import:
from autocli2.base.admins.based_admin import BaseAdmin

# AutoCli2 - executor model import:
from executor.models.executor import ExecutorConnectionTemplate
from executor.models.converted_data import ConvertedData
from executor.models.execution import Execution
from executor.models.executor import Executor
from executor.models.snapshot import Snapshot


# All messenger admin classes:
@admin.register(Executor)
class ExecutorAdmin(BaseAdmin):

    list_display = (
        'name', 'is_active', 'created', 'updated'
    )
    list_display_links = (
        'name',
    )
    list_filter = (
        'is_active', 'connection_templates',
    )
    search_fields = (
        'hosts', 'connection_templates', 'credential', 'description'
    )
    fieldsets = (
        ('Basic information', {
            'classes': ('wide', 'extrapretty',),
            'fields': ('is_active', 'created', 'updated', 'name',
                       'description', 'interval')
        }),
        ('Host type executor', {
            'classes': ('wide', 'extrapretty',),
            'fields': ('hosts',)
        })
    )
    readonly_fields = (
        'created', 'updated',
    )
    empty_value_display = '--None--'


# All messenger admin classes:
@admin.register(ExecutorConnectionTemplate)
class ExecutorConnectionTemplateAdmin(BaseAdmin):
    
    
    fieldsets = (
        ('Basic information', {
            'classes': ('wide', 'extrapretty',),
            'fields': ('order', 'executor', 'connection_template')
        }),
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

    actions = [
        'export_hosts'
    ]
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

    actions = [
        'export_hosts'
    ]
    list_display = (
        'pk', 'executor', 'host', 'connection_template', 'credential',
        'task_id', 'execution_status', 'created', 'updated'
    )
    list_display_links = (
        'pk',
    )
    list_filter = (
        'executor', 'host', 'connection_template', 'credential',
        'execution_status'
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
            'fields': ('host', 'host_representation', 'connection_template',
                       'connection_template_representation', 'credential',
                       'credential_representation', 'task_id',
                       'execution_status')
        }),
        ('Collected SSH data', {
            'classes': ('wide', 'extrapretty',),
            'fields': ('ssh_raw_data_status', 'ssh_processed_data_status',
                       'ssh_raw_data', 'ssh_processed_data')
        }),
        ('Collected HTTP(S) data', {
            'classes': ('wide', 'extrapretty',),
            'fields': ('http_response_code', 'http_response')
        }),
    )
    readonly_fields = (
        'created', 'updated', 'ssh_raw_data_status', 'ssh_processed_data_status',
        'ssh_raw_data', 'ssh_processed_data', 'credential_representation',
        'http_response_code', 'http_response', 'host', 'connection_template',
        'credential', 'execution_status', 'executor', 'task_id',
        'host_representation', 'connection_template_representation'
    )
    empty_value_display = '--None--'
