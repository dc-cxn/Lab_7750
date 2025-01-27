from Lab_7750.device_info import Lab_7750
from ncclient import manager
import xmltodict
import logging

#logging.basicConfig(
#    level=logging.DEBUG,
#)

if __name__ == '__main__':
    with manager.connect(host=Lab_7750["address"], 
                        port=Lab_7750["port"],
                        username=Lab_7750["username"],
                        password=Lab_7750["password"],
                        hostkey_verify=False) as m:
    
        print("here are the NETCONF Capabilities")
        for capability in m.server_capabilities:
            print(capability)
            

