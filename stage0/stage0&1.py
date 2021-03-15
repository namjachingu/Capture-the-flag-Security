#!/usr/bin/env python

import requests
import json
import sys
from pathlib import Path
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from pprint import pprint

here = Path(__file__).parent.absolute()
repository_root = (here / ".." ).resolve()
sys.path.insert(0, str(repository_root))

import env

inv_url = env.UMBRELLA.get("inv_url")
inv_token = env.UMBRELLA.get("inv_token")
#Use a domain of your choice
domain = "internetbadguys.com"

#Construct the API request to the Umbrella Investigate API to query for the status of the domain
url = f"{inv_url}/domains/categorization/{domain}?showLabels"
headers =  {"Authorization": f'Bearer {inv_token}'}
response = requests.get(url, headers=headers)
response.raise_for_status()


'''
#Make sure the right data in the correct format is chosen, you can use print statements to debug your code
domain_status = response.json()[domain]["status"]

if domain_status == 1:
    print(f"The domain {domain} is found CLEAN")
elif domain_status == -1:
    print(f"The domain {domain} is found MALICIOUS")
elif domain_status == 0:
    print(f"The domain {domain} is found UNDEFINED")

print("This is how the response data from Umbrella Investigate looks like: \n")
pprint(response.json(), indent=4)
'''

#check the historical data
url = f"https://investigate.api.umbrella.com/pdns/domain/{domain}"
response = requests.get(url, headers=headers)
#pprint(response.json(), indent=4)

### STAGE1 ###
en_key = env.UMBRELLA.get("en_key")
url = f"https://s-platform.api.opendns.com/1.0/events?customerKey={en_key}"
headers = {'Content-Type': 'application/json'}

data = {
    'protocolVersion': ,
    'providerName': ,
    'deviceId': ,
    'deviceVersion': , 
    'eventTime': ,
    'alertTime': ,
    'dstDomain': domain,
    'dstUrl': , 
    }

if response.json()[domain]["status"] == -1:
    response = requests.post(url, data=json.dumps(data), headers=headers)
    print(response.json())
    
