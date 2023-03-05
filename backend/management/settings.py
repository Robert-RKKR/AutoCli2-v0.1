# Settings model import:
from .models.administrator_settings import AdministratorSetting
from .models.global_settings import GlobalSetting

def collect_global_settings(key: str):
    """Xxx. """
    # Try to collect global settings if they exist:
    try:
        collect_settings = GlobalSetting.objects.get(is_current=True)
    except:
        collect_settings = GlobalSetting.objects.create()
    finally:
        try: # Try to collect key value:
            return getattr(collect_settings, key)
        except:
            return False
        
def collect_user_settings(key: str, administrator):
    """Xxx. """
    # Try to collect global settings if they exist:
    try:
        collect_settings = AdministratorSetting.objects.get(administrator=administrator)
    except:
        collect_settings = None
    finally:
        try: # Try to collect key value:
            return getattr(collect_settings, key)
        except:
            return False
