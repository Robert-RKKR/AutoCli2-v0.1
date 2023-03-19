# Django - admin import:
from django.contrib import admin

# AutoCli2 - base admin models import:
from autocli2.base.admins.based_admin import BaseAdmin

# AutoCli2 - connector model import:
from connector.models.connection_template import ConnectionTemplate
from connector.models.data_group_template import DataGroupTemplate
from connector.models.data_template import DataTemplate
from connector.models.model_group_template import ModelGroupTemplate
from connector.models.model_template import ModelTemplate


# All connectors admin classes:
@admin.register(ConnectionTemplate)
class ConnectionTemplateAdmin(BaseAdmin):

    list_display = (
        'name', 'is_active', 'execution_protocol',
        'ssh_command', 'http_url', 'created', 'updated'
    )
    list_display_links = (
        'name',
    )
    list_filter = (
        'is_active', 'execution_protocol', 'ssh_type', 'http_method',
    )
    search_fields = (
        'name', 'description', 'ssh_command', 'http_url', 'http_header',
        'http_body', 'http_params',
    )
    fieldsets = (
        ('Basic information', {
            'classes': ('wide', 'extrapretty',),
            'fields': ('is_active', 'created', 'updated', 'name', 'description',
                       'execution_protocol', 'platforms')
        }),
        ('SSH information', {
            'classes': ('wide', 'extrapretty',),
            'fields': ('ssh_type', 'ssh_command', 'ssh_template'),
        }),
        ('HTTP/S information', {
            'classes': ('wide', 'extrapretty',),
            'fields': ('http_method', 'http_url', 'http_body', 'http_params'),
        }),
        ('Output validation', {
            'classes': ('wide', 'extrapretty',),
            'fields': ('regex_expression', 'response_type'),
        })
    )
    readonly_fields = (
        'created', 'updated',
    )
    empty_value_display = '--None--'

    
@admin.register(ModelGroupTemplate)
class ModelGroupTemplateAdmin(BaseAdmin):

    list_display = (
        'name', 'is_active', 'created', 'updated'
    )
    list_display_links = (
        'name',
    )
    list_filter = (
        'is_active',
    )
    search_fields = (
        'name', 'description'
    )
    fieldsets = (
        ('Basic information', {
            'classes': ('wide', 'extrapretty',),
            'fields': ('is_active', 'created', 'updated', 'name',
                       'description')
        }),
    )
    readonly_fields = (
        'created', 'updated',
    )
    empty_value_display = '--None--'

    
@admin.register(ModelTemplate)
class ModelTemplateAdmin(BaseAdmin):

    list_display = (
        'name', 'is_active', 'created', 'updated'
    )
    list_display_links = (
        'name',
    )
    list_filter = (
        'is_active', 'model_group_template'
    )
    list_filter = (
        'model_group_template',
    )
    search_fields = (
        'name', 'description'
    )
    fieldsets = (
        ('Basic information', {
            'classes': ('wide', 'extrapretty',),
            'fields': ('is_active', 'created', 'updated', 'name', 'description',
                       'model_group_template')
        }),
    )
    readonly_fields = (
        'created', 'updated'
    )
    empty_value_display = '--None--'
    

    
@admin.register(DataGroupTemplate)
class DataGroupTemplateAdmin(BaseAdmin):

    list_display = (
        'pk', 'is_active', 'model_group_template', 'connection_template',
        'created', 'updated'
    )
    list_display_links = (
        'pk',
    )
    list_filter = (
        'is_active', 'model_group_template', 'connection_template'
    )
    search_fields = (
        'keys', 'keys_regex'
    )
    fieldsets = (
        ('Basic information', {
            'classes': ('wide', 'extrapretty',),
            'fields': ('is_active', 'created', 'updated',
                        'model_group_template', 'connection_template',
                        'platform')
        }),
        ('Data group specific fields', {
            'classes': ('wide', 'extrapretty',),
            'fields': ('keys', 'keys_regex',),
        }),
    )
    readonly_fields = (
        'created', 'updated'
    )
    empty_value_display = '--None--'

    
@admin.register(DataTemplate)
class DataTemplateAdmin(BaseAdmin):

    list_display = (
        'pk', 'is_active', 'created', 'updated'
    )
    list_display_links = (
        'pk',
    )
    list_filter = (
        'is_active', 'data_group_template', 'model_template'
    )
    search_fields = (
        'path',
    )
    fieldsets = (
        ('Basic information', {
            'classes': ('wide', 'extrapretty',),
            'fields': ('is_active', 'created', 'updated',
                        'data_group_template', 'model_template')
        }),
        ('Data path', {
            'classes': ('wide', 'extrapretty',),
            'fields': ('path',),
        }),
    )
    readonly_fields = (
        'created', 'updated'
    )
    empty_value_display = '--None--'
