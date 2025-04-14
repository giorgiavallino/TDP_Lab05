from database.corso_DAO import CorsoDAO

class Model:

    def __init__(self):
        self.corsoDao = CorsoDAO()

    def getAllVoti(self):
        return self.corsoDao.getAllCorsi()