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
        print(self._instance)
        print("GET DAO: getAll:" + model)

        if self._fileDataSource:
            print("Getting All From File...")
            print("Opening File : /database/" + model)
            dataFile = open("/database/" + model, "r+")
            print(dataFile)
            print("Fetching All Lines...")
            data = dataFile.read()
            print("Closing File")
            dataFile.close()
            print("Done")
            print(str(data))

        return data

# The CSV File that contains the models should have fields in order set in the config models.

# return returnString
