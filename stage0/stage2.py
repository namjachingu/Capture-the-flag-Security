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

#amp_host = env.AMP.get("Demo_AMP_Threat_Audit")
amp_host = env.AMP.get("host")
amp_client_id = env.AMP.get("client_id")
amp_api_key = env.AMP.get("api_key")

resp_amp = requests.get(f"https://{amp_client_id}:{amp_api_key}@{amp_host}/v1/event_types")
#resp_amp = requests.get(f"https://{amp_client_id}:{amp_api_key}@{amp_host}/v1/events")
#print(resp_amp.json())
'''
#for org in resp_amp.json()["metadata"]["results"]:
for org in resp_amp.json()["data"]:
    if org["name"] == "Executed malware":
        print(org["id"])
        print(org["description"])
        x = org["id"]
'''
resp_amp = requests.get(f"https://{amp_client_id}:{amp_api_key}@{amp_host}/v1/events")
print(resp_amp.json())

for org in resp_amp.json()["data"]:
    print(org)
    if org["hostname"] == "Demo_AMP_Threat_Audit":
        print(org["hostname"])




#url = "https://api.amp.cisco.com/v1/events?limit=2"
#url = resp_amp
#headers =  {"Content-Type": "application/json", "accept": "application/json"}
#response = requests.get(url, headers=headers)
#print(response.json())

