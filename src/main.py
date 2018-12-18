import machine
import Requests as req
import NetworkManager as nman
import SocketService as ss
import repos.POST as postrepo

nman.connectToWlan()
while (nman.getConnected==False):
	print("Connecting...")
ss.init()
postrepo.init()
