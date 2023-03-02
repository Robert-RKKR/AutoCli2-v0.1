# Python import:
import decimal
import json
import csv

# Django import:
from django.core.serializers import serialize
from django.http import HttpResponse
from django.contrib import messages
from django.contrib import admin

# Constants:
KEY_TO_FILTER = [
    'is_root',
    'is_deleted',
    'ico'
]

# Helper function:
def collect_keys(queryset):
    """ Collect model keys. """

    for query_object in queryset:
        try: # Try to collect model keys:
            raw_data = serialize('json', [query_object],
                use_natural_foreign_keys=True, use_natural_primary_keys=True)
            dict_data = json.loads(raw_data)[0]['fields']
            keys = list(dict_data.keys())
        except: # Return an empty list on failure:
            return []
        else:
            # Filter key:
            return_key = []
            for key in keys:
                if not key in KEY_TO_FILTER:
                    return_key.append(key)
            # Return filtered keys:
            return return_key


# Base admin class:
class BaseAdmin(admin.ModelAdmin):

    actions = [
        'make_nonactive',
        'make_active',
        'export_hosts'
    ]

    @admin.action(description='Export to CSV')
    def export_hosts(modeladmin, request, queryset):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="hosts.csv"'
        writer = csv.writer(response)
        keys = collect_keys(queryset)
        writer.writerow(keys)
        query_objects = queryset.values_list(*keys)
        for query_object in query_objects:
            writer.writerow(query_object)
        return response
    
    @admin.action(description='Make device nonactive')
    def make_nonactive(self, request, queryset):
        updated = queryset.update(is_active=False)
        self.message_user(request,
            '%d device was successfully marked as active.'
            % updated, messages.SUCCESS)

    @admin.action(description='Make device active')
    def make_active(self, request, queryset):
        change = queryset.update(is_active=True)
        self.message_user(request, '%d device was successfully marked as active.')
