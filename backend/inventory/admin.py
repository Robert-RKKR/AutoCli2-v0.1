# Django import:
from django.contrib import admin

# base admin class import:
from autocli2.base.admins.based_admin import BaseAdmin

# Notification log model import:
from .models.credentials import Credential
from .models.platform import Platform
from .models.region import Region
from .models.site import Site
from .models.host import Host


# All inventory admin classes:
@admin.register(Credential)
class CredentialAdmin(BaseAdmin):

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
        'name', 'description', 'username'
    )
    fieldsets = (
        ('Basic information', {
            'classes': ('wide', 'extrapretty',),
            'fields': ('is_active', 'created', 'updated', 'name', 'username',
                       'description')
        }),
        ('Security information', {
            'classes': ('wide', 'extrapretty',),
            'fields': ('password', 'token')
        }),
    )
    readonly_fields = (
        'created', 'updated',
    )
    empty_value_display = '--None--'

    
@admin.register(Platform)
class PlatformAdmin(BaseAdmin):

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
        ('Default values', {
            'classes': ('wide', 'extrapretty',),
            'fields': ('api_default_header', 'api_default_params')
        }),
        ('Data information', {
            'classes': ('wide', 'extrapretty',),
            'fields': ('api_data_path',)
        }),
        ('Pagination information', {
            'classes': ('wide', 'extrapretty',),
            'fields': ('api_pagination', 'api_next_page_code_path',
                       'api_next_page_link_path', 'api_pagination_param_key')
        }),
        ('Token information', {
            'classes': ('wide', 'extrapretty',),
            'fields': ('api_token_heder_key', 'api_token_heder_value')
        })
    )
    readonly_fields = (
        'created', 'updated'
    )
    empty_value_display = '--None--'

    
@admin.register(Region)
class RegionAdmin(BaseAdmin):

    list_display = (
        'name', 'is_active', 'code', 'created', 'updated'
    )
    list_display_links = (
        'name',
    )
    list_filter = (
        'is_active',
    )
    search_fields = (
        'name', 'description', 'code'
    )
    fieldsets = (
        ('Basic information', {
            'classes': ('wide', 'extrapretty',),
            'fields': ('is_active', 'created', 'updated', 'name',
                       'code', 'description')
        }),
    )
    readonly_fields = (
        'created', 'updated',
    )
    empty_value_display = '--None--'

    
@admin.register(Site)
class SiteAdmin(BaseAdmin):

    list_display = (
        'name', 'is_active', 'created', 'updated'
    )
    list_display_links = (
        'name',
    )
    list_filter = (
        'is_active', 'region'
    )
    search_fields = (
        'name', 'description', 'code'
    )
    fieldsets = (
        ('Basic information', {
            'classes': ('wide', 'extrapretty',),
            'fields': ('is_active', 'created', 'updated', 'name',
                       'code', 'region', 'description')
        }),
        ('Site details', {
            'classes': ('wide', 'extrapretty',),
            'fields': ('gps_coordinates', 'physical_address'),
        }),
    )
    readonly_fields = (
        'created', 'updated',
    )
    empty_value_display = '--None--'

    
@admin.register(Host)
class HostAdmin(BaseAdmin):
    
    list_display = (
        'name', 'is_active', 'site', 'platform', 'created', 'updated'
    )
    list_display_links = (
        'name',
    )
    list_filter = (
        'is_active', 'site', 'platform', 'credential'
    )
    search_fields = (
        'name', 'description', 'hostname'
    )
    fieldsets = (
        ('Basic information', {
            'classes': ('wide', 'extrapretty',),
            'fields': ('is_active', 'created', 'updated', 'name',
                       'hostname', 'description')
        }),
        ('Detailed information', {
            'classes': ('wide', 'extrapretty',),
            'fields': ('site', 'platform', 'credential')
        }),
        ('Port settings', {
            'classes': ('wide', 'extrapretty',),
            'fields': ('ssh_port', 'http_port', 'certificate_check')
        }),
    )
    readonly_fields = (
        'created', 'updated',
    )
    empty_value_display = '--None--'
