import network
import time
import _thread
import display.DisplayServiceSingleton as disp


class WifiManager():

    def __init__(self, config):
        self.displayService = disp.DisplaySingleService()
        self.wifiSettings = config["wifiSettings"]
        self.wlan_intf = network.WLAN(network.STA_IF)
        self.wlan_intf.active(True)
        self.isConnected = False

    def statusCheck(self):
        print("Wifi Status Check Started")
        while True:
            if self.wlan_intf.isconnected:
                print(self.wlan_intf.isconnected())
                print("Connected!")
                self.isConnected = True
                ip_addr = self.wlan_intf.ifconfig()[0]
                while len(ip_addr)<15:
                    ip_addr = " "+ip_addr+" "

                self.displayService.clear()
                self.displayService.print_text("!!!!!!!!!!!!!!!!", 0)
                self.displayService.print_text("!   CONNECTED  !", 1)
                self.displayService.print_text("!              !", 2)
                self.displayService.print_text(     ip_addr      , 3)
                self.displayService.print_text("!              !", 4)
                self.displayService.print_text("!!!!!!!!!!!!!!!!", 5)
                time.sleep(15)


            else:
                self.isConnected = False
                self.displayService.clear()
                self.displayService.print_text("!!!!!!!!!!!!!!!!", 0)
                self.displayService.print_text("!    ERROR!    !", 1)
                self.displayService.print_text("!              !", 2)
                self.displayService.print_text("!     Lost     !", 3)
                self.displayService.print_text("!  Connection  !", 4)
                self.displayService.print_text("!!!!!!!!!!!!!!!!", 5)
                self.wlan_intf.connect()
                time.sleep(5)



    # Connect To WLAN
    def connectToWlan(self):
        self.displayService.print_text(" !* Wifi *! ", 0)
        self. displayService.print_text("Connect Wifi", 1)
        self.displayService.print_text("Starting Up..", 2)
        SSID = self.wifiSettings["ssid"]
        password = self.wifiSettings["password"]

        self.wlan_intf.connect(SSID, password)
        x = 1
        while not self.wlan_intf.isconnected():
            elipses = ""
            for i in range(0, x % 4):
                elipses = elipses + "."
                self.displayService.clear()
                self.displayService.print_text("Connecting" + elipses, 4)
                self.displayService.print_text("To "+SSID, 5)

            print(self.wlan_intf.status())
            x = x + 1
            time.sleep(0.5)
        self.isConnected = True
        print("CONNECTED")
        self.displayService.clear()
        self.displayService.print_text(" !*Connected *!", 0)
        self.displayService.print_text("To: ", 1)
        self.displayService.print_text(self.wlan_intf.ifconfig()[2], 2)
        self.displayService.print_text(" ",3)
        self.displayService.print_text("As IP:",4)
        self.displayService.print_text(self.wlan_intf.ifconfig()[0], 5)

        time.sleep(2.0)

        _thread.start_new_thread(self.statusCheck, ())

    def get_connected(self):
        time.sleep(0.5)
        return self.isConnected
