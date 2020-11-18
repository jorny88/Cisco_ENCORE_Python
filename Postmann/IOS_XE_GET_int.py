import requests 
import sys

# Allow self sgined serts
requests.packages.urllib3.disable_warnings()

#Credentials - must be hidden in future
USER = 'developer'
PASS = 'C1sco12345'

# URL for GET requests
url = "https://ios-xe-mgmt.cisco.com:9443/restconf/data/ietf-interfaces:interfaces"

# SET yang+json as data formats
headers = {'Content-Type': 'application/yang-data+json',
            'Accept': 'application/yang-data+json'}

# Run GET
response = requests.get(url, auth=(USER, PASS), headers=headers, verify=False)


print(response.text)
