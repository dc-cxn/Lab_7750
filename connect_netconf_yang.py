import ncclient, xmltodict, json, pprint
from ncclient import manager
from device_info import Lab_7750

import logging

#logging.basicConfig(
#    level=logging.DEBUG,
#)

conn = manager.connect(host=Lab_7750["address"], 
                           port=Lab_7750["port"],
                           username=Lab_7750["username"],
                           password=Lab_7750["password"],
                           hostkey_verify=False)
 
rtr = conn.server_capabilities
print(type(rtr))

print(rtr)

for x in conn.server_capabilities:
    if "router" in x:
        print(x)
#    print(x)

#schema = conn.get_schema("nokia-system")
#print(schema)

conn.close_session()