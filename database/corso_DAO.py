# Add whatever it is needed to interface with the DB Table corso

from database.DB_connect import DBConnect
from model.corso import Corso
from model.studente import Studente

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

    def getAllStudenti(self):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = """SELECT *
                FROM studenti s"""
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(Studente(row["matricola"], row["nome"], row["cognome"], row["cds"]))
        cnx.close()
        return result
