import machine
import network
import urequests
import ujson

def sayHello():
	print("I am the Requests File!")

def getRequest(url):
	response = urequests.get(url)
	print(type(response))
	print(response.text)
	print(type(response.text))
	asJson = ujson.loads(response.text)
