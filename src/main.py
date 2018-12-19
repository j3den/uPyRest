import NetworkManager as nman
import SocketService as ss
import json
import _thread

# Load up and Print Config File out.
config = open("/config.json", "r")
configDict = json.loads(config.read())
for key in configDict.keys():
    print(key + " -> " + str(configDict[key]))
    print("")

# Connect to Wireless Network.

wifiman = nman.WifiManager(configDict)
wifiman.connectToWlan()
while not wifiman.get_connected:
    print("Connecting...")


# Start the WebSocket Service.
def ssThread():
    ss.init()


_thread.start_new_thread(ssThread, ())
