# Django import:
from django.contrib import admin

# Notification log model import:
from connectors.models.connection_template import ConnectionTemplate


# Messenger admin classes:
@admin.register(ConnectionTemplate)
class ConnectionTemplateAdmin(admin.ModelAdmin):

    list_display = (
        'pk', 'created', 'updated', 'name', 'execution_method', 'ssh_command', 'https_url',
    )
    list_filter = (
        'execution_method', 'ssh_type', 'https_method', 'certificate',
    )
    search_fields = (
        'name', 'ssh_command', 'https_url', 'https_header', 'https_body', 'https_params',
    )
    fieldsets = (
        ('Basic information', {
            'classes': ('wide', 'extrapretty',),
            'fields': ('is_active', 'is_root', 'name', 'slug', 'description', 'ico', 'execution_method',)
        }),
        ('SSH information', {
            'classes': ('wide', 'extrapretty',),
            'fields': ('ssh_type', 'ssh_command', 'ssh_fsm',),
        }),
        ('HTTPS information', {
            'classes': ('wide', 'extrapretty',),
            'fields': ('https_method', 'https_url', 'https_header', 'https_params', 'https_body', 'https_pagination', 'https_pagination_path',),
        }),
        ('Certificate information', {
            'classes': ('wide', 'extrapretty',),
            'fields': ('certificate',),
        }),
    )
