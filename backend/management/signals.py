# Django - models import:
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver

# AutoCli2 - management model import:
from management.models.global_settings import GlobalSetting

# AutoCli2 - settings function import:
from management.settings import update_global_settings_dictionary

# Signals functions:
@receiver(post_save, sender=GlobalSetting)
def global_settings_edit(
    sender: GlobalSetting,
    instance: GlobalSetting,
    created, **kwargs):
    """
    Signal Make sure that there are no other objects
    that have field 'is_current' set to True.
    """
    
    # Check if a new settings object current value is True:
    if instance.is_current == True:
        # Update global settings dictionary:
        update_global_settings_dictionary(instance)
        # Collect current global settings if they exist:
        collect_settings = sender.objects.filter(is_current=True)
        if collect_settings:
            # Iterate thru all collected global settings:
            for settings in collect_settings:
                # Change other global settings (Except current one) 
                # 'current' value to False:
                if settings.pk != instance.pk:
                    settings.is_current = False
                    settings.save(update_fields=['is_current'])
    else:
        # Collect current global settings if they exist:
        collect_settings = sender.objects.filter(is_current=True)
        if not collect_settings:
            # Update global settings dictionary:
            update_global_settings_dictionary(instance)
            # Change current global settings object, 'current' value to True:
            instance.is_current = True
            instance.save(update_fields=['is_current'])

@receiver(pre_delete, sender=GlobalSetting)
def global_settings_delete(instance: GlobalSetting, **kwargs):
    """
    Signal Make sure that there always is one object
    that have field 'is_current' set to True.
    """

    if instance.is_current == True:
        try: # Try to collect default global settings object:
           collect_settings = GlobalSetting.objects.get(name='Default')
        except:
            # Create default global settings object:
            collect_settings = GlobalSetting.objects.create(
                name='Default', is_current=True)
        else:
            collect_settings.is_current = False
            collect_settings.save(update_fields=['is_current'])
        finally:
            # Update global settings dictionary:
            update_global_settings_dictionary(collect_settings)
