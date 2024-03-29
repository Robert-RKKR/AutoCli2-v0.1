# PyTest - test import:
import pytest

# AutoCli2 - HTTP Connection class import:
from executor.connections.http_connection import Connection

# AutoCli2 - inventory model import:
from inventory.models.host import Host

# Test functions:
@pytest.mark.django_db
def test_http_connection(create_test_objects):
    # Collect test objects:
    test_host_2 = Host.objects.get(pk=2)
    # Create test HTTP connection:
    con = Connection(test_host_2)
    con.start_connection()
    # Sent GET request to test host:
    response = con.get('BikePoint')
    # Collect connection data:
    connection_data = [
        isinstance(response, list),
        con.json_response_status,
        con.response_status]
    # Check result:
    assert connection_data == [True, True, True]
