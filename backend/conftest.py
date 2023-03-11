# PyTest import:
import pytest

# Models import:
from management.models.global_settings import GlobalSetting

@pytest.fixture()
def create_global_settings(db):
    print('RKKR')
    # Create test-1 global settings:
    test_1 = GlobalSetting.objects.create(name='Test-1')
    # Create test-2 global settings:
    test_2 = GlobalSetting.objects.create(name='Test-2')
    # Return created tests global settings:
    return (test_1, test_2)