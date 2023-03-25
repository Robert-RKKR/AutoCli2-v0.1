# PyTest - test import:
import pytest

# AutoCli2 - inventory model import:
from inventory.models.credentials import Credential
from inventory.models.platform import Platform
from inventory.models.region import Region
from inventory.models.host import Host
from inventory.models.site import Site

# AutoCli2 - connector model import:
from connector.models.connection_template import ConnectionTemplate

# AutoCli2 - executor model import:
from executor.models.executor import Executor

# AutoCli2 - executor task import:
from executor.tasks.execute_executor import execute_executor_task

# Test functions:
@pytest.mark.django_db
def test_executor(create_test_objects):
    # Collect test objects:
    test_template = ConnectionTemplate.objects.get(pk=1)
    test_credentials = Credential.objects.get(pk=1)
    test_executor = Executor.objects.get(pk=1)
    test_platform = Platform.objects.get(pk=1)
    test_region = Region.objects.get(pk=1)
    test_host = Host.objects.get(pk=1)
    test_site = Site.objects.get(pk=1)
    # Test task 'execute_executor_task':
    task = execute_executor_task(1)
    assert task == {'Test HTTP host Cisco online': False}
