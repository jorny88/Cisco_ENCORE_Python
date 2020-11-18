import requests
import sys

# Allow self sgined serts
requests.packages.urllib3.disable_warnings()

# Credentials - must be hidden in future
USER = 'developer'
PASS = 'C1sco12345'

# URL for GET requests
url = 'https://ios-xe-mgmt.cisco.com:9443/restconf/data/ietf-interfaces:interfaces'

# SET yang+json as data formats
headers = {'Content-Type': 'application/yang-data+json',
           'Accept': 'application/yang-data+json'}

# Number of interfaces to create
int_number = 10

for x in range(int_number):
    ipaddr = '9.9.9.' + str(x)
    print('Creating loopback :' + ipaddr)

payload = '\
{\
    "ietf-interfaces:interface": {\
        "name": "Loopback123' + str(x) + '",\
        "description": "Added with RESTConf - Jorny",\
        "type": "iana-if-type:softwareLoopback",\
        "enabled": true,\
        "ietf-ip:ipv4": {\
            "address": [\
                {\
                    "ip": "9.9.9.' + str(x) + '",\
                    "netmask": "255.255.255.255"\
                }\
            ]\
        }\
    }\
}'

    #Print (payload)
response = requests.request("POST", url, auth=(USER, PASS), headers=headers, data=payload, verify=False)
print('Status Code:' + str(response.status_code))
print('Response Text:' + response.text)