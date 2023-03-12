# PyTest import:
import pytest

# Project inventory models import:
from executor.connections.http_connection import Connection

# Project inventory models import:
from inventory.models.host import Host

# Test functions:
@pytest.mark.django_db
def test_created_objects(create_test_objects):
    # Collect test objects:
    test_host_2 = Host.objects.get(pk=2)
    # Create test HTTP connection:
    con = Connection(test_host_2)
    # Sent GET request to test host:
    response = con.get('BikePoint')
    # Collect connection data:
    connection_data = [
        isinstance(response, list),
        con.json_status,
        con.status]
    # Check result:
    assert connection_data == [True, True, True]
