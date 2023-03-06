# Settings model import:
from .models.administrator_settings import AdministratorSetting
from .models.global_settings import GlobalSetting

# Django signals import:
from django.core.serializers import serialize

# Global settings dictionary:
globa_settings = {}

# Helper function:
def update_global_settings_dictionary(instance):
    # Collect global settings object content:
    json_str = serialize('json', [instance],
        use_natural_foreign_keys=True, use_natural_primary_keys=True)
    data = json.loads(json_str)[0]['fields']
    # Update global settings dictionary:
    globa_settings.update(data)

# Collect global settings function:
def collect_global_settings(key: str):
    """ Collect global settings. """

    if globa_settings:
        # Collect data from global settings dictionary:
        return globa_settings.get(key, False)
    else:
        try: # Try to collect global settings if they exist:
            collect_settings = GlobalSetting.objects.get(is_current=True)
        except:
            collect_settings = GlobalSetting.objects.create()
        finally:
            # Update global settings dictionary:
            update_global_settings_dictionary(collect_settings)
            # Collect data from global settings dictionary:
            return globa_settings.get(key, False)

# Collect administrator settings function:
# def collect_administrator_settings(key: str, administrator):
#     """ Collect administrator settings. """
#     # Try to collect global settings if they exist:
#     try:
#         collect_settings = AdministratorSetting.objects.get(administrator=administrator)
#     except:
#         collect_settings = None
#     finally:
#         try: # Try to collect key value:
#             return getattr(collect_settings, key)
#         except:
#             return False
