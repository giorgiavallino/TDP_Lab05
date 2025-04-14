# Add whatever it is needed to interface with the DB Table corso

from database.DB_connect import DBConnect
from model.corso import Corso

class CorsoDAO:

    def __init__(self):
        pass

    def getAllCorsi(self):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = """SELECT *
                FROM corso c"""
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(Corso(row["codins"], row["crediti"], row["nome"], row["pd"]))
        cnx.close()
        return result

    def cercaCorsiByMatricola(self, codice_matricola):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = """SELECT *
                FROM iscrizione i, corso c
                WHERE i.codins=c.codins AND i.matricola=%s"""
        cursor.execute(query, (codice_matricola,))
        result = []
        for row in cursor:
            result.append(Corso(row["codins"], row["crediti"], row["nome"], row["pd"]))
        cnx.close()
        return result