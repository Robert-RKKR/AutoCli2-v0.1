# PyTest - test import:
import pytest

# Project executor models import:
from connector.models.connection_template import ConnectionTemplate

# Test functions:
@pytest.mark.django_db
def test_regex_validation(create_test_connection_template_with_regex):
    # Collect test objects:
    collected_objects = ConnectionTemplate.objects.all()
    # Collect response:
    response = False
    # Iterate thru collected objects:
    for collected_object in collected_objects:
        if collected_object.name == 'Regex test template 1':
            response = True
        if collected_object.name == 'Regex test template 2':
            try:
                collected_object.full_clean()
            except:
                response = True
            else:
                response = False
    # Check result:
    assert response == True
