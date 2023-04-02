# Django - URL revers import
from django.urls import reverse

# AutoCli2 - base API test import:
from autocli2.base.tests.base_api_test import BaseApiTest


# Test classes:
class NotificationApiTest(BaseApiTest):

    def setUp(self) -> None:
        # Collect test URLs:
        self.change_log = reverse('api-inventory:change-log-list')
        self.notification = reverse('api-inventory:notification-list')
        # Inherit from base method:
        return super().setUp()
    
    def tearDown(self) -> None:
        # Inherit from base method:
        return super().tearDown()


class TestInventoryApi(NotificationApiTest):

    pass

    # def test_inventory_api(self):
    #     # Collect responses:
    #     responses = []
    #     # Run API tests:
        
    #     # Check responses status
    #     self.assertEqual(True,
    #         self.check_status_code_list(True, responses))
