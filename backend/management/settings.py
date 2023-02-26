# Settings model import:
from .models.global_settings import GlobalSetting

def collect_global_settings(key: str):
    """Xxx. """
    # Try to collect global settings if they exist:
    try:
        collect_settings = GlobalSetting.objects.get(is_current=True)
    except:
        collect_settings = GlobalSetting.objects.create(
            name='Default', slug='default')
    finally:
        try: # Try to collect key value:
            return getattr(collect_settings, key)
        except:
            return False
