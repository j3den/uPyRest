import json
import os


config = open("/config.json","r")
configDict = json.loads(config.read())
def postToFile(model,jsonDict):
	
	print("POST DAO:")
	returnString = ""
	for key in jsonDict.keys():
		print(key+" -> "+jsonDict[key])
		returnString = returnString+key+" -> "+jsonDict[key]+"\n"
	print("")
	#The CSV File that contains the models should have fields in order set in the config models.

	#return returnString

	
