from device_info import Lab_7750
from ncclient import manager
import xmltodict
import logging
import json

# Enable logging
#logging.basicConfig(level=logging.DEBUG)

device = {
    "host": Lab_7750["address"], 
    "port": Lab_7750["port"],
    "username":Lab_7750["username"],
    "password":Lab_7750["password"],
    "hostkey_verify":False
}

# NETCONF Config Payload
#config_payload = """
#<config>
#  <configure xmlns="urn:nokia.com:sros:ns:yang:sr:conf">
#    <port>
#      <port-id>1/1/c4/1</port-id>
#      <description>config-by-netconf</description>
#      <ethernet>
#        <mode>hybrid</mode>
#      </ethernet>  
#    </port>
#  </configure>
#</config>
#"""

config_payload_json = {
	"config": {
		"configure": {
        "@xmlns": "urn:nokia.com:sros:ns:yang:sr:conf",
            "port": {
                "port-id": "1/1/c4/1",
                "description": "config-by-netconf",
                "ethernet": {
                    "mode": "hybrid"
                }
            }
		}
	}
}


#def main():
#    # Build the XML Configuration to Send
#    try:
#         with manager.connect(**device) as m:
#              print("Connected to {}".format(Lab_7750["address"]))
#              response = m.edit_config(target="candidate", config=config_payload)
#              print(response)
#              m.commit()
#                        
#              print("Configuration committed.")
#
#    except Exception as e:
#        print("An error occurred: {}".format(e))

def main():
    # Build the XML Configuration to Send
    try:
         with manager.connect(**device) as m:
              print("Connected to {}".format(Lab_7750["address"]))
              config_xml = xmltodict.unparse(config_payload_json)
              print(config_xml)
              response = m.edit_config(target="candidate", config=config_xml)
              print(response)
              m.validate()
              m.commit()
                        
              print("Configuration committed.")

    except Exception as e:
        print("An error occurred: {}".format(e))

if __name__ == '__main__':
    main()
