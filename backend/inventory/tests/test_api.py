# Django - URL revers import
from django.urls import reverse

# AutoCli2 - base API test import:
from autocli2.base.tests.api_tests.base_api_test import BaseApiTest


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
            'code': 'TEST ST',
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

    # def test_api_create(self):
    #     # Collect responses:
    #     responses = []

    #     # Create test API credential object:
    #     response = self.client.post(
    #         self.credential, self.credential_data, format='json')
    #     # Add response status code to responses list:
    #     responses.append(response.status_code)
    #     # Create test API platform object:
    #     response = self.client.post(
    #         self.platform, self.platform_data, format='json')
    #     # Add response status code to responses list:
    #     responses.append(response.status_code)
    #     # Create test API region object:
    #     response = self.client.post(
    #         self.region, self.region_data, format='json')
    #     # Add response status code to responses list:
    #     responses.append(response.status_code)
    #     # Create test API site object:
    #     response = self.client.post(
    #         self.site, self.site_data, format='json')
    #     # Add response status code to responses list:
    #     responses.append(response.status_code)
    #     # Create test API host object:
    #     response = self.client.post(
    #         self.host, self.host_data, format='json')
    #     # Add response status code to responses list:
    #     responses.append(response.status_code)
 
    #     # Check responses status
    #     self.assertEqual(True, self.check_status_code_list(201, responses))

    # def test_api_list(self):
    #     # Collect responses:
    #     responses = []

    #     # Collect test api credential object:
    #     response = self.client.get(
    #         self.credential, params={'id': '1'}, format='json')
    #     # Add response status code to responses list:
    #     responses.append(response.status_code)
    #     # Collect test api platform object:
    #     response = self.client.get(
    #         self.platform, params={'id': '1'}, format='json')
    #     # Add response status code to responses list:
    #     responses.append(response.status_code)
    #     # Collect test api region object:
    #     response = self.client.get(
    #         self.region, params={'id': '1'}, format='json')
    #     # Add response status code to responses list:
    #     responses.append(response.status_code)
    #     # Collect test api site object:
    #     response = self.client.get(
    #         self.site, params={'id': '1'}, format='json')
    #     # Add response status code to responses list:
    #     responses.append(response.status_code)
    #     # Collect test api host object:
    #     response = self.client.get(
    #         self.host, params={'id': '1'}, format='json')
    #     # Add response status code to responses list:
    #     responses.append(response.status_code)
        
    #     # Check responses status
    #     self.assertEqual(True, self.check_status_code_list(200, responses))

    # def test_api_retrieve(self):
    #     # Collect responses:
    #     responses = []

    #     # Collect test api credential object:
    #     response = self.client.get(
    #         self.credential, format='json')
    #     # Add response status code to responses list:
    #     responses.append(response.status_code)
    #     # Collect test api platform object:
    #     response = self.client.get(
    #         self.platform, format='json')
    #     # Add response status code to responses list:
    #     responses.append(response.status_code)
    #     # Collect test api region object:
    #     response = self.client.get(
    #         self.region, format='json')
    #     # Add response status code to responses list:
    #     responses.append(response.status_code)
    #     # Collect test api site object:
    #     response = self.client.get(
    #         self.site, format='json')
    #     # Add response status code to responses list:
    #     responses.append(response.status_code)
    #     # Collect test api host object:
    #     response = self.client.get(
    #         self.host, format='json')
    #     # Add response status code to responses list:
    #     responses.append(response.status_code)
        
    #     # Check responses status
    #     self.assertEqual(True, self.check_status_code_list(200, responses))

    def test_api_update(self):
        # Collect responses:
        responses = []

        # Create
        create = self.client.post(
            self.credential, self.credential_data, format='json')
        
        get_all = self.client.get(
            self.credential, format='json')

        # prepare test api data for PUt method:
        self.credential_data['name'] = 'A new test credential'
        # Collect test api credential object:
        edit = self.client.put(self.credential + '1/', self.credential_data, format='json')
        
        get_one = self.client.get(
            self.credential, params={'id': '1'}, format='json')

        
        print('======> ', create.status_code, get_all.content, edit.status_code, get_one.content)
        # Add response status code to responses list:
        responses.append(301)
        
        
        # # Collect test api platform object:
        # response = self.client.get(
        #     self.platform, format='json')
        # # Add response status code to responses list:
        # responses.append(response.status_code)
        # # Collect test api region object:
        # response = self.client.get(
        #     self.region, format='json')
        # # Add response status code to responses list:
        # responses.append(response.status_code)
        # # Collect test api site object:
        # response = self.client.get(
        #     self.site, format='json')
        # # Add response status code to responses list:
        # responses.append(response.status_code)
        # # Collect test api host object:
        # response = self.client.get(
        #     self.host, format='json')
        # # Add response status code to responses list:
        # responses.append(response.status_code)
        
        # Check responses status
        self.assertEqual(True, self.check_status_code_list(200, responses))
