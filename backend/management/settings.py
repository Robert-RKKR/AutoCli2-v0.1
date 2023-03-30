# Python - library import:
import json

# Settings model import:
from .models.global_setting import GlobalSetting

# Django signals import:
from django.core.serializers import serialize

# Global settings dictionary:
global_settings = {}

# Helper function:
def update_global_settings_dictionary(instance):
    # Collect global settings object content:
    json_str = serialize('json', [instance],
        use_natural_foreign_keys=True, use_natural_primary_keys=True)
    data = json.loads(json_str)[0]['fields']
    # Update global settings dictionary:
    global_settings.update(data)

# Collect global settings function:
def collect_global_settings(key: str):
    """ Collect global settings. """

    if global_settings:
        # Collect data from global settings dictionary:
        return global_settings.get(key, False)
    else:
        try: # Try to collect global settings if they exist:
            collect_settings = GlobalSetting.objects.get(is_current=True)
        except:
            collect_settings = GlobalSetting.objects.create()
        finally:
            # Update global settings dictionary:
            update_global_settings_dictionary(collect_settings)
            # Collect data from global settings dictionary:
            return global_settings.get(key, False)
