import machine
import time
import socket
import requests
import networkmanager as nman
import SocketService as ss

nman.connectToWlan()
while (nman.getConnected==False):
	print("Connecting...")
ss.init()
