import NetworkManager as nman
import SocketService as ss
import json
import _thread
import display.DisplayServiceSingleton as disp
import time


# Load up and Print Config File out.
config = open("/config.json", "r")
configDict = json.loads(config.read())
for key in configDict.keys():
    print(key + " -> " + str(configDict[key]))
    print("")

 # Init the Display Service
displayService = disp.DisplaySingleService()
displayService.print_text("   Hello!   ", 0)
displayService.print_text("Jonno's uPyRest", 1)
displayService.print_text("Starting Up..", 2)
time.sleep(3)

# Connect to Wireless Network.

wifiman = nman.WifiManager(configDict)
wifiman.connectToWlan()
while not wifiman.get_connected:
    print("Connecting...")


# Start the WebSocket Service.
def ssThread():
    ss.init()


_thread.start_new_thread(ssThread, ())
