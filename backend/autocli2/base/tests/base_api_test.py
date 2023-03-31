# Python - Json import:
import json

# Django - user model import:
from django.contrib.auth.models import User

# Rest framework - test case import:
from rest_framework.test import APITestCase

# Rest framework - token import:
from rest_framework.authtoken.models import Token

# Constance:
RESPONSE_DATA = 'page_results'


# Base API test class:
class BaseApiTest(APITestCase):

    def setUp(self) -> None:
        
        # Create a user for testing:
        self.user = User.objects.create_superuser(
            'testuser', 'test@example.com', 'password')
        # Create an authentication token for the user
        self.token = Token.objects.create(user=self.user)
        # Authenticate the user by token:
        self.client.credentials(
            HTTP_AUTHORIZATION='Token ' + self.token.key)
        # Inherit from base method:
        return super().setUp()
    
    def tearDown(self) -> None:
        # Inherit from base method:
        return super().tearDown()
    
    def check_status_code_list(self,
            expected_status_code: int, status_code_list: list[int]):
        
        # Return bool value:
        status = False
        # Iterate thru all status codes:
        for status_code in status_code_list:
            # Check status code:
            if expected_status_code == status_code:
                status = True
            else:
                status = False
        # Return status:
        return status
    
    def _compare_data_with_response(
            self, data: dict, response: dict, action: str, url: str):
        """
        Compare data provided to create a new object via API with API response.
        """

        # Compare two dictionary's:
        for key, value in list(data.items()):
            if key in response:
                if response[key] != data[key]:
                    # Print error message:
                    print(f"===> {action}:{url} output key: '{key}' "\
                        f"value: '{response[key]}' doesn't match "\
                        f"provided data value '{value}'")
                    # Return False value:
                    return False
            else:
                # Print error message:
                print(f"===> {action}:{url} output key: '{key}' "
                    "doesn't belongs to data dictionary")
                # Return False value:
                return False
        # Return True value if not interrupted:
        return True
    
    def api_simple_test_create(
            self, url: str, data: dict) -> bool:
        """
        Simple API test - create POST method:
        """

        # Create test API object:
        response = self.client.post(url, data, format='json')
        # Collect return code:
        response_code = response.status_code 
        if response_code != 201: # Check return code:
            # Print message:
            print(f'===> Create API action ({url}), return code {response_code} '
                f'instead 201.\nResponse: {response.content}')
            # Return False value:
            return False
        # Collect response data:
        response_data = response.json().get(RESPONSE_DATA, False)
        if response_data:
            # Return PK value if not interrupted:
            return response_data.get('pk', False)
        else:
            # Return False if response data are not available:
            return False
    
    def api_simple_test_list(
            self, url: str, pk: int, data: dict or bool = False) -> bool:
        """
        Simple API test - list GET method:
        """

        # List test API objects:
        response = self.client.get(url, format='json')
        if data: # Check if data where provided:
            # Collect response data:
            object_list = response.json().get(RESPONSE_DATA, False)
            # Check if collected dat are valid:
            if object_list:
                # Iterate thru collected data:
                collected_object = False
                for received_object in object_list:
                    # Collect proper object:
                    if received_object.get('pk', False) == pk:
                        collected_object = received_object
                        break
            if collected_object:
                # Compare response to provided data:
                if not self._compare_data_with_response(
                    data, collected_object, 'List', url):
                    # Return False value:
                    return False
            else:
                # Return False object with provided PK doesn't exist:
                return False
        else:
            # Collect return code:
            code = response.status_code 
            if code != 200: # Check return code:
                # Print message:
                print(f'===> List API action ({url}), return code {code} '\
                      f'instead 200.\nResponse: {response.content}')
                # Return False value:
                return False
        # Return True value if not interrupted:
        return True
    
    def api_simple_test_update(
            self, url: str, pk: int, changes: dict) -> bool:
        """
        Simple API test - update PUT method:
        """

        # Update test API object:
        response = self.client.put(f'{url}{pk}/', changes, format='json')
        # Collect return code:
        code = response.status_code 
        if code != 200: # Check return code:
            # Print message:
            print(f'===> Update API action ({url}), return code {code} instead '\
                f'200.\nResponse: {response.content}')
            # Return False value:
            return False
        # Return True value if not interrupted:
        return True
    
    def api_simple_test_retrieve(
            self, url: str, pk: int, changes: dict or bool = False) -> bool:
        """
        Simple API test - retrieve GET method:
        """

        # Retrieve test API object:
        response = self.client.get(f'{url}{pk}/', format='json')
        response_data = response.json().get(RESPONSE_DATA, False)
        if changes and response_data: # Check if changes where provided:
            # Compare response:
            if not self._compare_data_with_response(
                changes, response_data, 'Retrieve', url):
                # Return False value:
                return False
        else:
            # Collect return code:
            code = response.status_code 
            if code != 200: # Check return code:
                # Print message:
                print(f'===> Retrieve API action ({url}), return code {code} '\
                      f'instead 200.\nResponse: {response.content}')
                # Return False value:
                return False
        # Return True value if not interrupted:
        return True
    
    def api_simple_test_delete(
            self, url: str, pk: int) -> bool:
        """
        Simple API test - delete GET method:
        """

        # Delete test API object:
        response = self.client.delete(f'{url}{pk}/')
        # Collect return code:
        code = response.status_code 
        if code != 204: # Check return code:
            # Print message:
            print(f'===> Retrieve API action ({url}), return code {code} '\
                f'instead 204.\nResponse: {response.content}')
            # Return False value:
            return False
        # Return True value if not interrupted:
        return True

    def api_simple_test(self, url, data, changes) -> bool:
        """
        Simple API test wil run four API task in specific order:
            - Create API test using POST method.
            - List API test using GET method.
            - Update API test using PUT method.
            - Retrieve API test using GET method.
        """

        # Collect responses:
        responses = []
        
        # Run create API test using POST method:
        pk = self.api_simple_test_create(
            url, data)
        if isinstance(pk, int):
            responses.append(True)
        # Run list API test using GET method:
        responses.append(self.api_simple_test_list(
            url, pk, data))
        # Run update API test using PUT method:
        responses.append(self.api_simple_test_update(
            url, pk, changes))
        # Run retrieve API test using GET method:
        responses.append(self.api_simple_test_retrieve(
            url, pk, changes))
        
        # Run create API test using POST method to check delete:
        delete_pk = self.api_simple_test_create(
            url, data)
        if isinstance(pk, int):
            # Run delete API test using DELETE method:
            responses.append(self.api_simple_test_delete(
                url, delete_pk))
        else:
            responses.append(False)
        
        # Check responses:
        if responses == [True, True, True, True, True]:
            return True
        else:
            return False
