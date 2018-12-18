import network
import time
import json
isConnected = False 

#Connect To WLAN
def connectToWlan():
	configFile = open("config.json","r")
	config = json.loads(configFile.read())
	print(config)
	print(config["wifiSettings"])
	wifiSettings = config["wifiSettings"]
	SSID = wifiSettings["ssid"]
	password = wifiSettings["password"]
	sta_if = network.WLAN(network.STA_IF);sta_if.active(True)
	sta_if.connect(SSID,password)
	while (sta_if.isconnected() == False):
        	print("Connecting...")
        	time.sleep(0.25)
	isConnected = True
	print("CONNECTED")

def getConnected():
	time.sleep(0.5)
	return isConnected


