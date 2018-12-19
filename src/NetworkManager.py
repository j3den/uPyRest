import network
import time
import display.DisplayService as ds

isConnected = False


# Connect To WLAN
def connectToWlan(config):
	display = ds.DisplayBuilder().get_display()
	wifiSettings = config["wifiSettings"]
	SSID = wifiSettings["ssid"]
	password = wifiSettings["password"]
	sta_if = network.WLAN(network.STA_IF);
	sta_if.active(True)
	sta_if.connect(SSID, password)
	x = 1
	while (sta_if.isconnected() == False):

		elipses = ""
		for i in range(0, x % 3):
			elipses = elipses + "."
		if (display is not None):
			display.fill(0)
			display.text("Connecting" + elipses, 0, 0)
			display.text("SSID: " + SSID, 0, 10)
			display.show()
		print("Connecting...")
		x = x + 1
		time.sleep(0.75)
	isConnected = True
	print("CONNECTED")
	if display is not None:
		display.fill(0)
		display.text("CONNECTED", 0, 0)
		display.show()


def getConnected():
	time.sleep(0.5)
	return isConnected
