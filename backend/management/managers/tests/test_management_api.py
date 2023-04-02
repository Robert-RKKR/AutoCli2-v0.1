# Django - URL revers import
from django.urls import reverse

# AutoCli2 - base API test import:
from autocli2.base.tests.base_api_test import BaseApiTest


# Test classes:
class ManagementApiTest(BaseApiTest):

    def setUp(self) -> None:
        # Collect test URLs:
        self.global_settings = reverse('api-inventory:credential-list')
        # Collect test data:
        self.global_settings_data = {
            'name': 'Test global settings'
        }
        # Inherit from base method:
        return super().setUp()
    
    def tearDown(self) -> None:
        # Inherit from base method:
        return super().tearDown()


class TestInventoryApi(ManagementApiTest):

    def test_inventory_api(self):
        # Collect responses:
        responses = []
        # Run API tests:
        responses.append(self.api_simple_test(
            self.global_settings, self.global_settings_data,
            {'name':'A new test global settings'}))
        # Check responses status
        self.assertEqual(True,
            self.check_status_code_list(True, responses))
