import NetworkManager as nman
import SocketService as ss
import json
import _thread
import display.DisplayServiceSingleton as disp
import time
import os
# Load up and Print Config File out.
config = open("/config.json", "r")
configDict = json.loads(config.read())
for key in configDict.keys():
    print(key + " -> " + str(configDict[key]))
    print("")

#Create Database Folder if does not exist:
print("Directory List:")
dirs = os.listdir("/")
hasDatabaseDir = False
for dir in range(0,len(dirs)):
    print(dirs[dir])
    if dirs[dir] == "database":
        hasDatabaseDir = True
if not hasDatabaseDir:
    print("Forming Database folder...")
    os.mkdir("/database")
else:
    print("Contains Database Folder.")


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


try:
    _thread.start_new_thread(ssThread, ())
except Exception as e:
    print(e)
