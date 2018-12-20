import json
import os

# Should be a singleton...
class DELETEDao:
    _instance = None
    _SDDataSource = False
    _fileDataSource = False

    def __new__(self):
        if not self._instance:
            print("POSTDao : Forming Instance")
            self._instance = super(DELETEDao, self).__new__(self)
        config = open("/config.json", "r")
        configDict = json.loads(config.read())
        databaseConfig = configDict["Database"]

        print("DATABASE CONFIG:" + str(databaseConfig))
        if databaseConfig["Settings"].get("localFile"):
            self._fileDataSource = True
            print("Using File DataSource")
        if databaseConfig["Settings"].get("SDCard"):
            print("Using SD Card DataSource")
            self._SDDataSource = True
        print(self._instance)
        return self._instance

    def deleteAll(self, model):

        print("DELETE : deleteAll:" + model)

        if self._fileDataSource:
            os.remove("/database/"+model)

        return True
