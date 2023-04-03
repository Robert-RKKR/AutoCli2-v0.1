# Django - admin import:
from django.contrib import admin

# AutoCli2 - base admin models import:
from autocli2.base.admins.based_admin import BaseAdmin

# AutoCli2 - inventory model import:
from inventory.models.credentials import Credential
from inventory.models.platform import Platform
from inventory.models.region import Region
from inventory.models.site import Site
from inventory.models.host import Host
from inventory.models.tag import Tag


# All inventory admin classes:
@admin.register(Tag)
class TagAdmin(BaseAdmin):

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
            'fields': ('is_active', 'created', 'updated', 'name', 'color',
                       'description')
        }),
    )
    readonly_fields = (
        'created', 'updated',
    )
    empty_value_display = '--None--'


@admin.register(Credential)
class CredentialAdmin(BaseAdmin):

    list_display = (
        'name', 'is_active', 'administrator', 'created', 'updated'
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
                       'description', 'administrator')
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
        ('Supported protocols', {
            'classes': ('wide', 'extrapretty',),
            'fields': ('is_http_supported', 'is_ssh_supported')
        }),
        ('HTTP(S) default values', {
            'classes': ('wide', 'extrapretty',),
            'fields': ('http_default_header', 'http_default_params')
        }),
        ('HTTP(S) data information', {
            'classes': ('wide', 'extrapretty',),
            'fields': ('http_data_path',)
        }),
        ('HTTP(S) pagination information', {
            'classes': ('wide', 'extrapretty',),
            'fields': ('http_pagination', 'http_next_page_code_path',
                       'http_next_page_link_path', 'http_pagination_param_key')
        }),
        ('HTTP(S) token information', {
            'classes': ('wide', 'extrapretty',),
            'fields': ('http_token_heder_key', 'http_token_heder_value')
        }),
        ('SSH information', {
            'classes': ('wide', 'extrapretty',),
            'fields': ('ssh_invalid_responses', 'ssh_device_type')
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
        'name', 'hostname', 'is_active', 'site', 'platform',
        'data_collection_protocol', 'created', 'updated'
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
                       'hostname', 'data_collection_protocol', 'description')
        }),
        ('Detailed information', {
            'classes': ('wide', 'extrapretty',),
            'fields': ('site', 'platform', 'credential', 'tag')
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
