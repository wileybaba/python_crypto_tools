#! python3
# gemini_price_pull.py - Prints last Gemini bitcoin and ether trade from command line

import requests, pprint, json, certifi, urllib3

# http = urllib3.PoolManager(
#         cert_reqs='CERT_REQUIRED',
#         ca_certs=certifi.where())

base_url = "https://api.gemini.com/v1"

# Bitcoin price pull
response = requests.get(base_url + "/pubticker/btcusd", verify=False)
assert response.status_code == 200
parsed_response_content = json.loads(response.content)
print('@Gemini:  Bitcoin = $' + parsed_response_content['last'] )

# Ether price pull
response = requests.get(base_url + "/pubticker/ethusd", verify=False)
assert response.status_code == 200
parsed_response_content = json.loads(response.content)
print('@Gemini:  Ether = $' + parsed_response_content['last'] )
