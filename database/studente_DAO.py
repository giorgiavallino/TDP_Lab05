# Add whatever it is needed to interface with the DB Table studente

from database.DB_connect import DBConnect
from model.studente import Studente

class StudenteDAO:

    def __init__(self):
        pass

    def cercaStudentiByCorso(self, codice_corso):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = """SELECT *
                FROM iscrizione i, studente s
                WHERE i.matricola=s.matricola AND i.codins=%s"""
        cursor.execute(query, (codice_corso,))
        result = []
        for row in cursor:
            result.append(Studente(row["matricola"], row["nome"], row["cognome"], row["CDS"]))
        cursor.close()
        cnx.close()
        return result

    def getMatricole(self):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = """SELECT s.matricola
                FROM studente s"""
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row["matricola"])
        cursor.close()
        cnx.close()
        return result

    def cercaStudenteByMatricola(self, codice_matricola):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = """SELECT *
                FROM studente s
                WHERE s.matricola=%s"""
        cursor.execute(query, (codice_matricola,))
        row = cursor.fetchone()
        studente = Studente(row["matricola"], row["nome"], row["cognome"], row["CDS"])
        cursor.close()
        cnx.close()
        return studente

    def iscrivi(self, codice_matricola, codice_corso):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = """INSERT INTO iscrizione
                (matricola, codins)
                VALUES (%s, %s)"""
        cursor.execute(query, (codice_matricola, codice_corso))
        cnx.commit()
        cursor.close()
        cnx.close()
        return

    def getCorsiStudente(self, codice_matricola):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = """SELECT codins
                FROM iscrizione
                WHERE matricola = %s"""
        cursor.execute(query, (codice_matricola,))
        result = []
        for row in cursor:
            result.append(row["codins"])
        cursor.close()
        cnx.close()
        return result