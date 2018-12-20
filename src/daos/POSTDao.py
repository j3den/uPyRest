import json


#Should be a singleton...
class POSTDaoService():
	_instance = None
	_SDDataSource = False
	_fileDataSource = False

	def __new__(self):
		if not self._instance:
			print("POSTDao : Forming Instance")
			self._instance = super(POSTDaoService,self).__new__(self)
		config = open("/config.json", "r")
		configDict = json.loads(config.read())
		databaseConfig = configDict["Database"]

		print("DATABASE CONFIG:"+str(databaseConfig))
		if databaseConfig["Settings"].get("localFile"):
			self._fileDataSource = True
			print("Using File DataSource")
		if databaseConfig["Settings"].get("SDCard"):
			print("Using SD Card DataSource")
			self._SDDataSource = True
		print(self._instance)
		return self._instance


	def post(self,model,body):
		print(self._instance)
		print("POST DAO:" + model + " "+body)
		print("File save:"+str(self._fileDataSource))
		if self._fileDataSource:
			print("Saving To File...")
			print("Opening File : /database/"+model)
			dataFile = open("/database/"+model,"a+")
			print(dataFile)
			print("Writing to file..."+body)
			dataFile.write(body)
			print("Closing File")
			dataFile.close()
			print("Done")


		return True
		#The CSV File that contains the models should have fields in order set in the config models.

		#return returnString

	
