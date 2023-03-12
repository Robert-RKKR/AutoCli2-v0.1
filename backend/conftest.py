# PyTest import:
import pytest

# Project management models import:
from management.models.global_settings import GlobalSetting

# Project inventory models import:
from inventory.models.credentials import Credential
from inventory.models.platform import Platform
from inventory.models.region import Region
from inventory.models.site import Site
from inventory.models.host import Host

# Project executor models import:
from connector.models.connection_template import ConnectionTemplate

# Project executor models import:
from executor.models.executor import Executor

# Model data:
api_default_header = {
    'Accept': 'application/yang-data+json',
    'Content-Type': 'application/yang-data+json'}
test_url = 'restconf/data/Cisco-IOS-XE-environment-oper:environment-sensors'

# Fixture functions:
@pytest.fixture()
def create_global_settings(db):
    # Create test-1 global settings:
    test_1 = GlobalSetting.objects.create(name='Test-1')
    # Create test-2 global settings:
    test_2 = GlobalSetting.objects.create(name='Test-2')

@pytest.fixture()
def create_test_objects(db):
    # Create test region:
    test_region = Region.objects.create(
        name='Test region',
        code='TR')
    # Create test site:
    test_site= Site.objects.create(
        name='Test site',
        code='TSS',
        region=test_region)
    # Create test platform:
    test_platform = Platform.objects.create(
        name='Test platform',
        api_default_header=api_default_header)
    # Create test credential:
    test_credential = Credential.objects.create(
        name='Test credential',
        username='developer',
        password='C1sco12345')
    # Create test hosts:
    test_host_1 = Host.objects.create(
        name='Test HTTP host Cisco online',
        hostname='sandbox-iosxe-latest-1.cisco.com',
        data_collection_protocol=2,
        site=test_site,
        platform=test_platform,
        credential=test_credential,
        certificate_check=False)
    test_host_2 = Host.objects.create(
        name='Test HTTP host London underground',
        hostname='api.tfl.gov.uk',
        data_collection_protocol=2,
        site=test_site,
        platform=test_platform,
        credential=test_credential)
    # Create test template:
    test_template = ConnectionTemplate.objects.create(
        name='Test template',
        execution_protocol=2,
        http_url=test_url)
    test_template.platforms.add(test_platform)
    # Create test executor:
    test_executor = Executor.objects.create(
        name='Test executor',
        executor_type=2)
    test_executor.hosts.add(test_host_1)
    test_executor.connection_templates.add(test_template)
