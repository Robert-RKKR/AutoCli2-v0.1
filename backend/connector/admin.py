# Django import:
from django.contrib import admin

# Models import:
from .models.connection_group import ConnectionGroup
from .models.connection_template import ConnectionTemplate
from .models.data_group_template import DataGroupTemplate
from .models.data_template import DataTemplate
from .models.model_group_template import ModelGroupTemplate
from .models.model_template import ModelTemplate


# All connectors admin classes:
@admin.register(ConnectionGroup)
class ConnectionGroupAdmin(admin.ModelAdmin):

    list_display = (
        'pk', 'created', 'updated', 'name',
    )
    search_fields = (
        'name',
    )
    fieldsets = (
        ('Basic information', {
            'classes': ('wide', 'extrapretty',),
            'fields': ('is_active', 'name', 'slug', 'description', 'ico',)
        }),
    )

    
@admin.register(ConnectionTemplate)
class ConnectionTemplateAdmin(admin.ModelAdmin):

    list_display = (
        'pk', 'created', 'updated', 'name', 'execution_protocol', 'ssh_command', 'http_url',
    )
    list_filter = (
        'execution_protocol', 'ssh_type', 'http_method',
    )
    search_fields = (
        'name', 'ssh_command', 'http_url', 'http_header', 'http_body', 'http_params',
    )
    fieldsets = (
        ('Basic information', {
            'classes': ('wide', 'extrapretty',),
            'fields': ('is_active', 'name', 'slug', 'description', 'ico', 'execution_protocol',)
        }),
        ('SSH information', {
            'classes': ('wide', 'extrapretty',),
            'fields': ('ssh_type', 'ssh_command', 'ssh_fsm',),
        }),
        ('http information', {
            'classes': ('wide', 'extrapretty',),
            'fields': ('http_method', 'http_url', 'http_header', 'http_params', 'http_body', 'http_pagination', 'http_pagination_path',),
        }),
    )

    
@admin.register(DataGroupTemplate)
class DataGroupTemplateAdmin(admin.ModelAdmin):

    list_display = (
        'pk', 'created', 'updated', 'model_group_template', 'connection_template',
    )
    list_filter = (
        'model_group_template', 'connection_template',
    )
    search_fields = (
        'keys', 'keys_regex',
    )
    fieldsets = (
        ('Basic information', {
            'classes': ('wide', 'extrapretty',),
            'fields': ('is_active', 'model_group_template', 'connection_template',)
        }),
        ('Data group specific fields', {
            'classes': ('wide', 'extrapretty',),
            'fields': ('keys', 'keys_regex',),
        }),
    )

    
@admin.register(DataTemplate)
class DataTemplateAdmin(admin.ModelAdmin):

    list_display = (
        'pk', 'created', 'updated',
    )
    list_filter = (
        'data_group_template', 'model_template',
    )
    search_fields = (
        'path',
    )
    fieldsets = (
        ('Basic information', {
            'classes': ('wide', 'extrapretty',),
            'fields': ('is_active', 'data_group_template', 'model_template',)
        }),
        ('Data path', {
            'classes': ('wide', 'extrapretty',),
            'fields': ('path',),
        }),
    )

    
@admin.register(ModelGroupTemplate)
class ModelGroupTemplateAdmin(admin.ModelAdmin):

    list_display = (
        'pk', 'created', 'updated', 'name',
    )
    search_fields = (
        'name',
    )
    fieldsets = (
        ('Basic information', {
            'classes': ('wide', 'extrapretty',),
            'fields': ('is_active', 'name', 'slug', 'description', 'ico',)
        }),
    )

    
@admin.register(ModelTemplate)
class ModelTemplateAdmin(admin.ModelAdmin):

    list_display = (
        'pk', 'created', 'updated', 'name',
    )
    list_filter = (
        'model_group_template',
    )
    search_fields = (
        'name',
    )
    fieldsets = (
        ('Basic information', {
            'classes': ('wide', 'extrapretty',),
            'fields': ('is_active', 'name', 'slug', 'description', 'ico', 'model_group_template',)
        }),
    )
