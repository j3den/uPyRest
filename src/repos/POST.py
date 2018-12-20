import daos.POSTDao as postDao
import display.DisplayServiceSingleton as ds
import json
import uos


# Make singleton...

class PostRepo:
    _instance = None
    display = ds.DisplaySingleService()
    _postDao = postDao.POSTDaoService()
    _print_text = display.print_text

    def __new__(self):
        if not self._instance:
            self._instance = super(PostRepo, self).__new__(self)
        print(self._instance)
        return self._instance

    def persist(self, request):
        print(self._instance)

        parts = request.split("\\r\\n")

        # Id the model via the URL
        model = parts[0].split("/")[1].replace(" HTTP", "")
        self._print_text(str(model), 4)
        parts = request.split("\\r\\n")
        for i in range(0, len(parts)):
            if str(parts[i]) == "":  # Look for empty line...Following is body.

                try:
                    body = str(parts[i + 1][:-1])
                    json.loads(str(parts[i + 1][:-1]))
                except Exception as e:
                    print(e)
                    raise Exception("No JSON Body or Invalid!")

                # Post the model via DAO.
                self._postDao.post(model, body)
                print(model + " file is now " + str(uos.stat("/database/" + model)[6]) + " bytes")
        return True
