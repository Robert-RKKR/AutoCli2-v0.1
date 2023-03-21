# Django - URL revers import
from django.urls import reverse

# AutoCli2 - base API test import:
from autocli2.base.tests.base_api_test import BaseApiTest


# Test classes:
class InventoryApiTest(BaseApiTest):

    def setUp(self) -> None:
        # Collect test URLs:
        self.simple_credential = reverse('api-inventory:simple_credential-list')
        self.simple_platform = reverse('api-inventory:simple_platform-list')
        self.simple_region = reverse('api-inventory:simple_region-list')
        self.simple_host = reverse('api-inventory:simple_host-list')
        self.simple_site = reverse('api-inventory:simple_site-list')
        self.credential = reverse('api-inventory:credential-list')
        self.platform = reverse('api-inventory:platform-list')
        self.region = reverse('api-inventory:region-list')
        self.host = reverse('api-inventory:host-list')
        self.site = reverse('api-inventory:site-list')
        # Collect test data:
        self.credential_data = {
            'name': 'Test credential',
            'username': 'admin',
            'password': 'password',
        }
        self.platform_data = {
            'name': 'Test platform',
        }
        self.region_data = {
            'name': 'Test region',
            'code': 'TEST',
        }
        self.site_data = {
            'name': 'Test site',
            'code': 'ST',
            'region': 1,
        }
        self.host_data = {
            'name': 'Test host',
            'hostname': '1.1.1.1',
            'site': 1,
            'platform': 1,
            'credential': 1,
        }
        # Inherit from base method:
        return super().setUp()
    
    def tearDown(self) -> None:
        # Inherit from base method:
        return super().tearDown()


class TestInventoryApi(InventoryApiTest):

    def test_api_update(self):
        # Collect responses:
        responses = []
        # Run API tests:
        responses.append(self.api_simple_test(
            self.credential, self.credential_data, {'name':'A new test credential'}))
        responses.append(self.api_simple_test(
            self.platform, self.platform_data, {'name':'A new test platform'}))
        responses.append(self.api_simple_test(
            self.region, self.region_data, {'name':'A new test region'}))
        responses.append(self.api_simple_test(
            self.site, self.site_data, {'name':'A new test site'}))
        responses.append(self.api_simple_test(
            self.host, self.host_data, {'name':'A new test host'}))
        # Check responses status
        self.assertEqual(True, self.check_status_code_list(True, responses))
