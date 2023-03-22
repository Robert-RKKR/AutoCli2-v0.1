# Python - Json import:
import json

# Rest framework - test case import:
from rest_framework.test import APITestCase

# Rest framework - token import:
from rest_framework.authtoken.models import Token

# Django - user model import:
from django.contrib.auth.models import User


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
    
    def compare_output(self, data: dict, output: dict, action: str, url):
        """ Compare two dictionary's, """
        # Prepare output data:
        if output.get('page_results', False):
            output = output['page_results']
        # Change output if it's a list:
        if isinstance(output, list):
            output = output[0]
        # Compare two dictionary's:
        for key in data:
            if key in output:
                if output[key] != data[key]:
                    error = f"===> {url} output key: '{key}' value: "\
                        f"'{output[key]}' doesn't match provided "\
                        f"data value '{data[key]}' Action: {action}"
                    return error
            else:
                error = f"===> {url} output key: '{key}' doesn't belongs "\
                    "to data dictionary"
                return error
        return True
    
    def api_simple_test(self, url, simple_url, data, changes):
        # Create test API object:
        create_api = self.client.post(url, data, format='json')
        # Collect return code:
        code = create_api.status_code 
        if code != 201: # Check return code:
            # Print message:
            print(f'===> Create API action ({url}), return code {code} instead '\
                f'201.\nResponse: {create_api.content}')
            # Return False value:
            return False
        
        # List test API objects:
        list_api = self.client.get(simple_url, format='json')
        # Collect response output:
        list_output = json.loads(list_api.content)
        # Compare output:
        response = self.compare_output(data, list_output, 'List', url)
        if response is not True:
            # Print message:
            print(response)
            # Return False value:
            return False
        
        # Update test API object:
        update_api = self.client.put(f'{url}1/', changes, format='json')
        # Collect return code:
        code = update_api.status_code 
        if code != 200: # Check return code:
            # Print message:
            print(f'===> Update API action ({url}), return code {code} instead '\
                f'200.\nResponse: {update_api.content}')
            # Return False value:
            return False
        
        # Retrieve test API object:
        retrieve_api = self.client.get(f'{simple_url}1/', format='json')
        # Collect response output:
        retrieve_output = json.loads(retrieve_api.content)
        # Compare output:
        response = self.compare_output(changes, retrieve_output, 'Retrieve', url)
        if response is not True:
            # Print message:
            print(response)
            # Return False value:
            return False
        
        # Return True value if not interrupted:
        return True
