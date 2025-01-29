import ncclient, xmltodict, json, pprint
from xml.etree import ElementTree
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

#for x in conn.server_capabilities:
#    if "port" in x:
#        print(x)
#    print(x)

schema = conn.get_schema("nokia-types-port")
print(schema)

#result = conn.get_config('running')
#print(result.xml)

#interfacefilter = """
#<filter>
#    <configure xmlns="urn:nokia.com:sros:ns:yang:sr:conf">
#        <router>
#
#        </router>
#    </configure>
#</filter>
#"""

portfilter = """
<filter>
    <configure xmlns="urn:nokia.com:sros:ns:yang:sr:conf">
        <port>

        </port>
    </configure>
</filter>
"""

#result = conn.get_config('running', filter=interfacefilter)

#print(result.xml)

result = conn.get_config('running', filter=portfilter)

config = xmltodict.parse(result.xml)["rpc-reply"]["data"]
jsonconfig = json.dumps(config, indent=4)

print(jsonconfig)

conn.close_session()