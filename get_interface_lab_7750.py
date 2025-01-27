from device_info import Lab_7750
from ncclient import manager
import xmltodict
import logging
import json

#logging.basicConfig(
#    level=logging.DEBUG,
#)

netconf_filter = open("filter-ietf-interfaces.xml").read()

if __name__ == '__main__':
    with manager.connect(host=Lab_7750["address"], 
                        port=Lab_7750["port"],
                        username=Lab_7750["username"],
                        password=Lab_7750["password"],
                        hostkey_verify=False) as m:
        
        netconf_reply = m.get(netconf_filter)

        intf_details = xmltodict.parse(netconf_reply.xml)["rpc-reply"]["data"]
        jsonconfig = json.dumps(intf_details, indent=4)
     #   print(jsonconfig)
        intf_config = intf_details ["configure"]["port"]
        intf_info = intf_details["state"]["port"]
#
        print("")
    #    print(intf_details)
        print("Interface Details:")
        print("  Name: {}".format(intf_config["port-id"]))
        print("  Description: {}".format(intf_config["description"]))
        print("  Type: {}".format(intf_config["ethernet"]["mode"]))
        print("  MAC Address: {}".format(intf_info["hardware-mac-address"]))
        print("  Packets Input: {}".format(intf_info["statistics"]["in-packets"]))
        print("  Packets Output: {}".format(intf_info["statistics"]["out-packets"]))
        print("")
        

