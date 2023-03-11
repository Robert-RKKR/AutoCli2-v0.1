# PyTest import:
import pytest

# Project inventory models import:
from inventory.models.credentials import Credential
from inventory.models.platform import Platform
from inventory.models.region import Region
from inventory.models.host import Host
from inventory.models.site import Site

# Project executor models import:
from connector.models.connection_template import ConnectionTemplate

# Project executor models import:
from executor.models.executor import Executor

# Test functions:
@pytest.mark.django_db
def test_created_objects(create_test_objects):
    # Collect test objects:
    test_template = ConnectionTemplate.objects.get(pk=1)
    test_credentials = Credential.objects.get(pk=1)
    test_executor = Executor.objects.get(pk=1)
    test_platform = Platform.objects.get(pk=1)
    test_region = Region.objects.get(pk=1)
    test_host = Host.objects.get(pk=1)
    test_site = Site.objects.get(pk=1)
    # Check if test global settings where created:
    assert test_executor.name == 'Test executor'
