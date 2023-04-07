# Python - JSON import:
import json

# Django - serializers import:
from django.core.serializers import serialize

# Django - user model import:
from django.contrib.auth.models import User

# AutoCli2 - base models import:
from autocli2.base.models.base_model import BaseModel

# AutoCli2 - notification model import:
from notification.models.change_log import ChangeLog

# AutoCli2 - application logger import:
from notification.system_logs import application_logger

def collect_names(sender):
    """
    Collect base content type information,
    like application and model names.
    """

    # Try to collect base content type information:
    try:
        app_name = sender._meta.app_label
        model_name = sender.__name__
    except:
        app_name = None
        model_name = None

    # Return names toupee:
    return (app_name, model_name)

def collect_object_representation(instance):
    """
    Collect object representation,
    like natural key or name or pk / id.
    """

    try: # Try to collect object representation:
        # Collect natural key like object representation:
        object_representation = instance.natural_key()
    except:
        try: # Try to collect name value like object representation:
            object_representation = instance.name
        except: # If object doesn't have name value:
            try: # Try to collect PK / ID value like object representation:
                object_representation = instance.pk
            except: # Return non like object representation:
                return None
    
    # Return object representation:
    return object_representation


def log_change(
        instance: BaseModel,
        administrator: User,
        change_log_action,
    ) -> ChangeLog:
    """
    Xxx.
    """

    # Check collected data:
    if not isinstance(administrator, User):
        administrator = None
    if not isinstance(instance, BaseModel) and not isinstance(instance, User):
        raise TypeError('Provided instance is not a valid AutoLci 2 model.')

    # Collect sender class:
    sender = instance.__class__
    # Collect object content:
    json_str = serialize('json', [instance], use_natural_foreign_keys=True,
        use_natural_primary_keys=True)
    object_data = json.loads(json_str)[0]['fields']
    # Collect base content type information:
    collected_names = collect_names(sender)
    try: # Try to create a new change log:
        change_log = ChangeLog.objects.create(
            administrator=administrator,
            action_type=change_log_action,
            app_name=collected_names[0],
            model_name=collected_names[1],
            object_id=instance.pk,
            object_representation=collect_object_representation(instance),
            after=object_data)
    except Exception as error:
        application_logger.error(error)
        return False
    else:
        return change_log
