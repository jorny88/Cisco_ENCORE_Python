import requests
import sys

# Allow self sgined serts
requests.packages.urllib3.disable_warnings()

# Credentials - must be hidden in future
USER = 'developer'
PASS = 'C1sco12345'


payload = {}
headers = {'Content-Type': 'application/yang-data+json', 'Accept': 'application/yang-data+json'}

# Number of interfaces to delete
int_number = 2

for x in range(int_number):
    intname = 'Loopback123' + str(x)
    print('Deleting ' + intname)

# URL for GET requests
url = 'https://ios-xe-mgmt.cisco.com:9443/restconf/data/ietf-interfaces:interfaces/interface=' + intname

# SET yang+json as data formats

#Print (payload)
response = requests.request("Delete", url, auth=(USER, PASS), headers=headers, data=payload, verify=False)
print('Status Code:' + str(response.status_code))
print('Response Text:' + response.text)