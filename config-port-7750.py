from device_info import Lab_7750
from ncclient import manager
import xmltodict
import logging
import json

# NETCONF Config Template to use
netconf_template = open("config-template-port.xml").read()

if __name__ == '__main__':
    # Build the XML Configuration to Send
    netconf_payload = netconf_template.format(int_name="1/1/c4/1",
                                              int_desc="Configured by NETCONF",
                                              int_mode="hybrid",
                                              )
    print("Configuration Payload:")
    print("----------------------")
    print(netconf_payload)

    with manager.connect(host=Lab_7750["address"], 
                        port=Lab_7750["port"],
                        username=Lab_7750["username"],
                        password=Lab_7750["password"],
                        hostkey_verify=False) as m:

        # Send NETCONF <edit-config>
        netconf_reply = m.edit_config(netconf_payload, target="running")

        # Print the NETCONF Reply
        print(netconf_reply)