import json
import os


# Should be a singleton...
class POSTDaoService:
    _instance = None
    _SDDataSource = False
    _fileDataSource = False

    def __new__(self):
        if not self._instance:
            print("POSTDao : Forming Instance")
            self._instance = super(POSTDaoService, self).__new__(self)

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

        print("POSTDao : Formed Instance" + str(self._instance))
        return self._instance

    def post(self, model, body):

        if self._fileDataSource:

            dataFile = open("/database/" + model, "a+")

            if os.stat("/database/" + model)[6] > 0:
                dataFile.write("\n" + body)

            else:
                dataFile.write(body)

            dataFile.close()

        return True
