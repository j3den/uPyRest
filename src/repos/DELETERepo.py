import daos.DELETEDao as deleteDao
import display.DisplayServiceSingleton as ds


# Make singleton...

class DeleteRepo:
    _instance = None
    _display = ds.DisplaySingleService()
    _delete_dao = deleteDao.DELETEDao()
    _print_text = _display.print_text

    def __new__(self):
        if not self._instance:
            self._instance = super(DeleteRepo, self).__new__(self)
        print(self._instance)
        return self._instance

    def deleteAll(self, request, conn):
        print("DELETE Repo DeleteAll")
        parts = request.split("\\r\\n")

        # Id the model via the URL
        model = parts[0].split("/")[1].replace(" HTTP", "")
        self._print_text(str(model), 4)

        # Send model to DAO
        self._delete_dao.deleteAll(model)

        # Return 200
        conn.send("HTTP/1.1 200 OK\n" + "Content-Type: text/html\n" + "\n" + "DELETED")
        conn.close()
