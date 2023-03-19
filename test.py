# Python - libraries import:
import requests

SENTINELONE_HEADER = {
    'Authorization': 'APIToken 5k2S4IdFgHAYyhwndqolBcXZihkKRqdh5IsZ9Rfr3WSVFQVQd7rACd83G3odEPPsoDZlFJwUoiPEgHAH',
    'Content-Type': 'application/json'}

session = requests.Session()
request = requests.Request(
    'GET',
    'https://glencore.sentinelone.net')
prepare_request = session.prepare_request(request)
response = session.send(
    prepare_request,
    verify=False)

print(response.status_code)
