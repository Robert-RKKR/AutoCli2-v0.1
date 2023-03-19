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
