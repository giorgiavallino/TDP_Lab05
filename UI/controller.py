import flet as ft
from model.corso import Corso
from model.studente import Studente


class Controller:

    def __init__(self, view, model):
        # The view, with the graphical elements of the UI
        self._view = view
        # The model, which implements the logic of the program and holds the data
        self._model = model

    def getCorsi(self):
        return self._model.corsoDao.getAllCorsi()

    def cercaStudentiByCorso(self, e):
        self._view._txtOut.controls.clear()
        corso = self._view._ddCorsi.value
        if corso is None:
            self._view.create_alert("Selezionare un corso!")
            return
        studenti = self._model.cercaStudentiByCorso(corso)
        self._view._txtOut.controls.append(ft.Text(f"Sono iscritti {len(studenti)} studenti: "))
        for studente in studenti:
            self._view._txtOut.controls.append(ft.Text(f"{studente.__str__()}"))
        self._view.update_page()

    def cercaStudenteByMatricola(self, e):
        self._view._txtNome.value = ""
        self._view._txtCognome.value = ""
        self._view.update_page()
        codice_matricola = self._view._txtInMatricola.value
        if codice_matricola == "":
            self._view.create_alert("Inserire un codice matricola!")
            return
        elif codice_matricola.isnumeric() == False:
            self._view.create_alert("Inserire un codice numerico!")
            self._view._txtInMatricola.value = ""
            self._view.update_page()
            return
        codice_matricola = int(codice_matricola)
        matricole = self._model.getMatricole()
        if codice_matricola not in matricole:
            self._view.create_alert("Nessuno studente possiede questa matricola!")
            self._view._txtInMatricola.value = ""
            self._view.update_page()
            return
        studente = self._model.cercaStudenteByMatricola(codice_matricola)
        self._view._txtNome.value = studente.nome
        self._view._txtCognome.value = studente.cognome
        self._view.update_page()

    def cercaCorsiByMatricola(self, e):
        self._view._txtOut.controls.clear()
        self._view.update_page()
        codice_matricola = self._view._txtInMatricola.value
        if codice_matricola == "":
            self._view.create_alert("Inserire un codice matricola!")
            return
        elif codice_matricola.isnumeric() == False:
            self._view.create_alert("Inserire un codice numerico!")
            self._view._txtInMatricola.value = ""
            self._view.update_page()
            return
        codice_matricola = int(codice_matricola)
        matricole = self._model.getMatricole()
        if codice_matricola not in matricole:
            self._view.create_alert("Nessuno studente possiede questa matricola!")
            self._view._txtInMatricola.value = ""
            self._view.update_page()
            return
        corsi = self._model.cercaCorsiByMatricola(codice_matricola)
        self._view._txtOut.controls.append(ft.Text(f"Lo studente è iscritto a {len(corsi)} corsi: "))
        for corso in corsi:
            self._view._txtOut.controls.append(ft.Text(f"{corso.__str__()}"))
        self._view.update_page()