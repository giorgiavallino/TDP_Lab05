import flet as ft

class Controller:

    def __init__(self, view, model):
        # The view, with the graphical elements of the UI
        self._view = view
        # The model, which implements the logic of the program and holds the data
        self._model = model

    def getCorsi(self):
        return self._model.corsoDao.getAllCorsi()

    def cercaSIscritti(self, e):
        corso = self._view._ddCorsi.value
        if corso is None:
            self._view.create_alert("Selezionare un corso!")
            return