import json


# Should be a singleton...
class GETDaoService():
    _instance = None
    _SDDataSource = False
    _fileDataSource = False

    def __new__(self):
        if not self._instance:
            print("POSTDao : Forming Instance")
            self._instance = super(GETDaoService, self).__new__(self)
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

    def getAll(self, model):
        print("GET DAO: getAll: " + model)

        if self._fileDataSource:
            dataFile = open("/database/" + model, "r+")
            data = dataFile.read()
            dataFile.close()

        return data

# The CSV File that contains the models should have fields in order set in the config models.

# return returnString
