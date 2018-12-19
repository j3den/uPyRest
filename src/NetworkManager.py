import network
import time
import _thread
import display.DisplayService as ds


class WifiManager():

    def __init__(self, config):
        self.display = ds.DisplayBuilder().get_display()
        self.wifiSettings = config["wifiSettings"]
        self.sta_if = network.WLAN(network.STA_IF)
        self.sta_if.active(True)
        self.isConnected = False


    def statusCheck(self):
        print("Wifi Status Check Started")
        blip_bool = False
        while True:
            self.display.fill(0)
            if self.sta_if.isconnected:
                print("Connected!")
                self.isConnected = True

                if blip_bool:
                    self.display.text("CONN", 0, 0)
                else:
                    self.display.text("CONN..", 0, 0)
                self.display.show()

                time.sleep(1)
            else:
                print("Connected NOT!!!")
                self.isConnected = False
                self.display.fill(0)
                if blip_bool:
                    self.display.text("CERR!", 0, 0)
                else:
                    self.display.text("CERR#.", 0, 0)
                self.display.show()
                self.sta_if.connect()
                time.sleep(1)

            blip_bool = not blip_bool

    # Connect To WLAN
    def connectToWlan(self):
        SSID = self.wifiSettings["ssid"]
        password = self.wifiSettings["password"]

        self.sta_if.connect(SSID, password)
        x = 1
        while not self.sta_if.isconnected():
            elipses = ""
            for i in range(0, x % 3):
                elipses = elipses + "."
            if self.display is not None:
                self.display.fill(0)
                self.display.text("Connecting" + elipses, 0, 0)
                self.display.text("SSID: " + SSID, 0, 10)
                self.display.show()
            print("Connecting...")
            x = x + 1
            time.sleep(0.75)
        self.isConnected = True
        print("CONNECTED")
        if self.display is not None:
            self.display.fill(0)
            self.display.text("CON", 0, 0)
            self.display.show()
            _thread.start_new_thread(self.statusCheck, ())

    def get_connected(self):
        time.sleep(0.5)
        return self.isConnected
