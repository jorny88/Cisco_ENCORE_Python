import requests 
import sys

# Allow self sgined serts
requests.packages.urllib3.disable_warnings()

#Credentials - must be hidden in future
USER = 'developer'
PASS = 'C1sco12345'

# URL for GET requests
url = "https://ios-xe-mgmt.cisco.com:9443/restconf/data/ietf-interfaces:interfaces"

#JSON Payload
payload = '\
{\
    "ietf-interfaces:interface": {\
        "name": "Loopback999",\
        "description": "Added with RESTCONF",\
        "type": "iana-if-type:softwareLoopback",\
        "enabled": true,\
        "ietf-ip:ipv4": {\
            "address":[\
                {\
                    "ip": "9.9.9.90",\
                    "netmask": "255.255.255.255"\
                    }\
                ]\
            }\
        }\
    }'


# SET yang+json as data formats
headers = {'Content-Type': 'application/yang-data+json',
            'Accept': 'application/yang-data+json'}

#Run POST 
response = requests.request('POST',url, auth=(USER, PASS), headers=headers, data=payload, verify=False)


#Print results
print('Status Code:' + str(response.status_code))
print('Response Text:' + response.text)