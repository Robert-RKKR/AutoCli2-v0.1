# PyTest import:
import pytest

# Models import:
from management.models.global_settings import GlobalSetting

# Test functions:
@pytest.mark.django_db
def test_global_settings_create(create_global_settings):
    # Collect test global settings:
    global_settings = GlobalSetting.objects.get(pk=1)
    # Check if test global settings where created:
    assert global_settings.name == 'Test-1'

@pytest.mark.django_db
def test_global_settings_delete(create_global_settings):
    # Collect test global settings:
    global_settings = GlobalSetting.objects.all()
    # Delete test global settings:
    global_settings.delete()
    # Check if default global settings where created:
    default_global_settings = GlobalSetting.objects.get(name='Default')
    # Check if default global settings where created:
    assert default_global_settings.name == 'Default'

@pytest.mark.django_db
def test_global_settings_new(create_global_settings):
    # Collect test global settings:
    test_1 = GlobalSetting.objects.get(pk=1)
    test_2 = GlobalSetting.objects.get(pk=2)
    # Collect global settings is_current values:
    test_data = [
       test_1.is_current,
        test_2.is_current]
    # Check if default global settings where created:
    assert test_data == [False, True]
