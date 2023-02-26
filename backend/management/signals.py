# Django import:
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver

# Settings model import:
from .models.global_settings import GlobalSetting

# 
@receiver(post_save, sender=GlobalSetting)
def global_settings_edit(sender: GlobalSetting,
                        instance: GlobalSetting,
                        created, **kwargs):
    """
    Signal Make sure that there are no other objects
    that have field 'is_current' set to True.
    """
    # Check if a new settings object have True value:
    if instance.is_current == True:
        # Collect current global settings if they exist:
        collect_settings = sender.objects.filter(is_current=True)
        if collect_settings:
            for settings in collect_settings:
                if settings.pk != instance.pk:
                    settings.is_current = False
                    settings.save(update_fields=['is_current'])
    else:
        # Collect current global settings if they exist:
        collect_settings = sender.objects.filter(is_current=True)
        if not collect_settings:
            instance.is_current = True
            instance.save(update_fields=['is_current'])

@receiver(pre_delete, sender=GlobalSetting)
def global_settings_delete(instance: GlobalSetting, **kwargs):
    """
    Signal Make sure that there always is one object
    that have field 'is_current' set to True.
    """
    if instance.is_current == True:
        GlobalSetting.objects.create(
            name='Default', slug='default')
