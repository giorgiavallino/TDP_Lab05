import flet as ft

class View():

    def __init__(self, page: ft.Page):
        super().__init__()
        # Page stuff
        self._page = page
        self._page.title = "Lab O5 - Segreteria studenti"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.LIGHT
        # Controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None
        # Graphical elements
        self._title = None
        self._ddCorso = None
        self._btnCercaIscritti = None
        self._txtInMatricola = None
        self._txtNome = None
        self._txtCognome = None
        self._btnCercaStudente = None
        self._btnCercaCorsi = None
        self._btnIscrivi = None
        self._txtOut = None

    def fillDDCorso(self):
        corsi = self._controller.getCorsi()
        for corso in corsi:
            self._ddCorso.options.append(ft.dropdown.Option(key=corso.codins, text=corso.__str__()))

    def load_interface(self):
        """Function that loads the graphical elements of the view"""
        # Title
        self._title = ft.Text("App Gestione Studenti",
                              color="blue",
                              size=24)
        # Elementi grafici
        self._ddCorso = ft.Dropdown(value="Corso",
                                    label="Selezionare un corso",
                                    hint_text="Selezionare un corso",
                                    width=750)
        self.fillDDCorso()
        self._btnCercaIscritti = ft.ElevatedButton(text="Cerca iscritti",
                                                   disabled=True)
        self._txtInMatricola = ft.TextField(value="Matricola",
                                            hint_text="Inserisci il numero della matricola",
                                            width=200)
        self._txtNome = ft.TextField(value="Nome",
                                      read_only=True)
        self._txtCognome = ft.TextField(value="Cognome",
                                        read_only=True)
        self._btnCercaStudente = ft.ElevatedButton(text="Cerca studente",
                                                   disabled=True)
        self._btnCercaCorsi = ft.ElevatedButton(text="Cerca corsi",
                                                disabled=True)
        self._btnIscrivi = ft.ElevatedButton(text="Iscrivi",
                                             disabled=True)
        self._txtOut = ft.ListView(expand=True)
        row_01 = ft.Container(self._title,
                              alignment=ft.alignment.center)
        row_02 = ft.Row([self._ddCorso, self._btnCercaIscritti],
                        alignment=ft.MainAxisAlignment.CENTER)
        row_03 = ft.Row([self._txtInMatricola, self._txtNome, self._txtCognome],
                        alignment=ft.MainAxisAlignment.CENTER)
        row_04 = ft.Row([self._btnCercaStudente, self._btnCercaCorsi, self._btnIscrivi],
                        alignment=ft.MainAxisAlignment.CENTER)
        self._page.add(row_01, row_02, row_03, row_04, self._txtOut)
        self._page.update()

    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, controller):
        self._controller = controller

    def set_controller(self, controller):
        self._controller = controller

    def create_alert(self, message):
        """Function that opens a popup alert window, displaying a message
        :param message: the message to be displayed"""
        dlg = ft.AlertDialog(title=ft.Text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()

    def update_page(self):
        self._page.update()
