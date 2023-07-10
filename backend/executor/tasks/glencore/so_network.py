# Python - IP address import:
import ipaddress

# Celery - application import:
from autocli2.celery import app

# AutoCli2 - base task import:
from autocli2.base.tasks.base_task import BaseTask

# AutoCli2 - executor import:
from executor.models.executor import Executor

# AutoCli2 - inventory import:
from inventory.models.host import Host

# AutoCli2 - HTTP/S connection import:
from executor.connections.http_connection import Connection


@app.task(bind=True, name='execute_executor_task', base=BaseTask)
def sentinelone_network_task(self):
    # Init task:
    self.init_task()
    # Collected data:
    collected_networks = []
    collected_prefixes = {}
    output_wrong = ''
    output = ''
    # Base script data:
    REGION_IDS = {
        'Europe': '1015682288865796819',
        # 'Australia': '1015682200751858224'
    }
    # Collect or create sentinel one / netbox device:
    sentinelone = Host.objects.get(pk=1)
    netbox = Host.objects.get(pk=2)

    # Collect networks:
    for region in REGION_IDS:
        # Collect region ID:
        region_id = REGION_IDS[region]
        # Connect to sentinel one device:
        with Connection(sentinelone) as con:
            networks = con.get('web/api/v2.1/ranger/gateways',
                {'limit':'1000', 'accountIds': region_id})
        # Check response:
        if isinstance(networks, list):
            for network in networks:
                # Collect ip:
                ip = network['ip']
                # Convert ip:
                network['convert_ip'] = ipaddress.ip_address(ip)
            # Add networks to all collected networks:
            collected_networks = collected_networks + networks

    # Collect prefixes:
    with Connection(netbox) as con:
        prefixes = con.get('api/ipam/prefixes/',
            {'limit':'1000'})
    # Check response:
    if isinstance(prefixes, list):
        for prefix in prefixes:
            # Collect network:
            network = prefix['prefix']
            # Convert network:
            convert_network = ipaddress.ip_network(network)
            prefix['convert_network'] = convert_network
            # Add networks to all collected networks:
            collected_prefixes[convert_network] = prefix

    # corelate collected data:
    for collected_network in collected_networks:
        # Collect IP:
        ip = collected_network['convert_ip']
        # Find best prefix:
        best_prefix = None
        for prefix in collected_prefixes:
            convert_network = collected_prefixes[prefix]['convert_network']
            if ip in convert_network:
                if best_prefix is None or convert_network.prefixlen > best_prefix.prefixlen:
                    best_prefix = convert_network
        try:
            temp = collected_prefixes[best_prefix]['custom_fields']['zone']
            parts = temp.split("_")
            best_netwokr_role = " ".join(parts[1:]).capitalize()
            output = output + f'IP: {ip} belongs to network {best_prefix} ({best_netwokr_role})\n'
            # Update SentinelOne:
            network_id = collected_network['id']
            url = f'web/api/v2.1/ranger/gateways/{network_id}'
            body = {
                "data": {
                    "networkName": best_netwokr_role
                }
            }
            with Connection(sentinelone) as con:
                networks = con.put(url, body=body)
        except:
            try:
                best_netwokr_role = collected_prefixes[best_prefix]['site']['display']
                output_wrong = output_wrong + f'IP: {ip} belongs to network {best_prefix} ({best_netwokr_role})\n'
            except:
                best_netwokr_role = False
                output_wrong = output_wrong + f'IP: {ip} belongs to network {best_prefix} ({best_netwokr_role})\n'
