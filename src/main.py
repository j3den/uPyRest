import machine
import Requests as req
import NetworkManager as nman
import SocketService as ss
import json
import ssd1306
import display.DisplayService as ds

#Load up and Print Config File out.
config = open("/config.json","r")
configDict = json.loads(config.read())
for key in configDict.keys():
		print(key+" -> "+str(configDict[key]))
		print("")

display = ds.DisplayBuilder().get_display()
display.fill(0)
display.text('MicroPython on', 0, 0)
display.text('an ESP32 with an', 0, 10)
display.text('attached SSD1306', 0, 20)
display.text('OLED display', 0, 30)
display.show()

#Connect to Wireless Network.
nman.connectToWlan(configDict)
while (nman.getConnected==False):
	print("Connecting...")

#Start the WebSocket Service. Uses a blocking listener! Call last.
ss.init()



