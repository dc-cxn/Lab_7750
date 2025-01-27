from device_info import Lab_7750
from ncclient import manager
import xmltodict
import logging
import json

# Enable logging
logging.basicConfig(level=logging.DEBUG)

# NETCONF Config Template to use
with open("config-template-port.xml") as f:
    netconf_template = f.read()

if __name__ == '__main__':
    # Build the XML Configuration to Send
    netconf_payload = netconf_template.format(int_name="1/1/c4/1",
                                              int_desc="Configured by NETCONF",
                                              int_mode="hybrid",
                                              )
    print("Configuration Payload:")
    print("----------------------")
    print(netconf_payload)

    try:
        with manager.connect(host=Lab_7750["address"], 
                        port=Lab_7750["port"],
                        username=Lab_7750["username"],
                        password=Lab_7750["password"],
                        hostkey_verify=False) as m:

            # Send NETCONF <edit-config>
            netconf_reply = m.edit_config(target="candidate", config=netconf_payload)

             # Print the NETCONF Reply
            print(netconf_reply)
    except Exception as e:
        print("An error occurred: {}".format(e))