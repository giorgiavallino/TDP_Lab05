from database.corso_DAO import CorsoDAO
from database.studente_DAO import StudenteDAO

class Model:

    def __init__(self):
        self.corsoDao = CorsoDAO()
        self.studenteDao = StudenteDAO()

    def getAllVoti(self):
        return self.corsoDao.getAllCorsi()

    def cercaStudentiByCorso(self, codice_corso):
        return self.studenteDao.cercaStudentiByCorso(codice_corso)

    def getMatricole(self):
        return self.studenteDao.getMatricole()

    def cercaStudenteByMatricola(self, codice_matricola):
        return self.studenteDao.cercaStudenteByMatricola(codice_matricola)

    def cercaCorsiByMatricola(self, codice_matricola):
        return self.corsoDao.cercaCorsiByMatricola(codice_matricola)

    def iscrivi(self, codice_matricola, codice_corso):
        return self.studenteDao.iscrivi(codice_matricola, codice_corso)

    def getCorsiStudente(self, codice_matricola):
        return self.studenteDao.getCorsiStudente(codice_matricola)