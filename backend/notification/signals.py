# Python import:
import json

# Django signals import:
from django.core.serializers import serialize

# Settings import:
from django.conf import settings

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

    # Try to collect object representation:
    try:
        # Collect natural key like object representation:
        object_representation = instance.natural_key()
    except:
        try:
            # Collect name value like object representation:
            object_representation = instance.name
        except:
            try:
                # Collect PK / ID value like object representation:
                object_representation = instance.pk
            except:
                # Return non like object representation:
                return None
    
    # Return object representation:
    return object_representation

# Post save signal:
def post_save_change_signal(sender, instance=None, created=False, **kwargs):
    """
    When application will receive a new post save signal in case of new
    object creation, the function will check if provided object model
    belongs to the group of models supporting change tracking
    (In application settings), change tracking will create a new
    change log object to keep information about the change occurred.
    """

    # Application change log import:
    from notification.models.change_log import ChangeLog
    
    change_log_action = 0
    # Check if object was created
    if created:
        change_log_action = 1
    else:
        change_log_action = 2

    # Collect base content type information:
    collected_names = collect_names(sender)
    
    if collected_names in settings.CHANGE_LOG_MODELS:
        # Collect object content:
        json_str = serialize('json', [instance], use_natural_foreign_keys=True,
            use_natural_primary_keys=True)
        data = json.loads(json_str)[0]['fields']
        # Try to create a new change log:
        try:
            ChangeLog.objects.create(
                action=change_log_action,
                app_name=collected_names[0],
                model_name=collected_names[1],
                object_id=instance.pk,
                object_representation=collect_object_representation(instance),
                after=data,
            )
        except: # Pass if sender was not register:
            pass

# Post delete signal:
def post_delete_change_signal(sender, instance=None, origin=None, **kwargs):
    """
    When application will receive a new post delete signal in case of
    new object creation, the function will check if provided object
    model belongs to the group of models supporting change tracking
    (In application settings), change tracking will create a new
    change log object to keep information about the change occurred.
    """

    # Application change log import:
    from notification.models.change_log import ChangeLog

    # Collect base content type information:
    collected_names = collect_names(sender)

    # Try to create a new change log:
    if collected_names in settings.CHANGE_LOG_MODELS:
        try:
            ChangeLog.objects.create(
                action=3,
                app_name=collected_names[0],
                model_name=collected_names[1],
                object_id=instance.pk,
                object_representation=collect_object_representation(
                    instance),
            )
        except: # Pass if sender was not register:
            pass
