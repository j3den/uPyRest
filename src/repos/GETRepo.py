import display.DisplayServiceSingleton as ds
import daos.GETDao as getDao


# Make singleton...

class GetRepo():
    _instance = None
    _display = ds.DisplaySingleService()
    _get_dao = getDao.GETDaoService()
    _print_text = _display.print_text

    def __new__(self):
        if not self._instance:
            self._instance = super(GetRepo, self).__new__(self)
        print(self._instance)
        return self._instance

    def getAll(self, request):
        print(self._instance)
        print("GET REPO GET")
        parts = request.split("\\r\\n")

        # Id the model via the URL
        model = parts[0].split("/")[1].replace(" HTTP", "")
        self._print_text(str(model), 4)
        self._get_dao.getAll(model)

        return True
