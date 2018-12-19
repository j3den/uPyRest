import ssd1306
import machine
import json



class DisplayBuilder():

    def __init__(self):
        config = open("/config.json", "r")
        configDict = json.loads(config.read())
        displayDict = configDict["Display"]
        if displayDict.get("ssd1306") is True:
            print("SSD1306 Display init: scl = " + str(displayDict.get("scl_pin"))
                  + " sda = " + str(displayDict.get("sda_pin"))
                  + " oled_rst = " + str(displayDict.get("oled_rst_pin"))
                  + " width = " + str(displayDict.get("width"))
                  + " height = " + str(displayDict.get("height"))
                  )
            scl_pin = displayDict.get("scl_pin")
            sda_pin = displayDict.get("sda_pin")
            rst_pin = displayDict.get("oled_reset_pin")
            width = displayDict.get("width")
            height = displayDict.get("height")
            pin16 = machine.Pin(rst_pin, machine.Pin.OUT)
            pin16.value(1)
            i2c = machine.I2C(scl=machine.Pin(scl_pin), sda=machine.Pin(sda_pin))
            self.__oled = ssd1306.SSD1306_I2C(width, height, i2c)

    def get_display(self):
        return self.__oled
