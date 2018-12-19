import machine
import Requests as req
import NetworkManager as nman
import SocketService as ss
import json

#Load up and Print Config File out.
config = open("/config.json","r")
configDict = json.loads(config.read())
for key in configDict.keys():
		print(key+" -> "+str(configDict[key]))
		print("")


#Connect to Wireless Network.
nman.connectToWlan(configDict)
while (nman.getConnected==False):
	print("Connecting...")

#Start the WebSocket Service. Uses a blocking listener! Call last.
ss.init()



