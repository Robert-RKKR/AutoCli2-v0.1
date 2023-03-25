# Python - Json import:
import json

# Rest framework - test case import:
from rest_framework.test import APITestCase

# Rest framework - token import:
from rest_framework.authtoken.models import Token

# AutoCli2 - management model import:
from management.models.administrator import Administrator


# Base API test class:
class BaseApiTest(APITestCase):

    def setUp(self) -> None:
        
        # Create a user for testing:
        self.user = Administrator.objects.create_superuser(
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
            self, data: dict, response: dict, action: str, url):
        """
        Compare data provided to create a new object via API with API response.
        """

        try: # Try to convert response JSON output into dictionary:
            response = json.loads(response.content)
        except Exception as error:
            return 'The response provided is not formatted as valid '\
                f'JSON.\nError: {error}'
        else:
            # Prepare response page results data:
            if response.get('page_results', False):
                response = response['page_results']
            # Collect only the first item if a list has been provided:
            if isinstance(response, list):
                response = response[0]
            # Compare two dictionary's:
            for key, value in list(data.items()):
                if key in response:
                    if response[key] != data[key]:
                        # Print error message:
                        print(f"===> {url} output key: '{key}' value: "\
                            f"'{response[key]}' doesn't match provided "\
                            f"data value '{value}' Action: {action}")
                        # Return False value:
                        return False
                else:
                    # Print error message:
                    print(f"===> {url} output key: '{key}' doesn't belongs "\
                        "to data dictionary")
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
        # Return True value if not interrupted:
        return True
    
    def api_simple_test_list(
            self, simple_url: str, data: dict or bool = False) -> bool:
        """
        Simple API test - list GET method:
        """

        # List test API objects:
        response = self.client.get(simple_url, format='json')
        if data: # Check if data where provided:
            # Compare response to provided data:
            if not self._compare_data_with_response(
                data, response, 'List', simple_url):
                # Return False value:
                return False
        else:
            # Collect return code:
            code = response.status_code 
            if code != 200: # Check return code:
                # Print message:
                print(f'===> List API action ({simple_url}), return code {code} '\
                      f'instead 200.\nResponse: {response.content}')
                # Return False value:
                return False
        # Return True value if not interrupted:
        return True
    
    def api_simple_test_update(
            self, url: str, changes: dict) -> bool:
        """
        Simple API test - update PUT method:
        """

        # Update test API object:
        response = self.client.put(f'{url}1/', changes, format='json')
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
            self, simple_url: str, changes: dict or bool = False) -> bool:
        """
        Simple API test - retrieve GET method:
        """

        # Retrieve test API object:
        response = self.client.get(f'{simple_url}1/', format='json')
        if changes: # Check if changes where provided:
            # Compare response:
            if not self._compare_data_with_response(
                changes, response, 'Retrieve', simple_url):
                # Return False value:
                return False
        else:
            # Collect return code:
            code = response.status_code 
            if code != 200: # Check return code:
                # Print message:
                print(f'===> Retrieve API action ({simple_url}), return code {code} '\
                      f'instead 200.\nResponse: {response.content}')
                # Return False value:
                return False
        # Return True value if not interrupted:
        return True

    def api_simple_test(self, url, simple_url, data, changes) -> bool:
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
        responses.append(self.api_simple_test_create(
            url, data))
        # Run list API test using GET method:
        responses.append(self.api_simple_test_list(
            simple_url, data))
        # Run update API test using PUT method:
        responses.append(self.api_simple_test_update(
            url, changes))
        # Run retrieve API test using GET method:
        responses.append(self.api_simple_test_retrieve(
            simple_url, changes))
        
        # Check responses:
        if responses == [True, True, True, True]:
            return True
        else:
            return False
