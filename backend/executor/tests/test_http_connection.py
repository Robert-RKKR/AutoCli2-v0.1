# PyTest import:
import pytest

# Models import:
from management.models.global_settings import GlobalSetting


# @pytest.mark.django_db
# def test_global_settings_create():
#     # Create test global settings:
#     GlobalSetting.objects.create(name='Test')
#     # Collect test global settings:
#     global_settings = GlobalSetting.objects.get(pk=1)
#     # Check if test global settings where created:
#     assert global_settings.name == 'Test'

# @pytest.mark.django_db
# def test_global_settings_delete():
#     # Create test global settings:
#     GlobalSetting.objects.create(name='Test')
#     # Collect test global settings:
#     global_settings = GlobalSetting.objects.get(pk=1)
#     # Delete test global settings:
#     global_settings.delete()
#     # Check if default global settings where created:
#     default_global_settings = GlobalSetting.objects.get(name='Default')
#     # Check if default global settings where created:
#     assert default_global_settings.name == 'Default'

# @pytest.mark.django_db
# def test_global_settings_new():
#     # Create test-1 global settings:
#     GlobalSetting.objects.create(name='Test-1')
#     # Create test-2 global settings:
#     GlobalSetting.objects.create(name='Test-2')
#     # Collect test-1 global settings:
#     test_1 = GlobalSetting.objects.get(name='Test-1')
#     # Collect test-2 global settings:
#     test_2 = GlobalSetting.objects.get(name='Test-2')
#     # Collect test data:
#     test_data = [
#         test_1.is_current,
#         test_2.is_current]
#     # Check if default global settings where created:
#     assert test_data == [False, True]
